use switz_bank;
-- show tables;
CREATE TABLE authen (sno int,atm_no VARCHAR(40),pass VARCHAR(10));
INSERT INTO authen (sno,atm_no, pass) VALUES(1,'1234567456', 'pswd123');
select * from authen;