-- creates database 'hbtn_0d_usa' and table 'cities' in hbtn_0d_usa on mysql
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities 
(id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT, state_id INT NOT NULL, 
name VARCHAR(256) NOT NULL, FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.state_id);
