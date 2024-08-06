 use switzbank;
CREATE TABLE USER (
    acc_no INT AUTO_INCREMENT,
    PRIMARY KEY (sno),
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

