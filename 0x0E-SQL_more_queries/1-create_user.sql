-- create MySQL server user 'user_0d_1'
-- grant all privileges on MySQL server
-- if user exists script should not fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' 
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
