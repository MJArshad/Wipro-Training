CREATE TABLE Customers(
CustomerId Int PRIMARY KEY,
CustomerName VARCHAR(50),
City VARCHAR (50)
);
INSERT INTO Customers VALUES
(1, 'Amit','Hyderabad'),
(2, 'Neha','Bangalore'),
(3, 'Rahul','Delhi'),
(4, 'Priya','Mumbai');

SELECT * FROM Customers;

INSERT INTO Customers (CustomerId,CustomerName,City)
VALUES (5,'Suresh','Chennai');

UPDATE Customers
SET City = 'pune'
WHERE CustomerName ='Priya';

DELETE FROM Customers
WHERE CustomerName = 'Rahul';

SELECT * FROM Customers
WHERE City = 'Bangalore';