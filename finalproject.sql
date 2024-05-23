DROP DATABASE IF EXISTS restaurant_reservations;

CREATE DATABASE restaurant_reservations;

USE restaurant_reservations;

CREATE TABLE Customers (
    customerId INT NOT NULL AUTO_INCREMENT,
    customerName VARCHAR(45) NOT NULL,
    contactInfo VARCHAR(200),
    PRIMARY KEY (customerId)
);

CREATE TABLE Reservations (
    reservationId INT NOT NULL AUTO_INCREMENT,
    customerId INT NOT NULL,
    reservationTime DATETIME NOT NULL,
    numberOfGuests INT NOT NULL,
    specialRequests VARCHAR(200),
    PRIMARY KEY (reservationId),
    FOREIGN KEY (customerId) REFERENCES Customers(customerId)
);

CREATE TABLE DiningPreferences (
    preferenceId INT NOT NULL AUTO_INCREMENT,
    customerId INT NOT NULL,
    favoriteTable VARCHAR(45),
    dietaryRestrictions VARCHAR(200),
    PRIMARY KEY (preferenceId),
    FOREIGN KEY (customerId) REFERENCES Customers(customerId)
);

INSERT INTO Customers (customerName, contactInfo)
VALUES
    ('Customer 1', 'customer1@example.com'),
    ('Customer 2', '123-456-7890'),
    ('Customer 3', 'customer3@example.com');

INSERT INTO Reservations (customerId, reservationTime, numberOfGuests, specialRequests)
VALUES
    (1, '2024-05-20 18:00:00', 2, 'Window seat'),
    (2, '2024-05-21 19:30:00', 4, 'Birthday celebration'),
    (3, '2024-05-22 20:00:00', 2, NULL);

INSERT INTO DiningPreferences (customerId, favoriteTable, dietaryRestrictions)
VALUES
    (1, 'Table 5', 'Vegetarian'),
    (2, NULL, 'Nut allergy'),
    (3, 'Booth 2', NULL);