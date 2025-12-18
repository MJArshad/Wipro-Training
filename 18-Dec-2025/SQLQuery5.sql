CREATE TABLE Departments (
DepartmentId INT IDENTITY(1,1) PRIMARY KEY,
DepartmentName VARCHAR(100) NOT NULL
);
INSERT INTO Departments (DepartmentName)
VALUES ('Computer Science'),('Mechanical'),('Electrical');

INSERT INTO Departments (DepartmentName)
VALUES (NULL);