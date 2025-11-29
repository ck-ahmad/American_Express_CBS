from flask import Flask, render_template, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from functools import wraps

# =====================================
#            FLASK SETUP
# =====================================
app = Flask(__name__)
app.secret_key = "nsluvurhozqetrxz"

# ============ DATABASE (SQLite) =============
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cbs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# =====================================
#              MODELS
# =====================================
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

class Customer(db.Model):
    CustomerID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('user.id'))
    Name = db.Column(db.String(100), nullable=False)
    CNIC = db.Column(db.String(20), unique=True, nullable=False)
    Contact = db.Column(db.String(20), nullable=False)

class Account(db.Model):
    AccountNo = db.Column(db.Integer, primary_key=True)
    CustomerID = db.Column(db.Integer, db.ForeignKey('customer.CustomerID'))
    Email = db.Column(db.String(120), nullable=False)
    Type = db.Column(db.String(20), nullable=False)
    Balance = db.Column(db.Float, default=0.00)
    
    customer = db.relationship('Customer', backref='accounts')

class TransactionLog(db.Model):
    TransID = db.Column(db.Integer, primary_key=True)
    FromAccount = db.Column(db.Integer)
    ToAccount = db.Column(db.Integer)
    Amount = db.Column(db.Float, nullable=False)
    Type = db.Column(db.String(20), nullable=False)
    DateTime = db.Column(db.DateTime, default=datetime.utcnow)
    UserID = db.Column(db.Integer)

class AuditLog(db.Model):
    LogID = db.Column(db.Integer, primary_key=True)
    Operation = db.Column(db.String(20), nullable=False)
    TableAffected = db.Column(db.String(20), nullable=False)
    UserName = db.Column(db.String(20), nullable=False)
    DateTime = db.Column(db.DateTime, default=datetime.utcnow)

# =====================================
#       LOGIN REQUIRED DECORATOR
# =====================================
def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if "user" not in session:
            return redirect("/login")
        return fn(*args, **kwargs)
    return wrapper

