SHOW DATABASES;

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


-- SELECT username, `password`, CONCAT(f_name, " ", l_name) from usr_info;
SELECT username, `password`, CONCAT(f_name, " ", l_name) as names FROM airport_staff_management.usr_info;

CREATE TABLE test(
    hashed_pass VARCHAR(100) PRIMARY KEY
);


-- DELIMITER $$
-- CREATE FUNCTION InsertPassword(
--     new_string VARCHAR(255) -- Change the data type and length as needed
-- )
-- RETURNS INT
-- READS SQL DATA
-- DETERMINISTIC
-- BEGIN
--     DECLARE new_id INT;
    
--     -- Insert the new string into the table
--     INSERT INTO  test(hashed_pass) VALUES (new_string);

--     -- Get the last inserted ID (assuming the table has an auto-increment primary key)
--     SET new_id = LAST_INSERT_ID();

--     RETURN new_id;
-- END $$
-- DELIMITER ;


-- SHOW FUNCTION STATUS where db='airport_staff_management';

-- SELECT InsertPassword('pass123');

SELECT * FROM usr_info;


-- DROP FUNCTION InsertPassword;

DROP TABLE usr_info;