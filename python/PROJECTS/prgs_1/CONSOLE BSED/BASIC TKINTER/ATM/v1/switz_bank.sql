-- create database switz_bank;
use switz_bank;
CREATE TABLE USERS (
    acc_no INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(80) NOT NULL,
    dob DATE NOT NULL,
    gender VARCHAR(10) NOT NULL,
    address VARCHAR(100) NOT NULL,
    qualification VARCHAR(20) NOT NULL,
    mobile_no BIGINT(12) NOT NULL,
    adhar_no VARCHAR(20) NOT NULL,
    email VARCHAR(50) NOT NULL,
    acc_type VARCHAR(7) NOT NULL,
    amount DECIMAL(9,2),
    debit_card_no VARCHAR(16),
    debit_card_pin INT(6),
    prof_img LONGBLOB,
    id_proof LONGBLOB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)AUTO_INCREMENT = 780980;



INSERT INTO USERS (
    user_name, dob, gender, address, qualification,
    mobile_no, adhar_no, email, acc_type, amount,
    debit_card_no, debit_card_pin
) VALUES (
    'John Doe', '1990-05-15', 'Male', '123 Main Street, Cityville', 'Bachelor\'s Degree',
    123456789012, '1234-5678-9012', 'john.doe@example.com', 'Savings', 5000.00,
    '1234567890123456', 123456
);

select * from users;