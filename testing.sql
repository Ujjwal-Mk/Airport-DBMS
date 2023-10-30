-- Active: 1696681355003@@127.0.0.1@3306@airport_staff_management

-- DROP DATABASE IF EXISTS testing;
DROP DATABASE IF EXISTS airport_staff_management;

USE airport_staff_management;

DROP DATABASE IF EXISTS airport_staff_management;

CREATE DATABASE airport_staff_management;

USE airport_staff_management;

CREATE TABLE usr_info(
    usrid INT AUTO_INCREMENT PRIMARY KEY,
    f_name VARCHAR(25),
    minit VARCHAR(5),
    l_name VARCHAR(25),
    username VARCHAR(25) UNIQUE,
    hashed_pass VARCHAR(255),
    auth_level ENUM('0','1','2') DEFAULT '2',
    CONSTRAINT uname_pass UNIQUE (username,hashed_pass)
);

CREATE TABLE usr_info1(
    usrid INT AUTO_INCREMENT PRIMARY KEY,
    f_name VARCHAR(25),
    minit VARCHAR(5),
    l_name VARCHAR(25),
    username VARCHAR(25) UNIQUE,
    hashed_pass VARCHAR(255),
    auth_level ENUM('0','1','2') DEFAULT '2',
    CONSTRAINT uname_pass UNIQUE (username,hashed_pass)
);

INSERT INTO usr_info1(f_name, l_name, minit, username, hashed_pass, auth_level) VALUES
('John', 'Doe', 'A', 'johndoe1', 'pass123', '1'),
('Alice', 'Smith', 'B', 'alice.smith', 'abc456', '2'),
('Bob', 'Johnson', 'C', 'bobj', 'bob789', '0'),
('Emily', 'Davis', 'D', 'emily_d', 'emily123', '1'),
('Michael', 'Wilson', 'E', 'mike.w', 'mike456', '2'),
('Sarah', 'Brown', 'F', 'sarah_b', 'sarah789', '1'),
('David', 'Lee', 'G', 'davidl', 'david123', '2'),
('Laura', 'Clark', 'H', 'laura.c', 'laura456', '1'),
('James', 'Anderson', 'I', 'james123', 'pass789', '0'),
('Sophia', 'Martinez', 'J', 'sophiam', 'sophia123', '2');


-- Create the tables

-- Create the Airlines table
CREATE TABLE Airlines (
  airline_id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (airline_id)
);

-- Create the Airplanes table
CREATE TABLE Airplanes (
  airplane_id INT NOT NULL AUTO_INCREMENT,
  type VARCHAR(255) NOT NULL,
  airline_id INT NOT NULL,
  PRIMARY KEY (airplane_id),
  FOREIGN KEY (airline_id) REFERENCES Airlines (airline_id)
);

-- Create the Services table
CREATE TABLE Services (
  service_id INT NOT NULL AUTO_INCREMENT,
  type VARCHAR(255) NOT NULL,
  airplane_id INT NOT NULL,
  provider_name VARCHAR(255) NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  capacity INT NOT NULL,
  availability VARCHAR(255) NOT NULL,
  PRIMARY KEY (service_id),
  FOREIGN KEY (airplane_id) REFERENCES Airplanes (airplane_id)
);

-- Create the Gateways table
CREATE TABLE Gateways (
  gateway_id INT NOT NULL AUTO_INCREMENT,
  gate VARCHAR(255) NOT NULL,
  hangar_bay VARCHAR(255) NOT NULL,
  capacity INT NOT NULL,
  PRIMARY KEY (gateway_id)
);

-- Create the Fueling centers table
CREATE TABLE FuelingCenters (
  fueling_center_id INT NOT NULL AUTO_INCREMENT,
  type VARCHAR(255) NOT NULL,
  capacity INT NOT NULL,
  PRIMARY KEY (fueling_center_id)
);

-- Create the De-icing methods table
CREATE TABLE DeIcingMethods (
  de_icing_method_id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (de_icing_method_id)
);

-- Create the Service mappings table
CREATE TABLE ServiceDeIcingMethodMappings (
  service_id INT NOT NULL,
  de_icing_method_id INT NOT NULL,
  PRIMARY KEY (service_id, de_icing_method_id),
  FOREIGN KEY (service_id) REFERENCES Services (service_id),
  FOREIGN KEY (de_icing_method_id) REFERENCES DeIcingMethods (de_icing_method_id)
);

-- Insert data into the Airlines table
INSERT INTO Airlines (name) VALUES
('Delta Air Lines'),
('American Airlines'),
('United Airlines'),
('Southwest Airlines'),
('Spirit Airlines');

-- Insert data into the Airplanes table
INSERT INTO Airplanes (type, airline_id) VALUES
('Boeing 737-800', 1),
('Boeing 737-900', 1),
('Airbus A320-200', 2),
('Airbus A321-200', 2),
('Boeing 777-200', 3),
('Airbus A380-800', 3);

-- Insert data into the Services table
INSERT INTO Services (type, airplane_id, provider_name, price, capacity, availability) VALUES
('Catering', 1, 'Gate Gourmet', 100, 100, 'Available'),
('Cleaning', 2, 'Servisair', 50, 50, 'Available'),
('De-icing', 1, 'Global Ground Services', 200, 50, 'Available'),
('Fueling', 3, 'World Fuel Services', 500, 50, 'Available'),
('Gate handling', 4, 'Swissport', 100, 50, 'Available');

-- Insert data into the Gateways table
INSERT INTO Gateways (gate, hangar_bay, capacity) VALUES
('A1', 'H1', 10),
('A2', 'H2', 10),
('B1', 'H3', 10),
('B2', 'H4', 10),
('C1', 'H5', 10);

-- Insert data into the Fueling centers table
INSERT INTO FuelingCenters (type, capacity) VALUES
('Jet fuel', 1000000),
('Avgas', 100000);

-- Insert data into the De-icing methods table
INSERT INTO DeIcingMethods (name) VALUES
('Glycol-based de-icing fluids'),
('Pneumatic de-icing'),
('Electrothermal de-icing');

-- Insert data into the Service mappings table
INSERT INTO ServiceDeIcingMethodMappings (service_id, de_icing_method_id) VALUES
(1, 1),
(2, 1),
(3, 1);

INSERT INTO Airplanes (type, airline_id) VALUES
('Boeing 737-MAX 8', 1),
('Airbus A320neo', 2),
('Boeing 787-9 Dreamliner', 3),
('Airbus A350-900', 3),
('Boeing 747-8 Intercontinental', 1),
('Airbus A380-800', 2);

INSERT INTO Services (type, airplane_id, provider_name, price, capacity, availability) VALUES
('Catering', 7, 'Gate Gourmet', 100, 100, 'Available'),
('Cleaning', 8, 'Servisair', 50, 50, 'Available'),
('De-icing', 7, 'Global Ground Services', 200, 50, 'Available'),
('Fueling', 9, 'World Fuel Services', 500, 50, 'Available'),
('Gate handling', 10, 'Swissport', 100, 50, 'Available');

-- SELECT `airplane_id`,`type` FROM `Airplanes`
-- WHERE airline_id=1;

-- USE airport_staff_management;
-- SELECT airplane_id, `type` FROM `Airplanes` WHERE airline_id=1;