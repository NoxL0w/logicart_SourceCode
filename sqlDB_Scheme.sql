CREATE DATABASE IF NOT EXISTS logicart;
USE logicart;

CREATE TABLE IF NOT EXISTS user\_registration (
UserID VARCHAR(12) PRIMARY KEY,
Username VARCHAR(50),
Password VARCHAR(255),
AccountType ENUM('Business', 'Individual', 'Hybrid'),
Email VARCHAR(100),
ContactNum VARCHAR(20),
TelephoneNum VARCHAR(20),
FirstName VARCHAR(50),
LastName VARCHAR(50),
CompanyName VARCHAR(100),
Owner VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS user\_data (
UserID VARCHAR(12),
Cart JSON,
ChosenPaymentOption VARCHAR(50),
SavedAddresses TEXT,
FOREIGN KEY (UserID) REFERENCES user\_registration(UserID)
);

CREATE TABLE IF NOT EXISTS product (
ItemID INT AUTO\_INCREMENT PRIMARY KEY,
Name VARCHAR(100),
Price DECIMAL(10,2),
Specs TEXT,
Rating DECIMAL(3,2)
);

CREATE TABLE IF NOT EXISTS orders (
OrderID INT AUTO\_INCREMENT PRIMARY KEY,
UserID VARCHAR(12),
OrderDate DATETIME,
ItemID INT,
Quantity INT,
FOREIGN KEY (UserID) REFERENCES user\_registration(UserID),
FOREIGN KEY (ItemID) REFERENCES product(ItemID)
);