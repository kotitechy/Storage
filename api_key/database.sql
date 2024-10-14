CREATE DATABASE chatbot_ai;
USE chatbot_ai;

CREATE TABLE users (
    sno INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) UNIQUE,
    email VARCHAR(255) UNIQUE
);

CREATE TABLE queries (
    sno INT primary key AUTO_INCREMENT,
    username VARCHAR(255),
    query TEXT,
    inserted TIMESTAMP  DEFAULT  CURRENT_TIMESTAMP);
insert into users (username,email) values("shiva","ksc11197@gmail.com");
insert into queries (query,username) values ("what is sqrt of 6","shiva");

select * from queries;
drop table queries;