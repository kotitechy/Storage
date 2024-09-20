-- d1
create database lab;
use lab;
CREATE TABLE customers (
    cus_id INTEGER PRIMARY KEY,
    cus_name VARCHAR(100) NOT NULL
);
CREATE TABLE items (
    item_id INTEGER PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    price int
);
CREATE TABLE sales (
    bill_no INTEGER PRIMARY KEY,
    bill_date DATE NOT NULL,
    cus_id INTEGER,
    item_id INTEGER,
    q_sold INTEGER NOT NULL CHECK (q_sold > 0),
    FOREIGN KEY (cus_id) REFERENCES customers(cus_id),
    FOREIGN KEY (item_id) REFERENCES items(item_id)
);

INSERT INTO customers (cus_id, cus_name) VALUES 
(1001, 'vamshi'),
(1002, 'ramesh'),
(1003, 'karthik'),
(1004, 'jetendra'),
(1005, 'sai'),
(1006, 'shiva'),
(1007, 'raj'),
(1008, 'pranay'),
(1009, 'karan'),
(1010, 'uma');

INSERT INTO items (item_id, item_name, price) VALUES 
(1100, 'cabinet-rgb', 200),
(1101, 'rgb-fans', 400),
(1102, 'monitors-22inch', 600),
(1103, 'keyboard-mouse combo', 300),
(1104, 'bluetooth dongle', 250),
(1105, 'rasberry pi 5-8gb', 800),
(1106, 'wifi dongle', 500),
(1107, 'power cables', 350),
(1108, 'ssd-512', 700),
(1109, 'nvme-1tb', 1200);

INSERT INTO sales (bill_no, bill_date, cus_id, item_id, q_sold) VALUES 
(13, '2023-08-05', 1001, 1103, 1),
(2, '2023-08-12', 1002, 1100, 2),
(3, '2023-08-14', 1003, 1101, 3),
(4, '2023-08-19', 1001, 1102, 15),
(5, '2023-08-21', 1007, 1103, 18),
(6, '2023-08-23', 1008, 1104, 1),
(7, '2023-08-27', 1008, 1105, 13),
(8, '2023-08-30', 1005, 1106, 20),
(9, '2023-09-01', 1003, 1107, 34),
(10, '2023-09-03', 1002, 1108, 100),
(11, '2023-09-23', 1002, 1109, 19),
(12, '2023-10-27', 1001, 1100, 24);
SELECT sales.bill_no, customers.cus_name, sales.item_id
FROM sales
JOIN customers ON sales.cus_id = customers.cus_id
WHERE sales.bill_date = CURRENT_DATE;

SELECT sales.bill_no, sales.bill_date, customers.cus_name, items.item_name, 
       sales.q_sold, items.price, (sales.q_sold * items.price) AS final_amount
FROM sales
JOIN customers ON sales.cus_id = customers.cus_id
JOIN items ON sales.item_id = items.item_id
WHERE sales.bill_date = '2023-10-27';

SELECT DISTINCT customers.cus_id, customers.cus_name
FROM customers
JOIN sales ON customers.cus_id = sales.cus_id
JOIN items ON sales.item_id = items.item_id
WHERE items.price > 200;

SELECT customers.cus_id, customers.cus_name, SUM(sales.q_sold) AS total_products_bought
FROM customers
JOIN sales ON customers.cus_id = sales.cus_id
GROUP BY customers.cus_id, customers.cus_name;

SELECT items.item_id, items.item_name, sales.q_sold
FROM sales
JOIN items ON sales.item_id = items.item_id
WHERE sales.cus_id = 1005;

SELECT items.item_id, items.item_name, SUM(sales.q_sold) AS total_sold
FROM items
JOIN sales ON items.item_id = sales.item_id
WHERE sales.bill_date = CURRENT_DATE
GROUP BY items.item_id, items.item_name;

CREATE VIEW bill_details AS
SELECT sales.bill_no, sales.bill_date, sales.cus_id, sales.item_id, 
       items.price, sales.q_sold, (sales.q_sold * items.price) AS amount
FROM sales
JOIN items ON sales.item_id = items.item_id;



