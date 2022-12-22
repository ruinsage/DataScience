-- JOIN : ���� �ٸ� ���̺��� �����Ѵ�.
-- ����Ŭ ����, �Ƚ�(ANSI) ����

-- CROSS JOIN : �ΰ��� ���̺� ���� ī�׽þ� ���δ�Ʈ(Cartesian Produnt)��
-- ���� ���(��� ����)�� ���

--����
--1 3
--2 4
-- ī�׽þ� ���δ�Ʈ ���
--1 3
--1 4
--2 3
--2 4

-- ����
--select table1.column1, table2.columns2
--from table1
--cross join table2

select employee_id from employees;
select department_name from departments;

select employee_id, department_name
from employees cross join departments;

-- NATURAL JOIN
-- �����Ϸ����ϴ� �� ���̺��� ������ �÷��� �̸��� ���� ��
select employee_id, first_name, department_id, department_name
from employees natural join departments;

-- USING�� Ȱ���� JOIN: USING ���� ����Ͽ� ���ϴ� �÷��� ���Ͽ� ��������� ����
select first_name, department_name from employees
join departments
USING (department_id);

-- ON�� Ȱ���� JOIN
-- JOING ���Ŀ� ���������� ���� �߰� ���� 3�� �̻� ���̺��� ���ε� ���� ������ JOIN�� �����ϴ�
select first_name, department_name from employees e   -- e�� ���̺� ��Ī
join departments d on (e.department_id = d.department_id);

select * from locations;
-- ���� ���̺� ����
select e.first_name as name,
       d.department_name as department,
       l.street_address || '. ' || l.city || ', ' || l.state_province as adress
from employees e
join departments d
on e.department_id = d.department_id
join locations l
on d.location_id = l.location_id;

-- where ���� ȥ��
select e.first_name as name, d.department_name as departname
from employees e
join departments d
on e.department_id = d.department_id
where employee_id = 103;

select e.first_name as name, d.department_name as departname
from employees e
join departments d
on e.department_id = d.department_id and employee_id = 103;

-- Join ���� �Է½� ����� �� : ��� ���ο� ������ �� ���ΰ�?
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
-- ����
-- SELECT
-- FROM table1
-- [LEFT|RIGHT|FULL] [OUTER] JOIN table2 <== OUTER ��������
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