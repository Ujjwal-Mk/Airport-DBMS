DROP DATABASE IF EXISTS airport;

CREATE DATABASE airport;

USE airport;


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


-- Airlines table
CREATE TABLE Airlines (
  AirlineID INT NOT NULL AUTO_INCREMENT,
  AirlineName VARCHAR(255) NOT NULL,
  AirlineCode VARCHAR(3) NOT NULL,
  PRIMARY KEY (AirlineID)
);

-- Airplanes table
-- CREATE TABLE Airplanes (
--   AirplaneID INT NOT NULL AUTO_INCREMENT,
--   AirplaneType VARCHAR(255) NOT NULL,
--   AirplaneRegistration VARCHAR(100) NOT NULL,
--   PRIMARY KEY (AirplaneID)
-- );

CREATE TABLE Airplanes (
  AirplaneID INT NOT NULL AUTO_INCREMENT,
  AirplaneType VARCHAR(255) NOT NULL,
  AirplaneRegistration VARCHAR(100) NOT NULL,
  AirlineID INT NOT NULL,
  PRIMARY KEY (AirplaneID),
  FOREIGN KEY (AirlineID) REFERENCES Airlines(AirlineID)
);

-- DeIcingMethods table
CREATE TABLE DeIcingMethods (
  DeIcingMethodID INT NOT NULL AUTO_INCREMENT,
  DeIcingMethodName VARCHAR(255) NOT NULL,
  PRIMARY KEY (DeIcingMethodID)
);

-- FuelingCenters table
CREATE TABLE FuelingCenters (
  FuelingCenterID INT NOT NULL AUTO_INCREMENT,
  FuelingCenterName VARCHAR(255) NOT NULL,
  FuelingCenterLocation VARCHAR(255) NOT NULL,
  PRIMARY KEY (FuelingCenterID)
);

-- Gateways table
CREATE TABLE Gateways (
  GatewayID INT NOT NULL AUTO_INCREMENT,
  GatewayName VARCHAR(255) NOT NULL,
  GatewayLocation VARCHAR(255) NOT NULL,
  PRIMARY KEY (GatewayID)
);
-- Services table
CREATE TABLE Services (
  ServiceID INT NOT NULL AUTO_INCREMENT,
  ServiceName VARCHAR(255) NOT NULL,
  PRIMARY KEY (ServiceID)
);

-- ServiceDeIcingMethodMappings table
CREATE TABLE ServiceDeIcingMethodMappings (
  ServiceID INT NOT NULL,
  DeIcingMethodID INT NOT NULL,
  PRIMARY KEY (ServiceID, DeIcingMethodID),
  FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID),
  FOREIGN KEY (DeIcingMethodID) REFERENCES DeIcingMethods(DeIcingMethodID)
);


-- Resource Inventory table
CREATE TABLE ResourceInventory (
  ResourceID INT NOT NULL AUTO_INCREMENT,
  ResourceType VARCHAR(255) NOT NULL,
  ResourceName VARCHAR(255) NOT NULL,
  Quantity INT NOT NULL,
  Location VARCHAR(255) NOT NULL,
  Status VARCHAR(255) NOT NULL,
  LastUpdated DATETIME NOT NULL,
  ServiceID INT NOT NULL,
  FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID),
  PRIMARY KEY (ResourceID)
);

-- Resource Request table
CREATE TABLE ResourceRequests (
  RequestID INT NOT NULL AUTO_INCREMENT,
  ResourceID INT NOT NULL,
  Quantity INT NOT NULL,
  RequestedBy VARCHAR(255) NOT NULL,
  RequestDate DATETIME NOT NULL,
  Status VARCHAR(255) NOT NULL,
  ServiceID INT NOT NULL,
  FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID),
  PRIMARY KEY (RequestID),
  FOREIGN KEY (ResourceID) REFERENCES ResourceInventory(ResourceID)
);

-- Maintenance Schedule table
CREATE TABLE MaintenanceSchedule (
  ScheduleID INT NOT NULL AUTO_INCREMENT,
  AirplaneID INT NOT NULL,
  MaintenanceType VARCHAR(255) NOT NULL,
  ScheduledDate DATETIME NOT NULL,
  Status VARCHAR(255) NOT NULL,
  ServiceID INT NOT NULL,
  FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID),
  PRIMARY KEY (ScheduleID),
  FOREIGN KEY (AirplaneID) REFERENCES Airplanes(AirplaneID)
);

