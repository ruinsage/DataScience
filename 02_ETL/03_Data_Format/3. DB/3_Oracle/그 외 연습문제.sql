2. ����� �̸�, �޿�, ���� �� ������ �� ������ ���� �ͺ��� ���� ������ ����Ͻÿ�, 
���� �Ѽ����� ���޿� 12�� ���� �� $100�� �󿩱��� ���ؼ� ����Ͻÿ�.

select first_name as �̸�, salary as �޿�, salary*12+100 as ����_��_���� from employees
order by ����_��_���� desc;

3. �޿��� 2000�� �Ѵ� ����� �̸��� �޿��� ǥ��, �޿��� ���� �ͺ��� ���� ������
����Ͻÿ�.

select first_name �̸�, salary �޿� from employees where salary >= 2000
order by salary desc;

4. �����ȣ�� 203�� ����� �̸��� �μ���ȣ�� ����Ͻÿ�.

select first_name, department_id from employees where EMPLOYEE_ID = '203';

5. �޿��� 2000���� 3000 ���̿� ���Ե��� �ʴ� ����� �̸��� �޿��� ����Ͻÿ�.

select first_name, salary from employees where salary not between 2000 and 3000;

6. 2005�� 3�� 20�� ���� 2005�� 8�� 1�� ���̿� �Ի��� ����� �̸�, ������, �Ի�����
����Ͻÿ�.

select first_name, job_id, hire_date from employees 
where hire_date between '05/03/20' and '05/08/01' order by hire_date;

7. �μ���ȣ�� 20 �� 30�� ���� ����� �̸��� �μ���ȣ�� ���,
�̸��� ����(��������)���� �����ڼ����� ����Ͻÿ�.

select first_name, department_id from employees
where department_id = 20 or department_id = 30 order by first_name desc;

8. ����� �޿��� 2000���� 3000���̿� ���Եǰ� �μ���ȣ�� 20 �Ǵ� 30�� �����
�̸�, �޿��� �μ���ȣ�� ���, �̸���(��������)���� ����Ͻÿ�.

select first_name �̸�, salary �޿�, department_id �μ���ȣ from employees
where salary >= 2000 and salary <= 3000 and department_id = 20 or department_id = 30
order by first_name;

9. 2006�⵵�� �Ի��� ����� �̸��� �Ի����� ����Ͻÿ�.
-- (like �����ڿ� ���ϵ�ī�� ���)

select first_name, hire_date from employees where hire_date like '06%';

10. �����ڰ� ���� ����� �̸��� ��� ������ ����Ͻÿ�.

select first_name name, job_id job from employees where manager_id is null;

11. Ŀ�̼��� ���� �� �ִ� �ڰ��� �Ǵ� ����� �̸�, �޿�, Ŀ�̼��� ����ϵ�
�޿� �� Ŀ�̼��� �������� �������� �����Ͽ� ǥ���Ͻÿ�.

select first_name name, salary, commission_pct commission from employees
where commission_pct is not null order by commission_pct desc;

12. �̸��� ����° ���ڰ� R�� ����� �̸��� ǥ���Ͻÿ�.

select first_name name from employees where first_name like '__r%';

13. �̸��� A�� E�� ��� �����ϰ� �ִ� ����� �̸��� ǥ���Ͻÿ�.

select first_name name from employees
where first_name like '%A%' or first_name like '%E%';

14. �������� CLERK, �Ǵ� SALESMAN�̸鼭 �޿��� $1600, $950 �Ǵ� $1300�� �ƴ� �����
�̸�, ������, �޿��� ����Ͻÿ�.

select first_name name, job_id job, salary from employees
where job_id like '%CLERK%' or job_id = 'SA_MAN';

15. Ŀ�̼��� $500 �̻��� ����� �̸��� �޿� �� Ŀ�̼��� ����Ͻÿ�.

select first_name name, salary, commission_pct*salary as com from employees
where comt*salary >= '500';

16. SUBSTR �Լ��� ����Ͽ� ������� �Ի��� �⵵�� �Ի��� �޸� ����Ͻÿ�.

select substr(hire_date,1,2) year, substr(hire_date,4,2) month from employees;










 
