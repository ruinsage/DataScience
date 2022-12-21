------------------------------------------------------------------------------
--   �׷� �Լ��� �̿��� ������ ����
------------------------------------------------------------------------------

-- COUNT, SUM, AVG, MIN, MAX, VARIANCE, STDDEV
-- (salary)
select COUNT(salary) count, SUM(salary) sum, round(AVG(salary)), MIN(salary) MIN,
MAX(salary) MAX, round(VARIANCE(salary)) VARIANCE, round(STDDEV(salary)) STDDEV from employees;

SELECT min(hire_date), max(hire_date) from employees;

SELECT min(first_name), max(first_name) from employees;

-- Q] ���� ū �޿�����?
select max(salary) from employees;

-- Q] ������� �޿��� ����, ���, ǥ������, �л��� ���ϼ���.
select sum(salary) sum, round(avg(salary),2) avg,
round(variance(salary),2) variance, round(stddev(salary),2) stddev
from employees;

-- ����Լ� ���� ������ ��
select commission_pct  from employees;
select round( sum(salary*commission_pct),2) sum_bonus,
       round( sum(salary*commission_pct)/count(*),2) avg_bonus1,
       -- sum�Լ��� ����� �λ���� ��� count �Լ��� null���� ����
       round( avg(salary*commission_pct),2) avg_bonus2
       -- avg�Լ��� ����� �λ���� ��� avg�Լ��� null���� �����Ѵ�.
       from employees;

-- GROUP BY
select department_id from employees group by department_id;

-- GROUP BY�� ���� �Լ� ����
select department_id, round(avg(salary),2) avg from employees group by department_id;

-- �ϳ� �̻��� ���� �׷�ȭ �ϱ�
-- select/group by�� �����ϴ� �� �̸��� ��ġ�ؾ� �Ѵ�.
select department_id, job_id, round(avg(salary),2) avg  from employees 
group by department_id, job_id order by department_id desc;

-- �׷� �Լ��� �߸� �Ͽ��� ���
-- �������� ���� �׷��Լ��� ȥ���ؼ� ����� ������ �������� ���� ����ϴ�
-- group by���� �ݵ�� �����ؾ� �Ѵ�.
select department_id, count(first_name) from employees;

select department_id, count(first_name) from employees group by department_id;


-- group by ����

-- select
-- from
-- where
-- group by <- �� ��ġ���� ���
-- having
-- order by

-- having : group by�� ����� ���͸� �� �� ����Ѵ�.

select department_id, round(avg(salary),2) from employees 
group by department_id having avg(salary) >= 8000;

select job_id, avg(salary) payroll from employees
where job_id not like 'SA%' group by job_id having avg(salary) > 8000
order by payroll;

-- grouping set : �������� �׷���� �����ϰ� ó��, union all�� ����� ��ü
select to_char(department_id), round(avg(salary),2) from employees
group by department_id;

select job_id, round(avg(salary),2) from employees group by job_id;

-- ���� �̸��� grouping�� ���� ��ġ������ �ʴ´�.
select to_char(department_id), round(avg(salary),2) from employees
group by department_id
union all
select job_id, round(avg(salary),2) from employees group by job_id;

-- �� ����� grouping sets �Լ��� ���� ����
select department_id, job_id, round(avg(salary),2) from employees
group by grouping sets (department_id, job_id) order by department_id, job_id;

-- grouping set Ȯ��
-- groupin set ((�׷��1),(�׷��2)...)
select department_id, job_id, manager_id, round(avg(salary),2) from employees
group by grouping sets ((department_id, job_id),(job_id, manager_id)) 
order by department_id, job_id, manager_id;

-- ROLLUP, CUBE
-- �μ���, ������ �޿��� ��հ� ����� ���� ����϶�.
select department_id, job_id, round(avg(salary),2), count(*) from employees
group by (department_id, job_id) order by department_id, job_id;

select department_id �μ��ڵ�, NVL(job_id, '�μ����') �������μ�, round(avg(salary),2) ���, count(*) �μ��ο� from employees
group by rollup (department_id, job_id) order by department_id, job_id;
-- ROLLUP�� ������ ���谡 �����ϴ�. ������ ���� ��ü������ ������� ����Ѵ�.

select count() from employees;