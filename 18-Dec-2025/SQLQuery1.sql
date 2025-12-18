CREATE TABLE Students (
StudentId INT IDENTITY(1,1) PRIMARY KEY,
FirstName VARCHAR(50),
LastName VARCHAR(50),
Email VARCHAR(100),
DateOfBirth DATE
);
select * from Students