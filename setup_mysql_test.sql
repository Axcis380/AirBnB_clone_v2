-- Create the test database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the test user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges on the test database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on the performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Apply privilege changes
FLUSH PRIVILEGES;
