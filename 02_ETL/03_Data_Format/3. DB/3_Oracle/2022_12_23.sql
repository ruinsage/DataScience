-- �޿��� ������ ���� ���� �μ��� ��ȣ�� ����ϼ���.

select department_id from (
select nvl(department_id,0) department_id, STDDEV(salary) stdd from employees group by department_id order by department_id)
where stdd = min(stdd);

min(STDDEV(salary))
select department_id, salary from employees group by department_id, salary order by department_id;



-- 103�� ����� �̸��� �Ŵ����� �̸��� ����ϼ���.
-- ����� ������ employees, �Ŵ��� ������... employees�� ����
-- ���� ���̺��� ������ ���������̶�� �մϴ�.
-- ���̺� ��Ī�� �ݵ�� �ʿ���
-- ���� ������ �� ��Ī�� �̿��ؼ� ����
select e.first_name, m.first_name from employees e
join employees m
on m.employee_id = e.manager_id
where e.employee_id = 103;

-- 60�� �μ��� �ִ� ������ �����ȣ�� ����ϼ���.
select * from departments where department_id = 60;
select * from locations where location_id = 1400;


-- �޿��� ���� ���� ���� �޴� ����� �̸���?