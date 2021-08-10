-- Start MySQL server

-- Create database
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

-- Create User
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges to user
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';

-- Grant select privileges to user
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;
