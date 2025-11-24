# 🏦 American Express - Core Banking System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg) ![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg) ![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg) ![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**A premium banking management system inspired by American Express**

*Core Banking System - DBMS Project*

<img width="959" height="419" alt="image" src="https://github.com/user-attachments/assets/9b092e6e-98f7-4d50-9360-b81c84492c02" />


[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Team](#team) • [Documentation](#documentation)

</div>
---

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Team Members](#team-members)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

The **American Express Core Banking System** is a comprehensive banking management application developed as part of our Database Management System coursework. This project demonstrates advanced database concepts including transaction control (TCL), audit logging, and secure financial operations.

Built with a professional American Express-inspired black theme, the system provides a modern, intuitive interface for managing banking operations including member registration, account management, and secure financial transactions.

### 🎓 Academic Context

- **Course:** Database Management System
- **Institution:** Fast Nuces
- **Semester:** 5TH
- **Project Type:** Team Collaborative Project

---

## ✨ Features

### 🏠 Core Functionality

- **Member Management**
  - Register new members with CNIC verification
  - View comprehensive member directory
  - Track membership tiers (Centurion, Platinum, Gold)
  - Member profile management

- **Account Services**
  - Create multiple account types (Savings, Current, Fixed Deposit)
  - Real-time balance tracking
  - Account statistics and analytics
  - Multi-currency support (PKR)

- **Transaction Management**
  - **Deposit:** Add funds to accounts
  - **Withdraw:** Remove funds with balance validation
  - **Transfer:** Secure inter-account transfers
  - Complete transaction history
  - Real-time processing

- **Security & Audit**
  - Comprehensive audit trail logging
  - Transaction control (COMMIT, ROLLBACK, SAVEPOINT)
  - Activity monitoring dashboard
  - Tamper-proof logging system

### 🎨 Design Features

- American Express premium black theme
- Responsive design for all devices
- Professional gradient cards and components
- Real-time statistics dashboard
- Intuitive navigation system
- Professional icons and badges

---

## 🛠️ Technology Stack

### Backend
- **Python 3.8+** - Core programming language
- **Flask 3.0.0** - Web framework
- **MySQL 8.0+** - Relational database management
- **mysql-connector-python** - Database driver

### Frontend
- **HTML5** - Structure and content
- **CSS3** - Styling and animations
- **JavaScript (Vanilla)** - Client-side functionality
- **SVG** - Professional icons

### Development Tools
- **Git** - Version control
- **VS Code** - Code editor
- **XAMPP** - Local development environment
- **phpMyAdmin** - Database administration

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────┐
│           Presentation Layer (Frontend)         │
│    HTML5 • CSS3 • JavaScript • SVG Icons        │
└─────────────────────────────────────────────────┘
                       ↕
┌─────────────────────────────────────────────────┐
│         Application Layer (Backend)             │
│      Flask Routes • Business Logic • API        │
└─────────────────────────────────────────────────┘
                       ↕
┌─────────────────────────────────────────────────┐
│           Data Layer (Database)                 │
│    MySQL • Transaction Control • Audit Logs     │
└─────────────────────────────────────────────────┘
```

### Database Schema

```sql
Customer
├── CustomerID (PK)
├── Name
├── CNIC (Unique)
└── Contact

Account
├── AccountNo (PK)
├── CustomerID (FK)
├── Type
└── Balance

TransactionLog
├── TransID (PK)
├── FromAccount (FK)
├── ToAccount (FK)
├── Amount
├── Type
└── DateTime

AuditLog
├── LogID (PK)
├── Operation
├── TableAffected
├── UserName
└── DateTime
```

---

## 📦 Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- MySQL 8.0 or higher
- pip (Python package manager)
- XAMPP (recommended) or standalone MySQL server

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/american-express-banking.git
cd american-express-banking
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt:**
```
flask==3.0.0
mysql-connector-python==8.2.0
```

---

## 🗄️ Database Setup

### Option 1: Using phpMyAdmin (Recommended)

1. Start XAMPP and ensure MySQL is running
2. Open phpMyAdmin (`http://localhost/phpmyadmin`)
3. Create a new database named `cbs`
4. Import the `database.sql` file:
   - Click on the `cbs` database
   - Go to the "Import" tab
   - Choose the `database.sql` file
   - Click "Go"

### Option 2: Using MySQL Command Line

```bash
# Login to MySQL
mysql -u root -p

# Create database and import
CREATE DATABASE cbs;
USE cbs;
SOURCE /path/to/database.sql;
```

### Option 3: Using MySQL Workbench

1. Open MySQL Workbench
2. Connect to your local MySQL instance
3. File → Run SQL Script
4. Select `database.sql`
5. Execute

### Database Configuration

Update the database credentials in `app.py`:

```python
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",           # Your MySQL username
        password="",           # Your MySQL password
        database="cbs"
    )
```

---

## 🚀 Usage

### Starting the Application

```bash
# Ensure you're in the project directory and virtual environment is activated
python app.py
```

The application will start on `http://127.0.0.1:5000`

### Accessing the Application

Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

### Default Features

The system comes pre-loaded with sample data:
- 3 sample members
- 3 sample accounts
- 2 sample transactions
- Complete audit trail

### User Workflows

#### 1. Register a New Member
```
Home → Members → Add New Member → Fill Form → Submit
```

#### 2. Create an Account
```
Home → Accounts → Open Premium Account → Select Member → Choose Type → Submit
```

#### 3. Perform Transaction
```
Home → Transactions → Choose Transaction Type → Enter Details → Submit
```

#### 4. View Activity Logs
```
Home → Activity → View Complete Audit Trail
```

---

## 📁 Project Structure

```
american-express-banking/
│
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── database.sql                    # Database schema and sample data
├── README.md                       # Project documentation
│
├── static/
│   └── style.css                  # American Express black theme CSS
│
├── templates/
│   ├── index.html                 # Home page
│   ├── customer.html              # Member management
│   ├── account.html               # Account management
│   ├── transaction.html           # Transaction operations
│   ├── logs.html                  # Audit logs
│   └── support.html               # Developer contact
│
└── docs/
    ├── API_DOCUMENTATION.md       # API endpoint documentation
    ├── DATABASE_DESIGN.md         # Database schema details
    └── USER_GUIDE.md              # End-user guide
```

## 👥 Team Members

<table>
  <tr>
    <td align="center">
      <img src="https://via.placeholder.com/150" width="100px;" alt="Ahmad"/>
      <br />
      <sub><b>Ahmad</b></sub>
      <br />
      <sub>Lead Developer</sub>
      <br />
      <a href="mailto:ahmadleo498@gmail.com">📧 Email</a> •
      <a href="https://github.com/ck-ahmad">💻 GitHub</a>
    </td>
    <td align="center">
      <img src="https://via.placeholder.com/150" width="100px;" alt="Hadia"/>
      <br />
      <sub><b>Hadia</b></sub>
      <br />
      <sub>Frontend Developer</sub>
      <br />
      <a href="mailto:hadia@gmail.com">📧 Email</a> •
      <a href="https://github.com/hadia">💻 GitHub</a>
    </td>
    <td align="center">
      <img src="https://via.placeholder.com/150" width="100px;" alt="Tabbaya"/>
      <br />
      <sub><b>Tabbaya</b></sub>
      <br />
      <sub>Database Specialist</sub>
      <br />
      <a href="mailto:tabbaya@gmail.com">📧 Email</a> •
      <a href="https://github.com/tabbaya">💻 GitHub</a>
    </td>
  </tr>
</table>

### 🎯 Contributions

| Team Member | Primary Responsibilities |
|-------------|-------------------------|
| **Ahmad** | Backend development, Flask routes, API integration, transaction logic |
| **Hadia** | Frontend design, UI/UX, CSS styling, responsive layouts |
| **Tabbaya** | Database design, SQL queries, audit logging, data integrity |

*All team members contributed collaboratively to project planning, testing, and documentation.*

---

## 🔐 Security Features

### Transaction Control (TCL)

The system implements comprehensive transaction control:

- **COMMIT**: Automatically commits successful transactions
- **ROLLBACK**: Reverts failed transactions to maintain data integrity
- **SAVEPOINT**: Uses savepoints for complex multi-step operations

Example from `app.py`:
```python
try:
    # Perform transaction
    cursor.execute("UPDATE Account SET Balance = ...")
    db.commit()  # COMMIT on success
except Exception as e:
    db.rollback()  # ROLLBACK on failure
```

### Audit Logging

Every system operation is automatically logged:
- User identification
- Operation type (INSERT, UPDATE, DELETE)
- Table affected
- Timestamp
- Complete audit trail

### Data Validation

- CNIC format validation
- Balance verification before withdrawals
- Account existence checks
- Input sanitization
- SQL injection prevention through parameterized queries

---

## 📊 Database Concepts Demonstrated

### 1. Normalization
- All tables are in **3rd Normal Form (3NF)**
- No redundant data
- Proper foreign key relationships

### 2. Referential Integrity
- Foreign key constraints
- CASCADE operations
- Data consistency enforcement

### 3. Transaction Management
- ACID properties implementation
- Atomic operations
- Consistency guarantees

### 4. Triggers (Implemented via Application Logic)
- Automatic audit log generation
- Balance update tracking
- Transaction validation

---

## 🧪 Testing

### Running Tests

```bash
# Test database connection
python test_db.py

# Test API endpoints
python test_api.py

# Run all tests
python -m pytest tests/
```

### Manual Testing Checklist

- [ ] Member registration
- [ ] Account creation
- [ ] Deposit transaction
- [ ] Withdrawal transaction
- [ ] Transfer between accounts
- [ ] Audit log generation
- [ ] Balance validation
- [ ] Error handling

---

## 🐛 Troubleshooting

### Common Issues

**Issue:** `ModuleNotFoundError: No module named 'flask'`
```bash
Solution: pip install flask mysql-connector-python
```

**Issue:** `Can't connect to MySQL server`
```bash
Solution: 
1. Ensure MySQL is running in XAMPP
2. Check credentials in app.py
3. Verify database 'cbs' exists
```

**Issue:** `TemplateNotFound: index.html`
```bash
Solution: 
1. Ensure templates folder exists
2. Verify all HTML files are in templates/
3. Check folder structure
```

**Issue:** Port 5000 already in use
```bash
Solution: Change port in app.py
app.run(debug=True, port=5001)
```

---

## 📚 Documentation

### Additional Resources

- [API Documentation](docs/API_DOCUMENTATION.md) - Complete API reference
- [Database Design](docs/DATABASE_DESIGN.md) - ERD and schema details
- [User Guide](docs/USER_GUIDE.md) - End-user instructions
- [Developer Guide](docs/DEVELOPER_GUIDE.md) - Contributing guidelines

---

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add comments for complex logic
- Update documentation for new features

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **American Express** - Design inspiration
- **Flask Documentation** - Technical guidance
- **MySQL Documentation** - Database reference
- **Our Professor** - Project guidance and support
- **Open Source Community** - Icons and resources

---

## 📞 Contact & Support

### Team Contact

For questions, suggestions, or support:

- **Email:** ahmad@example.com, hadia@example.com, tabbaya@example.com
- **Project Repository:** [GitHub](https://github.com/ck-ahmad/American_Express_CBS)
- **Issues:** [Report a Bug](https://github.com/ck-ahmad/American_Express_CBS/issues)

### Response Time

We typically respond to inquiries within 24 hours.

---

## 🗺️ Roadmap

### Current Version: 1.0.0

### Future Enhancements

- [ ] User authentication system
- [ ] Email notifications
- [ ] Export to PDF/Excel
- [ ] Advanced search and filtering
- [ ] Mobile application
- [ ] Multi-language support
- [ ] Real-time notifications
- [ ] Biometric authentication
- [ ] AI-powered fraud detection
- [ ] Blockchain integration

---


<div align="center">

**Built with ❤️ by Ahmad, Hadia & Tabbaya**

*Database Management System Project - 2024*

⭐ Star this repository if you found it helpful!

</div>

---

## 🔖 Version History

### Version 1.0.0 (2025-11-23)
- Initial release
- Complete member management
- Account services implementation
- Transaction management (Deposit, Withdraw, Transfer)
- Audit logging system
- American Express premium theme
- Responsive design
- Complete documentation

---

**© 2025 American Express Banking System. All Rights Reserved.**

*This is an academic project and is not affiliated with American Express Company.*