-- Maintenance Request table
CREATE TABLE MaintenanceRequests (
  RequestID INT NOT NULL AUTO_INCREMENT,
  AirplaneID INT NOT NULL,
  MaintenanceType VARCHAR(255) NOT NULL,
  RequestedBy VARCHAR(255) NOT NULL,
  RequestDate DATETIME NOT NULL,
  Status VARCHAR(255) NOT NULL,
  ServiceID INT NOT NULL,
  FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID),
  PRIMARY KEY (RequestID),
  FOREIGN KEY (AirplaneID) REFERENCES Airplanes(AirplaneID)
);

-- Gate Allocation table
CREATE TABLE GateAllocation (
  GateID INT NOT NULL,
  AirplaneID INT NOT NULL,
  AirlineID INT NOT NULL,
  FlightNumber VARCHAR(10) NOT NULL,
  ArrivalDate DATETIME NOT NULL,
  DepartureDate DATETIME NOT NULL,
  ServiceID INT NOT NULL,
  FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID),
  PRIMARY KEY (GateID, AirplaneID)
);


-- Ground Handling Request table
CREATE TABLE GroundHandlingRequests (
RequestID INT NOT NULL AUTO_INCREMENT,
AirplaneID INT NOT NULL,
GroundHandlingService VARCHAR(255) NOT NULL,
RequestedBy VARCHAR(255) NOT NULL,
RequestDate DATETIME NOT NULL,
Status VARCHAR(255) NOT NULL,
ServiceID INT NOT NULL,
FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID),
PRIMARY KEY (RequestID),
FOREIGN KEY (AirplaneID) REFERENCES Airplanes(AirplaneID)
);

-- De-icing Request table
CREATE TABLE DeIcingRequests (
RequestID INT NOT NULL AUTO_INCREMENT,
AirplaneID INT NOT NULL,
DeIcingMethod VARCHAR(255) NOT NULL,
RequestedBy VARCHAR(255) NOT NULL,
RequestDate DATETIME NOT NULL,
Status VARCHAR(255) NOT NULL,
ServiceID INT NOT NULL,
FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID),
PRIMARY KEY (RequestID),
FOREIGN KEY (AirplaneID) REFERENCES Airplanes(AirplaneID)
);

-- Incident Report table
CREATE TABLE IncidentReport (
IncidentID INT NOT NULL AUTO_INCREMENT,
IncidentType VARCHAR(255) NOT NULL,
IncidentDate DATETIME NOT NULL,
IncidentLocation VARCHAR(255) NOT NULL,
IncidentDescription VARCHAR(255) NOT NULL,
ReportedBy VARCHAR(255) NOT NULL,
ServiceID INT NOT NULL,
FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID),
PRIMARY KEY (IncidentID)
);

-- Communication Log table
CREATE TABLE CommunicationLog (
MessageID INT NOT NULL AUTO_INCREMENT,
SenderID INT NOT NULL,
RecipientID INT NOT NULL,
MessageType VARCHAR(255) NOT NULL,
MessageSubject VARCHAR(255) NOT NULL,
MessageBody VARCHAR(255) NOT NULL,
SentDate DATETIME NOT NULL,
-- FOREIGN KEY (SenderID) REFERENCES Users(UserID),
-- FOREIGN KEY (RecipientID) REFERENCES Users(UserID),
PRIMARY KEY (MessageID)
);

-- Airlines table
INSERT INTO Airlines (AirlineName, AirlineCode) VALUES
('Delta Airlines', 'DL'),
('American Airlines', 'AA'),
('United Airlines', 'UA'),
('Lufthansa', 'LH'),
('Emirates', 'EK');

-- Airplanes table
-- Insert data into the new Airplanes table with AirlineID
INSERT INTO Airplanes (AirplaneType, AirplaneRegistration, AirlineID) VALUES
('Boeing 737-800', 'N123DA', 1),
('Airbus A320', 'N456AA', 2),
('Boeing 777-200', 'N789UA', 3),
('Airbus A380', 'N456LH', 4),
('Boeing 747-400', 'N789EK', 5),
('Airbus A330', 'N321DL', 1),
('Boeing 787-9', 'N789AA', 2),
('Airbus A321', 'N456UA', 3),
('Boeing 747-8', 'N101LH', 4),
('Embraer E190', 'N456EK', 5),
('Boeing 737-700', 'N234DL', 1),
('Airbus A350', 'N654AA', 2),
('Boeing 767-300', 'N222UA', 3),
('Airbus A319', 'N987LH', 4),
('Embraer E175', 'N987EK', 5);

