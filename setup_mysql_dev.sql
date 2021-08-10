-- Start MySQL server

-- Creating databe
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;

-- Creating user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Granting privileges to user
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';

-- Grant select privileges to user
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;
