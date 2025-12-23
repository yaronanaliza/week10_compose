CREATE DATABASE DB_CONTACTS

CREATE TABLE Contacts (
    ContactID int NOT NULL AUTO_INCREMENT,
    FirstName varchar(255),
    LastName varchar(255),
    PhoneNumber varchar(11),
);

INSERT INTO Contacts (FirstName, LastName, PhoneNumber) VALUES
    ('John', 'Doe', '050-1234567'),
    ('Jane', 'Smith', '052-9876543'),
    ('Bob', 'Johnson', '054-5555555'),
    ('Jack', 'Robinson', '050-6115555');