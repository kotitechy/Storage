use lab;
CREATE TABLE membership (
    mem_no INTEGER PRIMARY KEY,
    stud_no INTEGER NOT NULL
);

CREATE TABLE book (
    book_no INTEGER PRIMARY KEY,
    book_name VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL
);

CREATE TABLE iss_record (
    iss_no INTEGER PRIMARY KEY,
    iss_date DATE NOT NULL,
    mem_no INTEGER,
    book_no INTEGER,
    FOREIGN KEY (mem_no) REFERENCES membership(mem_no),
    FOREIGN KEY (book_no) REFERENCES book(book_no)
);
INSERT INTO membership (mem_no, stud_no) VALUES 
(1, 101),
(2, 102),
(3, 103),
(4, 104),
(5, 105),
(6, 106),
(7, 107),
(8, 108),
(9, 109),
(10, 110);
INSERT INTO book (book_no, book_name, author) VALUES 
(201, 'Introduction to Programming', 'Korth'),
(202, 'Data Structures', 'Korth'),
(203, 'Database Management Systems', 'Silberschatz'),
(204, 'Operating Systems', 'Stallings'),
(205, 'Computer Networks', 'Korth'),
(206, 'Artificial Intelligence', 'Russell'),
(207, 'Software Engineering', 'Pressman'),
(208, 'Web Development', 'Korth'),
(209, 'Machine Learning', 'Murphy'),
(210, 'Cybersecurity Essentials', 'Korth');
INSERT INTO iss_record (iss_no, iss_date, mem_no, book_no) VALUES 
(1, '2023-09-01', 1, 201),
(2, '2023-09-02', 2, 202),
(3, '2023-09-03', 3, 203),
(4, '2023-09-01', 4, 204),
(5, '2023-09-05', 5, 205),
(6, '2023-09-01', 6, 206),
(7, '2023-09-02', 7, 207),
(8, '2023-09-03', 8, 208),
(9, '2023-09-02', 9, 209),
(10, '2023-09-03', 10, 210);

SELECT membership.mem_no, membership.stud_no
FROM membership;

SELECT iss_record.iss_no, membership.stud_no, book.book_name
FROM iss_record
JOIN membership ON iss_record.mem_no = membership.mem_no
JOIN book ON iss_record.book_no = book.book_no
WHERE iss_record.iss_date = CURRENT_DATE;

SELECT DISTINCT membership.stud_no, book.book_name
FROM iss_record
JOIN membership ON iss_record.mem_no = membership.mem_no
JOIN book ON iss_record.book_no = book.book_no
WHERE book.author = 'Korth';

SELECT membership.stud_no, COUNT(iss_record.book_no) AS total_books_issued
FROM membership
LEFT JOIN iss_record ON membership.mem_no = iss_record.mem_no
GROUP BY membership.stud_no;

SELECT book.book_name
FROM iss_record
JOIN book ON iss_record.book_no = book.book_no
WHERE iss_record.mem_no = (SELECT mem_no FROM membership WHERE stud_no = 5);

SELECT book.book_name, iss_record.iss_date
FROM iss_record
JOIN book ON iss_record.book_no = book.book_no
WHERE iss_record.iss_date = CURRENT_DATE;

CREATE VIEW issue_details_view AS
SELECT iss_record.iss_no, iss_record.iss_date, membership.stud_no, book.book_name
FROM iss_record
JOIN membership ON iss_record.mem_no = membership.mem_no
JOIN book ON iss_record.book_no = book.book_no;

CREATE VIEW weekly_issues AS
SELECT iss_record.iss_date, COUNT(iss_record.iss_no) AS total_issues
FROM iss_record
WHERE iss_record.iss_date >= CURRENT_DATE - 7
GROUP BY iss_record.iss_date
ORDER BY iss_record.iss_date;
select * from issue_details_view;


