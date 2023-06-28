CREATE DATABASE Student_Timetable2
GO
USE Student_Timetable2
GO


CREATE TABLE Class(
ID INT IDENTITY (1,1) PRIMARY KEY,
Class_ID VARCHAR (15) UNIQUE,
Class_Name VARCHAR(20)
)
GO

CREATE TABLE Room(
ID INT IDENTITY(1,1) PRIMARY KEY,
Room_Name VARCHAR(20) UNIQUE,
Class_ID VARCHAR(15) NOT NULL,
)
GO

CREATE TABLE Subject(
ID INT IDENTITY(1,1) PRIMARY KEY,
Subject_ID VARCHAR(10) UNIQUE,
Subject_Name NVARCHAR(20),
Lecturer NVARCHAR(30),
Credit INT,
Room_Name VARCHAR(20) NOT NULL,
)
GO


CREATE TABLE Time_Table(
ID INT IDENTITY(1,1) PRIMARY KEY,
Day VARCHAR(20),
Class_ID VARCHAR(15) NOT NULL,
Subject_ID VARCHAR(10) NOT NULL,
Room_Name VARCHAR(20) NOT NULL,
Work_Shift INT,
FOREIGN KEY (Class_ID) REFERENCES Class(Class_ID),
FOREIGN KEY (Subject_ID) REFERENCES Subject(Subject_ID),
FOREIGN KEY (Room_Name) REFERENCES Room(Room_Name)
)
GO


CREATE TABLE Student(
ID INT IDENTITY(1,1) PRIMARY KEY,
Student_ID INT UNIQUE,
Full_Name NVARCHAR(40),
DoB VARCHAR(20),
Class_ID VARCHAR(15) NOT NULL,
FOREIGN KEY(Class_ID) REFERENCES Class(Class_ID)
)
GO


CREATE TABLE Account(
    ID INT IDENTITY(1,1) PRIMARY KEY,
    adminUsername VARCHAR(20),
    adminPass VARCHAR(15)
)
GO

INSERT INTO Class (Class_ID, Class_Name)
VALUES ('IT12', 'DC.IT.12.10'),
('BM12', 'DC.BM.12.10'),
('IT13', 'DC.IT.13.10'),
('BM13', 'DC.BM.13.10');

INSERT INTO Room (Room_Name, Class_ID)
VALUES ('101 DTD', 'IT12'),
('503 DTD', 'BM12'),
('602 PLC', 'IT13'),
('203 EAUT', 'BM13');

INSERT INTO Subject (Subject_ID, Subject_Name, Lecturer, Credit, Room_Name)
VALUES ('OS12', 'Operating System', 'John Smith', 3, '101 DTD'),
('NE13', 'Networking', 'Sarah Johnson', 4, '503 DTD'),
('HBM12', 'Human Resource', 'Michael Lee', 3, '602 PLC'),
('MATBM13', 'Probability', 'David Brown', 4,'203 EAUT');

INSERT INTO Time_Table (Day, Class_ID, Subject_ID, Room_Name, Work_Shift)
VALUES ('20-04-2023', 'IT12', 'OS12', '101 DTD', 3),
('23-05-2023', 'BM12', 'HBM12', '503 DTD', 1),
('22-04-2023', 'BM13', 'MATBM13', '602 PLC', 4),
('24-06-2023', 'IT13', 'NE13', '203 EAUT', 5)


INSERT INTO Student (Student_ID, Full_Name, DoB, Class_ID)
VALUES (20211015, N'Nguyễn Minh Quân', '20-04-2003', 'IT12 '),
(20221052, N'Nguyễn Văn Sơn', '23-01-2004', 'IT13'),
(20211053, N'Nguyễn Phương Lan', '20-03-2003', 'BM12'),
(20222241, N'Nguyễn Thủy ', '03-04-2004', 'BM13')


INSERT INTO Subject (Subject_ID, Subject_Name, Lecturer, Credit, Room_Name)
VALUES ('NT12', 'Networking', 'John Smith', 3, '101 DTD')

INSERT INTO Account (adminUsername, adminPass)
VALUES ('MinhQuan', 'Quan123'), ('MinhNguyen', 'Minh123');




SELECT*FROM Subject
SELECT*FROM Class
SELECT*FROM Room
SELECT Class_ID,Subject_ID from Class,Subject
SELECT*FROM Time_Table
SELECT*FROM Account
SELECT*FROM Student

USE Student_Timetable2
go
SELECT * FROM Student 
WHERE Deleted = 0

ALTER TABLE Student 
ADD Deleted BIT NOT NULL DEFAULT 0;

ALTER TABLE Student 
ADD Time_Delete VARCHAR(50)

UPDATE Student
SET Deleted = 1, Time_Delete = GETDATE()
WHERE ID = 5;


SELECT*FROM Subject

ALTER TABLE Subject 
ADD Deleted BIT NOT NULL DEFAULT 0;
ALTER TABLE Subject 
ADD Time_Delete VARCHAR(50)


ALTER TABLE Time_Table 
ADD Deleted BIT NOT NULL DEFAULT 0;
ALTER TABLE Time_Table 
ADD Time_Delete VARCHAR(50)

ALTER TABLE Time_Table 
ADD Deleted BIT NOT NULL DEFAULT 0;
ALTER TABLE Time_Table 
ADD Time_Delete VARCHAR(50)


ALTER TABLE Room 
ADD Deleted BIT NOT NULL DEFAULT 0;
ALTER TABLE Room 
ADD Time_Delete VARCHAR(50)

