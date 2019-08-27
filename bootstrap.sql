use mydb;
create table t_temp(
    reading_id INT AUTO_INCREMENT PRIMARY KEY ,
    temp TEXT,
    reading_data TEXT
);

use mydb;
create table t_humidity(
    reading_id INT AUTO_INCREMENT PRIMARY KEY ,
    humidity TEXT,
    reading_data TEXT
);

use mydb;
create table t_moisture(
    reading_id INT AUTO_INCREMENT PRIMARY KEY ,
    moisture TEXT,
    reading_data TEXT
);