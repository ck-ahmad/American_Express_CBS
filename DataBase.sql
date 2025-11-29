-- ================================================
-- CORE BANKING SYSTEM DATABASE (EMAIL-BASED ACCOUNTS)
-- ================================================

DROP DATABASE IF EXISTS rncbs;
CREATE DATABASE rncbs;
USE rncbs;

-- ================================================
-- TABLE 1: Users (login info)
-- ================================================
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- ================================================
-- TABLE 2: Customer
-- ================================================
CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    CNIC VARCHAR(20) UNIQUE NOT NULL,
    Contact VARCHAR(20) NOT NULL,
    UserID INT NOT NULL,
    FOREIGN KEY (UserID) REFERENCES users(id)
);

-- ================================================
-- TABLE 3: Account
-- ================================================
CREATE TABLE Account (
    AccountNo INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    Email VARCHAR(100) NOT NULL,        -- store owner email
    Type VARCHAR(20) NOT NULL,
    Balance DECIMAL(12,2) DEFAULT 0.00,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

-- ================================================
-- TABLE 4: TransactionLog
-- ================================================
CREATE TABLE TransactionLog (
    TransID INT PRIMARY KEY AUTO_INCREMENT,
    FromAccount INT,
    ToAccount INT,
    Amount DECIMAL(12,2) NOT NULL,
    Type VARCHAR(20) NOT NULL,
    DateTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ================================================
-- TABLE 5: AuditLog
-- ================================================
CREATE TABLE AuditLog (
    LogID INT PRIMARY KEY AUTO_INCREMENT,
    Operation VARCHAR(20) NOT NULL,
    TableAffected VARCHAR(20) NOT NULL,
    UserName VARCHAR(20) NOT NULL,
    DateTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ================================================
-- SAMPLE DATA
-- ================================================

-- Insert Users
INSERT INTO users (email, password) VALUES
('ali@gmail.com', 'password1'),
('sara@gmail.com', 'password2'),
('hassan@gmail.com', 'password3');

-- Insert Customers linked to users
INSERT INTO Customer (Name, CNIC, Contact, UserID) VALUES
('Ali Ahmed', '42101-1234567-1', '0300-1234567', 1),
('Sara Khan', '42101-7654321-2', '0321-7654321', 2),
('Hassan Ali', '42201-9876543-3', '0333-9876543', 3);

-- Insert Accounts with Email
INSERT INTO Account (CustomerID, Email, Type, Balance) VALUES
(1, 'ali@gmail.com', 'Savings', 50000.00),
(2, 'sara@gmail.com', 'Current', 75000.00),
(3, 'hassan@gmail.com', 'Savings', 100000.00);

-- Sample Transactions
INSERT INTO TransactionLog (FromAccount, ToAccount, Amount, Type) VALUES
(1, NULL, 10000.00, 'Deposit'),
(2, 3, 5000.00, 'Transfer');

-- Sample Audit Logs
INSERT INTO AuditLog (Operation, TableAffected, UserName) VALUES
('INSERT', 'Customer', 'Admin'),
('INSERT', 'Account', 'Admin');