-- DeIcingMethods table
INSERT INTO DeIcingMethods (DeIcingMethodName) VALUES
('Type I De-Icing'),
('Type II De-Icing'),
('Type III De-Icing');

-- FuelingCenters table
INSERT INTO FuelingCenters (FuelingCenterName, FuelingCenterLocation) VALUES
('Fuel Center A', 'Terminal A'),
('Fuel Center B', 'Terminal B'),
('Fuel Center C', 'Terminal C'),
('Fuel Center D', 'Terminal D'),
('Fuel Center E', 'Terminal E');

-- Gateways table
INSERT INTO Gateways (GatewayName, GatewayLocation) VALUES
('Gate A1', 'Terminal A'),
('Gate B2', 'Terminal B'),
('Gate C3', 'Terminal C'),
('Gate D4', 'Terminal D'),
('Gate E5', 'Terminal E');



-- Services table
INSERT INTO Services (ServiceName) VALUES
('Fueling Service'),
('Aircraft Parking Gates'),
('Air Traffic Control'),
('Ground Handling Service'),
('Aircraft De-icing'),
('Emergency Services'),
('Catering Service'),
('Fueling Centre');

-- ServiceDeIcingMethodMappings table
INSERT INTO ServiceDeIcingMethodMappings (ServiceID, DeIcingMethodID) VALUES
(5, 1),
(5, 2),
(5, 3);

-- Resource Inventory table
INSERT INTO ResourceInventory (ResourceType, ResourceName, Quantity, Location, Status, LastUpdated, ServiceID) VALUES
('Jet Fuel', 'Jet A1', 100000, 'Fuel Center A', 'In Service', '2023-11-01 08:00:00', 1),
('De-Icing Fluid', 'Type I De-Icer', 50, 'Hangar X', 'In Service', '2023-11-01 10:00:00', 5),
('Food Supplies', 'Meal Cartons', 10000, 'Catering Warehouse', 'In Service', '2023-11-02 09:30:00', 7);

-- Resource Request table
INSERT INTO ResourceRequests (ResourceID, Quantity, RequestedBy, RequestDate, Status, ServiceID) VALUES
(1, 50000, 'Delta Airlines', '2023-11-02 14:15:00', 'Approved', 1),
(2, 20, 'American Airlines', '2023-11-03 10:30:00', 'Pending', 5),
(3, 2000, 'United Airlines', '2023-11-02 16:45:00', 'Pending', 7);

-- Maintenance Schedule table
INSERT INTO MaintenanceSchedule (AirplaneID, MaintenanceType, ScheduledDate, Status, ServiceID) VALUES
(1, 'Routine Inspection', '2023-11-05 08:00:00', 'Scheduled', 3),
(2, 'Repair', '2023-11-07 14:30:00', 'Scheduled', 3);

-- Maintenance Request table
INSERT INTO MaintenanceRequests (AirplaneID, MaintenanceType, RequestedBy, RequestDate, Status, ServiceID) VALUES
(3, 'Routine Inspection', 'United Airlines', '2023-11-08 09:00:00', 'Pending', 3),
(1, 'Repair', 'Delta Airlines', '2023-11-08 11:45:00', 'Pending', 3);

-- Gate Allocation table
INSERT INTO GateAllocation (GateID, AirplaneID, AirlineID, FlightNumber, ArrivalDate, DepartureDate, ServiceID) VALUES
(1, 1, 1, 'DL123', '2023-11-05 09:30:00', '2023-11-05 13:45:00', 2),
(2, 2, 2, 'AA456', '2023-11-06 10:15:00', '2023-11-06 14:30:00', 2);

-- Ground Handling Request table
INSERT INTO GroundHandlingRequests (AirplaneID, GroundHandlingService, RequestedBy, RequestDate, Status, ServiceID) VALUES
(1, 'Baggage Handling', 'Delta Airlines', '2023-11-05 09:00:00', 'Approved', 4),
(2, 'Towing', 'American Airlines', '2023-11-06 10:30:00', 'Pending', 4);

-- De-icing Request table
INSERT INTO DeIcingRequests (AirplaneID, DeIcingMethod, RequestedBy, RequestDate, Status, ServiceID) VALUES
(1, 'Type II De-Icing', 'Delta Airlines', '2023-11-05 11:15:00', 'Approved', 5),
(2, 'Type I De-Icing', 'American Airlines', '2023-11-06 12:30:00', 'Pending', 5);

