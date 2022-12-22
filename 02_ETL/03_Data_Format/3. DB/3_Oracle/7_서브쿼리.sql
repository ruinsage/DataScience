-- �������� : ������ �� ���� �������踦 Ȱ���Ͽ� ��ø�� ������ �ۼ��� �ϳ��� �˻� ����� �ڵ����� �ϼ��Ѵ�.

-- Nancy�� �޿����� ���� �޿��� �޴� ����� �̸��� �޿��� ���

select salary from employees where first_name = 'Nancy';

select first_name salary from employees where salary > 12008;

-- ���� ������ ���� : ������ ��������, ������ ��������
-- ���� ���� Ȱ��(������ ��������: �ϳ��� ���� ��ü)
select first_name salary from employees where salary > 
(select salary from employees where first_name = 'Nancy');

-- where ���ǿ� ���� ���ͷ����� ����ؾ��ϳ� ������(������)�� ���� ��Ī�ǹǷ� ���� �߻�
select first_name salary from employees where salary > 
(select salary from employees where first_name = 'David');
-- ������ ����
select first_name, salary, job_id from employees where first_name = 'David';

-- ������ ��������
-- ANY/ALL
-- ANY : �ϳ��� �����ϴ� ����/ ALL : ��� ���� �����ϴ� ����
-- > ANY : ���� ���� ������ ū ���� (MIN ����)
-- < ANY : ���� ū ������ ���� ���� (MAX ����)
-- > ALL : ���� ū ������ ���� ���� (MAX ����)
-- < ALL : ���� ���� ������ ū ���� (MIN ����)

select first_name, salary from employees
where salary >  ANY(select salary
                    from employees
                    where first_name = 'David');
                    
-- IN�� ���������� Ȱ��: ����� � ���� ������ Ȯ��
-- STEP1: �˻� ������ Ȯ��
select department_id from employees where first_name = 'David'; --60, 80, 80
-- STEP2
select first_name, department_id, job_id from employees
where department_id in (select department_id from employees where first_name = 'David');

select first_name, department_id, job_id from employees
where department_id in (60,80,80);

-- Q] 20�� �μ��� �ٹ��ϴ� ����� ��պ��� ���� �޿��� ���� ����� �̸��� �޿��� ����Ͻÿ�.
select first_name, salary from employees 
where salary > (select avg(salary) from employees where department_id = 20);

-- ��ȣ ���� ���� : ���� ������ ���̺��� ������������ ���Ǵ� ����
-- �ڽ��� ���� �μ��� ��պ��� ���� �޿��� �޴� ����� �̸��� �޿��� ���
select first_name, salary from employees a 
where salary > (select avg(salary) from employees b where b.department_id = a.department_id);

-- select ������ �������� ��� -> Scalar Sub Query
-- Select ������ Join�� ������ ����Ͽ� Join�� ��� ������ ���δ�.
-- ��Ȳ�� ���� Join���� ���� ������ ���̱� ������ ����Ѵ�. (�׻� ������ ���� ���� �ƴϴ�.)
select first_name, department_name from employees e
join departments d on (e.department_id = d.department_id)
order by first_name;

select first_name, (select department_name from departments d
where d.department_id = e.department_id) department_name
from employees e order by first_name;

-- �ζ��� ��
-- from ���� �����ϴ� ��������. from ������ ���̺� �Ǵ� �䰡 �� �� �ִ�.
-- ���������� �������� ���� �� �� �ֱ� ������ �ζ��� ��� Ī�Ѵ�.

-- Q] �޿��� ���� ���� �޴� ���� 10�� ����� �̸��� �޿��� ���
select first_name, salary 
from (
    select first_name, salary 
    from employees
    )
where rownum between 1 and 10
order by salary desc;