# =====================================
#                AUTH
# =====================================
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        if User.query.filter_by(username=username).first():
            flash("Username already exists!", "error")
            return redirect("/register")

        hashed_pw = generate_password_hash(password)
        user = User(username=username, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful! Please login.", "success")
        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session["user"] = user.id
            session["username"] = user.username
            return redirect("/")

        flash("Invalid username or password!", "error")
        return redirect("/login")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out successfully.", "success")
    return redirect("/login")


# =====================================
#                HOME
# =====================================
@app.route("/")
@login_required
def index():
    # Get statistics
    customers = Customer.query.filter_by(UserID=session["user"]).all()
    accounts = Account.query.join(Customer).filter(Customer.UserID == session["user"]).all()
    total_balance = sum([acc.Balance for acc in accounts])
    recent_transactions = TransactionLog.query.filter_by(UserID=session["user"]).order_by(TransactionLog.DateTime.desc()).limit(5).all()
    
    return render_template("index.html", 
                         customer_count=len(customers),
                         account_count=len(accounts),
                         total_balance=total_balance,
                         recent_transactions=recent_transactions)


# =====================================
#              CUSTOMER
# =====================================
@app.route("/customer")
@login_required
def customer():
    customers = Customer.query.filter_by(UserID=session["user"]).all()
    return render_template("customer.html", customers=customers)

@app.route("/customer/add", methods=["POST"])
@login_required
def add_customer():
    name = request.form.get("name")
    cnic = request.form.get("cnic")
    contact = request.form.get("contact")

    if Customer.query.filter_by(CNIC=cnic).first():
        flash("Customer with this CNIC already exists!", "error")
        return redirect("/customer")

    c = Customer(Name=name, CNIC=cnic, Contact=contact, UserID=session["user"])
    db.session.add(c)
    
    log = AuditLog(Operation="INSERT", TableAffected="Customer", UserName=session.get("username", "unknown"))
    db.session.add(log)
    
    db.session.commit()
    flash("Customer added successfully!", "success")
    return redirect("/customer")

@app.route("/customer/delete/<int:id>")
@login_required
def delete_customer(id):
    customer = Customer.query.filter_by(CustomerID=id, UserID=session["user"]).first()
    if customer:
        # Check if customer has accounts
        if Account.query.filter_by(CustomerID=id).first():
            flash("Cannot delete customer with active accounts!", "error")
        else:
            db.session.delete(customer)
            log = AuditLog(Operation="DELETE", TableAffected="Customer", UserName=session.get("username", "unknown"))
            db.session.add(log)
            db.session.commit()
            flash("Customer deleted successfully!", "success")
    return redirect("/customer")


# =====================================
#              ACCOUNT
# =====================================
@app.route("/account")
@login_required
def account():
    accounts = Account.query.join(Customer).filter(
        Customer.UserID == session["user"]
    ).all()
    customers = Customer.query.filter_by(UserID=session["user"]).all()
    return render_template("account.html", accounts=accounts, customers=customers)

@app.route("/account/add", methods=["POST"])
@login_required
def add_account():
    customer_id = request.form["customer_id"]
    acc_type = request.form["type"]
    balance = float(request.form["balance"])
    email = request.form["email"]

    customer = Customer.query.filter_by(CustomerID=customer_id, UserID=session["user"]).first()
    if not customer:
        flash("Invalid customer selected!", "error")
        return redirect("/account")

    acc = Account(CustomerID=customer_id, Type=acc_type, Balance=balance, Email=email)
    db.session.add(acc)

    log = AuditLog(Operation="INSERT", TableAffected="Account", UserName=session.get("username", "unknown"))
    db.session.add(log)
    
    # Log initial deposit
    trans = TransactionLog(ToAccount=None, Amount=balance, Type="Deposit", UserID=session["user"])
    db.session.add(trans)

    db.session.commit()
    flash("Account created successfully!", "success")
    return redirect("/account")


# =====================================
#          TRANSACTIONS
# =====================================
@app.route("/transaction")
@login_required
def transaction():
    transactions = TransactionLog.query.filter_by(UserID=session["user"]).order_by(TransactionLog.DateTime.desc()).all()
    accounts = Account.query.join(Customer).filter(Customer.UserID == session["user"]).all()
    return render_template("transaction.html", transactions=transactions, accounts=accounts)

@app.route("/transaction/add", methods=["POST"])
@login_required
def add_transaction():
    trans_type = request.form["type"]
    amount = float(request.form["amount"])
    
    if trans_type in ["Deposit", "Withdraw"]:
        account_no = int(request.form["account"])
        account = Account.query.join(Customer).filter(
            Account.AccountNo == account_no,
            Customer.UserID == session["user"]
        ).first()
        
        if not account:
            flash("Invalid account!", "error")
            return redirect("/transaction")
        
        if trans_type == "Deposit":
            account.Balance += amount
            trans = TransactionLog(ToAccount=account_no, Amount=amount, Type="Deposit", UserID=session["user"])
        else:
            if account.Balance < amount:
                flash("Insufficient balance!", "error")
                return redirect("/transaction")
            account.Balance -= amount
            trans = TransactionLog(FromAccount=account_no, Amount=amount, Type="Withdraw", UserID=session["user"])
        
        db.session.add(trans)
        db.session.commit()
        flash(f"{trans_type} successful!", "success")
    
    elif trans_type == "Transfer":
        from_account = int(request.form["from_account"])
        to_account = int(request.form["to_account"])
        
        acc_from = Account.query.join(Customer).filter(
            Account.AccountNo == from_account,
            Customer.UserID == session["user"]
        ).first()
        
        acc_to = Account.query.get(to_account)
        
        if not acc_from or not acc_to:
            flash("Invalid account numbers!", "error")
            return redirect("/transaction")
        
        if acc_from.Balance < amount:
            flash("Insufficient balance!", "error")
            return redirect("/transaction")
        
        acc_from.Balance -= amount
        acc_to.Balance += amount
        
        trans = TransactionLog(FromAccount=from_account, ToAccount=to_account, Amount=amount, Type="Transfer", UserID=session["user"])
        db.session.add(trans)
        db.session.commit()
        flash("Transfer successful!", "success")
    
    return redirect("/transaction")


# =====================================
#           AUDIT LOGS
# =====================================
@app.route("/audit")
@login_required
def audit():
    logs = AuditLog.query.order_by(AuditLog.DateTime.desc()).limit(50).all()
    return render_template("audit.html", logs=logs)


# =====================================
#           DB CREATE + RUN
# =====================================
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)