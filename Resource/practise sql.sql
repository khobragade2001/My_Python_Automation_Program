----max salary from EMP
select max(salary) from emp 
select * from emp where salary=(select max(salary) from emp)

---- second max salary from emp 
select max(salary) from salary from emp where salary <(select max(salary) from emp)

---- 5 max salary 
select * from (select emp.*, dense_rank()over(order by salary desc null last)as Ranking from emp)where Ranking=5

----- duplicate ROW
select e_id,e_name,e_add,count(*) from emp group by e_id,e_name, e_add having count(*)>1

----- unique row 
select e_id,e_name,e_add,count(*) from emp group by e_id,e_name,e_add having count(*)=1

----- first five record 
select  emp.*, rownum from emp where rownum <=5;

----- last five records 
select * from (select emp.*, rownum,dense_rank()over(order by rownum desc)as ranking from emp)where ranking <=5;

----- first inserted row 
select emp.*, rowid from emp where rowid in (select min(rowid) from emp)

----- last inserted row 
select emp.*, rowid from emp where rowid in (select max(rowid) from emp)

----- department wise latest row 
select department,max(rowid)from emp group by department;

----- department wise oldest row 
select department,min(rowid) from emp group by deparrtment;

----- department wise highest salary
select max(salary) from emp group by department

----- dapartment wise min salary
select min(salary) from emp group by department

----- department wise highest salary 
select * from (select emp.*, dense_rank()over(partition by department order by salary desc )as Ranking from emp)where Ranking=1

----- in civil department third max salary
select * from (select emp.*, dense_rank()over (partition by department order by salary desc)as ranking from emp where department="civil")where ranking =3;

----- to change gander m as male and f as female 
select gender case when gender ="m" then "male" else "female" end as full_form_gender from emp;

----- to chage month 1 to jan,2 to feb,3 to march and so ON
select gender case when cal_month = 1 then "jan" cal_month=2 then "feb" cal_month=3 then "march" end as name_month from emp

----- sum of positive value in one colume and negative value sin anather column 
select sum(case when balance >0 then balance else null end) as positive_bal,
sum(case when balance< 0 then balance else null end) as negative_balfrom EMP

------ display data in two table having table name orders and sales
select cust_name,cust_id,cust_order,sale_amount from sales, orders where sales.sale_id = orders.order_id

-----  