-- Incident Report table
INSERT INTO IncidentReport (IncidentType, IncidentDate, IncidentLocation, IncidentDescription, ReportedBy, ServiceID) VALUES
('Safety Incident', '2023-11-04 14:45:00', 'Gate A1', 'Minor safety issue', 'Delta Airlines', 6),
('Accident', '2023-11-07 10:30:00', 'Runway C', 'Aircraft collision', 'American Airlines', 6);

-- Communication Log table
INSERT INTO CommunicationLog (SenderID, RecipientID, MessageType, MessageSubject, MessageBody, SentDate) VALUES
(1, 2, 'Notification', 'Gate Change', 'Gate A1 changed to Gate B2', '2023-11-05 09:15:00'),
(3, 1, 'Emergency', 'Safety Alert', 'Emergency on Runway C, please divert flights', '2023-11-07 10:32:00');



-- SELECT
--     AirlineName,
--     AirplaneType,
--     ScheduledDate AS FlightDate,
--     Status AS FlightStatus
-- FROM Airlines
-- JOIN Airplanes ON Airlines.AirlineID = Airplanes.AirplaneID
-- JOIN GateAllocation ON Airplanes.AirplaneID = GateAllocation.AirplaneID
-- JOIN Services ON GateAllocation.ServiceID = Services.ServiceID
-- JOIN MaintenanceSchedule ON Airplanes.AirplaneID = MaintenanceSchedule.AirplaneID
-- WHERE Airlines.AirlineName = 'Delta Airlines';


-- -- Report a safety incident
-- INSERT INTO IncidentReport (IncidentType, IncidentDate, IncidentLocation, IncidentDescription, ReportedBy, ServiceID)
-- VALUES ('Safety Incident', '2023-11-09 13:30:00', 'Gate C3', 'Minor safety issue', 'Delta Airlines', 6);


-- SELECT * FROM `Airlines`;

CREATE TABLE MonthlyAirplaneCount (
  MonthlyCountID INT NOT NULL AUTO_INCREMENT,
  AirlineID INT NOT NULL,
  Year INT NOT NULL,
  Month INT NOT NULL,
  AirplaneCount INT NOT NULL,
  PRIMARY KEY (MonthlyCountID),
  FOREIGN KEY (AirlineID) REFERENCES Airlines(AirlineID)
);



-- Delta Airlines (DL) Monthly Airplane Counts for 2023
INSERT INTO MonthlyAirplaneCount (AirlineID, Year, Month, AirplaneCount)
VALUES
  (1, 2023, 6, 52),
  (1, 2023, 7, 54),
  (1, 2023, 8, 53),
  (1, 2023, 9, 56),
  (1, 2023, 10, 58),
  (1, 2023, 11, 57),
  (1, 2023, 12, 60);

-- American Airlines (AA) Monthly Airplane Counts for 2023
INSERT INTO MonthlyAirplaneCount (AirlineID, Year, Month, AirplaneCount)
VALUES
  (2, 2023, 6, 60),
  (2, 2023, 7, 62),
  (2, 2023, 8, 63),
  (2, 2023, 9, 65),
  (2, 2023, 10, 68),
  (2, 2023, 11, 67),
  (2, 2023, 12, 70);

-- United Airlines (UA) Monthly Airplane Counts for 2023
INSERT INTO MonthlyAirplaneCount (AirlineID, Year, Month, AirplaneCount)
VALUES
  (3, 2023, 6, 48),
  (3, 2023, 7, 50),
  (3, 2023, 8, 52),
  (3, 2023, 9, 53),
  (3, 2023, 10, 55),
  (3, 2023, 11, 57),
  (3, 2023, 12, 58);


-- Lufthansa (LH) Monthly Airplane Counts for 2023
INSERT INTO MonthlyAirplaneCount (AirlineID, Year, Month, AirplaneCount)
VALUES
  (4, 2023, 6, 40),
  (4, 2023, 7, 42),
  (4, 2023, 8, 44),
  (4, 2023, 9, 45),
  (4, 2023, 10, 48),
  (4, 2023, 11, 50),
  (4, 2023, 12, 52);

-- Emirates (EK) Monthly Airplane Counts for 2023
INSERT INTO MonthlyAirplaneCount (AirlineID, Year, Month, AirplaneCount)
VALUES
  (5, 2023, 6, 55),
  (5, 2023, 7, 57),
  (5, 2023, 8, 59),
  (5, 2023, 9, 60),
  (5, 2023, 10, 62),
  (5, 2023, 11, 64),
  (5, 2023, 12, 66);