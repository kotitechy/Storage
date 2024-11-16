-- WEEK-9
-- Q1
delimiter //
create  procedure update_salaries(in id int)
begin
    if id > 0 then
        update employee set salary = salary + 5 where eid=id;
    else
        select 'wrong' as e_m, eid;
    end if;
end//
delimiter ;
CREATE TABLE employee (eid INT(12),name VARCHAR(50),dept_name VARCHAR(50),salary INT(10),designation VARCHAR(50));
insert into employee (eid,name,dept_name,salary,designation) values  (12,'shiva','HR',30,'ceo');
call update_salary(12);
-- 2q
DELIMITER //
create  function is_palindrome(a char(10))
returns char(10)
begin
declare r,re char(10);
    set r:=reverse(a);
    if strcmp(a,r)=0 then
        set re = "YES";
    else set re="NO";
    end if;
    return re;
    end;//
--  call
delimiter //
select is_palindrome("shiva");//
-- Q3
create function salary_sum()
returns int begin
declare total int;
select sum(salary) into total from employee;
return total;
end;
//
select salary_sum();
//
-- Q4
create trigger b_up before update on employee for each row
begin if old.salary>10 then
set new.salary = old.salary+5000;
end if;
end;
//
--  call
 update employee set name='vamshi' where eid=12;
 //
  select * from employee;
  //