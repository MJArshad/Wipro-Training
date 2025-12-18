CREATE TABLE Product(
ProductId INT PRIMARY KEY,
Name VARCHAR(100),
Brand VARCHAR(50),
ManufactureDate DATE,
ExpiryDate DATE,
Price DECIMAL(10,2)
);
INSERT INTO Product (productId,Name,Brand,ManufactureDate,ExpiryDate,Price)
VALUES(1, 'Laptop', 'HP', '2023-01-01', '2028-01-01', 55000.00),
(2, 'Smartphone', 'Samsung', '2023-05-10', '2026-05-10', 25000.00),
(3, 'Headphones', 'Sony', '2023-03-15', '2025-03-15', 5000.00),
(4, 'Monitor', 'Dell', '2022-12-20', '2027-12-20', 12000.00),
(5, 'Keyboard', 'Logitech', '2023-06-01', '2026-06-01', 1500.00),
(6, 'Mouse', 'Apple', '2023-02-10', '2025-02-10', 8000.00),
(7, 'Tablet', 'Lenovo', '2023-08-12', '2026-08-12', 18000.00),
(8, 'Smartwatch', 'Fossil', '2023-04-22', '2026-04-22', 12000.00),
(9, 'Printer', 'Canon', '2023-01-30', '2027-01-30', 10000.00),
(10, 'Speaker', 'JBL', '2023-07-05', '2025-07-05', 4000.00);
SELECT * From Product;


