DROP DATABASE IF EXISTS testing;

CREATE DATABASE testing;

USE testing;

-- Create the tables

-- Airlines table
CREATE TABLE airlines (
  airline_id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (airline_id)
);

-- Airplanes table
CREATE TABLE airplanes (
  airplane_id INT NOT NULL AUTO_INCREMENT,
  type VARCHAR(255) NOT NULL,
  airline_id INT NOT NULL,
  PRIMARY KEY (airplane_id),
  FOREIGN KEY (airline_id) REFERENCES airlines(airline_id)
);

-- Services table
CREATE TABLE services (
  service_id INT NOT NULL AUTO_INCREMENT,
  type VARCHAR(255) NOT NULL,
  airplane_id INT NOT NULL,
  provider_name VARCHAR(255) NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  capacity INT NOT NULL,
  availability VARCHAR(255) NOT NULL,
  PRIMARY KEY (service_id),
  FOREIGN KEY (airplane_id) REFERENCES airplanes(airplane_id)
);
-- Gateways table
CREATE TABLE gateways (
  gateway_id INT NOT NULL AUTO_INCREMENT,
  location_id INT NOT NULL,
  gate VARCHAR(255) NOT NULL,
  hangar_bay VARCHAR(255) NOT NULL,
  capacity INT NOT NULL,
  PRIMARY KEY (gateway_id),
  FOREIGN KEY (gateway_id) REFERENCES airplanes(airplane_id)
);

-- Fueling centers table
CREATE TABLE fueling_centers (
  fueling_center_id INT NOT NULL AUTO_INCREMENT,
  location_id INT NOT NULL,
  type VARCHAR(255) NOT NULL,
  capacity INT NOT NULL,
  PRIMARY KEY (fueling_center_id)
);

-- De-icing methods table
CREATE TABLE de_icing_methods (
  de_icing_method_id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (de_icing_method_id)
);

-- Service mappings table
-- This table maps services to de-icing methods
CREATE TABLE service_de_icing_method_mappings (
  service_id INT NOT NULL,
  de_icing_method_id INT NOT NULL,
  PRIMARY KEY (service_id, de_icing_method_id),
  FOREIGN KEY (service_id) REFERENCES services(service_id),
  FOREIGN KEY (de_icing_method_id) REFERENCES de_icing_methods(de_icing_method_id)
);

-- Airlines table
INSERT INTO airlines (name) VALUES
('Delta Air Lines'),
('American Airlines'),
('United Airlines'),
('Southwest Airlines'),
('Spirit Airlines');

-- Airplanes table
INSERT INTO airplanes (type, airline_id) VALUES
('Boeing 737-800', 1),
('Boeing 737-900', 1),
('Airbus A320-200', 2),
('Airbus A321-200', 2),
('Boeing 777-200', 3);

-- Services table
INSERT INTO services (type, airplane_id, provider_name, price, capacity, availability) VALUES
('Catering', 1, 'Gate Gourmet', 100, 100, 'Available'),
('Cleaning', 2, 'Servisair', 50, 50, 'Available'),
('De-icing', 1, 'Global Ground Services', 200, 50, 'Available'),
('Fueling', 3, 'World Fuel Services', 500, 50, 'Available'),
('Gate handling', 4, 'Swissport', 100, 50, 'Available');

-- Gateways table
INSERT INTO gateways (gateway_id, gate, hangar_bay, capacity) VALUES
(1, 'A1', 'H1', 10),
(2, 'A2', 'H2', 10),
(3, 'B1', 'H3', 10),
(4, 'B2', 'H4', 10),
(5, 'C1', 'H5', 10);

-- Fueling centers table
INSERT INTO fueling_centers (type, capacity) VALUES
('Jet fuel', 1000000),
('Avgas', 100000);

-- De-icing methods table
INSERT INTO de_icing_methods (name) VALUES
('Glycol-based de-icing fluids'),
('Pneumatic de-icing'),
('Electrothermal de-icing');

-- Service mappings table
INSERT INTO service_de_icing_method_mappings (service_id, de_icing_method_id) VALUES
(1, 1),
(2, 1),
(3, 1);

-- SHOW TABLES;