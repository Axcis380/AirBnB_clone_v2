-- Create the development database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the development user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privileges on the development database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on the performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Apply privilege changes
FLUSH PRIVILEGES;
