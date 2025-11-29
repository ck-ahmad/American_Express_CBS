# 🏦 Core Banking System (CBS) - DBMS Project

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg) 
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg) 
![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey.svg) 
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
[![YouTube](https://img.shields.io/badge/YouTube-Subscribe-red)]()

---

<img width="956" height="418" alt="image" src="https://github.com/user-attachments/assets/aea4b310-c136-43f3-9c27-dd3de4ada03e" />

---

**A premium banking system backend built with Flask and SQLite**  

*Database Management System Project*

[Features](#features) • [Installation](#installation) • [Docker Setup](#docker-setup) • [Usage](#usage) • [Project Structure](#project-structure) • [Team](#team-members)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Technology Stack](#technology-stack)  
- [Installation](#installation)  
- [Docker Setup](#docker-setup)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Team Members](#team-members)  
- [License](#license)  

---

## 🎯 Overview

This **Core Banking System (CBS)** backend provides a foundation for managing:  

- User authentication (Register/Login/Logout)  
- Customer management  
- Account management  
- Financial transactions (Deposit, Withdraw, Transfer)  
- Audit logging  

The backend uses **Flask**, **SQLite**, and follows MVC principles to separate business logic, data models, and templates.

---

## ✨ Features

### 🔐 Authentication
- User registration with **hashed passwords**
- Login and session management
- Logout and session clearing

### 🏦 Customer Management
- Add, view, and delete customers
- CNIC uniqueness validation
- Audit logging for all operations

### 💳 Account Management
- Create accounts (Savings, Current, Fixed Deposit)
- Associate accounts with customers
- Initial deposit recorded as transaction
- Audit logs for account operations

### 💸 Transactions
- **Deposit** and **Withdraw** with balance validation
- **Transfer** between accounts
- Transaction history logging
- Audit logs for all financial operations

### 📝 Audit Logs
- Record every INSERT/DELETE operation
- Track affected table, operation type, user, and timestamp
- View recent 50 audit logs

---

## 🛠️ Technology Stack

**Backend**
- Python 3.8+  
- Flask 3.0.0  
- SQLite (local database)  
- Werkzeug (password hashing)  

**Frontend Templates**
- HTML  
- Jinja2 templates for dynamic rendering  

**Tools**
- VS Code / PyCharm  
- SQLite Browser (optional)  

---

## 📦 Installation

### Prerequisites
- Python 3.8+ installed
- pip (Python package manager)

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/cbs-flask-backend.git
cd cbs-flask-backend

# 2. Create a virtual environment
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
````

**requirements.txt**

```
Flask==3.0.0
Flask_SQLAlchemy==3.0.0
Werkzeug==2.3.0
```

---

## 🐳 Docker Setup

```bash
# Build the Docker image
docker build -t ck714/cbs-backend:0.0.1 .

# Run the container
docker container run -d -p 5000:5000 ck714/cbs-backend:0.0.1

# List running containers
docker container ls

# Stop a container
docker container stop <container_id_or_name>
```

---

## 🚀 Usage

### Start the Flask App

```bash
python app.py
```

Open in browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### Default Features

* Admin can register new users
* CRUD operations for customers
* Account creation with initial deposits
* Deposit, Withdraw, Transfer transactions
* Audit logs viewable for tracking all operations

---

## 📁 Project Structure

```
cbs-flask-backend/
├── app.py                     # Main Flask application
├── requirements.txt           # Python dependencies
├── cbs.db                     # SQLite database (auto-created)
├── templates/                 # HTML templates
│   ├── login.html
│   ├── register.html
│   ├── index.html
│   ├── customer.html
│   ├── account.html
│   ├── transaction.html
│   └── audit.html
└── static/                     # CSS & JS (optional)
```

---

## 👥 Team Members

| Name    | Role                | Contact                                                  | GitHub                                |
| ------- | ------------------- | -------------------------------------------------------- | ------------------------------------- |
| Ahmad   | Backend Developer   | 📧 [ahmadleo498@gmail.com](mailto:ahmadleo498@gmail.com) | [GitHub](https://github.com/ck-ahmad) |
| Hadia   | Frontend Developer  | 📧 [hadia@gmail.com](mailto:hadia@gmail.com)             | [GitHub](https://github.com/hadia)    |
| Tabbaya | Database Specialist | 📧 [tabbaya@gmail.com](mailto:tabbaya@gmail.com)         | [GitHub](https://github.com/tabbaya)  |

---

## 📄 License

MIT License - see [LICENSE](LICENSE)

---

<div align="center">
**Built with ❤️ by Ahmad, Hadia & Tabbaya**  
*Database Management System Project - 2025*  
⭐ Star this repository if helpful!
</div>



