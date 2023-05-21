-- create database 'hbtn_0d_2' and user "user_0d_2"
-- user_0d_2 should only have 'select' privilege in the database 'hbtn_0d_2'
-- if the database 'hbtn_0d_2' exists script should not fail
-- if user "user_0d_2" exists script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' 
IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
