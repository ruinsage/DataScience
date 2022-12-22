-- JOIN : 서로 다른 테이블을 병합한다.
-- 오라클 조인, 안시(ANSI) 조인

-- CROSS JOIN : 두개의 테이블에 대한 카테시안 프로덕트(Cartesian Produnt)와
-- 같은 결과(모든 조합)을 출력

--원본
--1 3
--2 4
-- 카테시안 프로덕트 결과
--1 3
--1 4
--2 3
--2 4

-- 문법
--select table1.column1, table2.columns2
--from table1
--cross join table2

select employee_id from employees;
select department_name from departments;

select employee_id, department_name
from employees cross join departments;

-- NATURAL JOIN
-- 조인하려고하는 두 테이블에서 조인할 컬럼의 이름이 같을 때
select employee_id, first_name, department_id, department_name
from employees natural join departments;

-- USING을 활용한 JOIN: USING 절을 사용하여 원하는 컬럼에 대하여 명시적으로 조인
select first_name, department_name from employees
join departments
USING (department_id);

-- ON을 활용한 JOIN
-- JOING 이후에 서브쿼리와 같은 추가 서술 3개 이상 테이블에서 조인등 보다 복잡한 JOIN이 가능하다
select first_name, department_name from employees e   -- e는 테이블 별칭
join departments d on (e.department_id = d.department_id);

select * from locations;
-- 여러 테이블 조인
select e.first_name as name,
       d.department_name as department,
       l.street_address || '. ' || l.city || ', ' || l.state_province as adress
from employees e
join departments d
on e.department_id = d.department_id
join locations l
on d.location_id = l.location_id;

-- where 절과 혼용
select e.first_name as name, d.department_name as departname
from employees e
join departments d
on e.department_id = d.department_id
where employee_id = 103;

select e.first_name as name, d.department_name as departname
from employees e
join departments d
on e.department_id = d.department_id and employee_id = 103;

-- Join 조건 입력시 고려할 점 : 어느 조인에 조건을 걸 것인가?
select e.first_name as name,
       d.department_name as department,
       l.street_address || '. ' || l.city || ', ' || l.state_province as adress
from employees e
join departments d
on e.department_id = d.department_id and employee_id = 103
join locations l
on d.location_id = l.location_id;

select e.first_name as name,
       d.department_name as department,
       l.street_address || '. ' || l.city || ', ' || l.state_province as adress
from employees e
join departments d
on e.department_id = d.department_id 
join locations l
on d.location_id = l.location_id and employee_id = 103;

-- OUTER JOIN
-- 문법
-- SELECT
-- FROM table1
-- [LEFT|RIGHT|FULL] [OUTER] JOIN table2 <== OUTER 생략가능
-- ON

select e.employee_id, e.first_name, e.hire_date,
       j.start_date, j.end_date, j.job_id, j.department_id
from employees e
left join job_history j
on e.employee_id = j.employee_id
order by j.employee_id;

select e.employee_id, e.first_name, e.hire_date,
       j.start_date, j.end_date, j.job_id, j.department_id
from employees e
right join job_history j
on e.employee_id = j.employee_id
order by j.employee_id;

select e.employee_id, e.first_name, e.hire_date,
       j.start_date, j.end_date, j.job_id, j.department_id
from employees e
full join job_history j
on e.employee_id = j.employee_id
order by j.employee_id;