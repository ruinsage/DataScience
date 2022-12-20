-- * �Լ�
-- -������ �Լ� : ���� �࿡���� ���� �����ϰ� �ະ�� �ϳ��� ����� ����
-- -������ �Լ� : ���� ���� �����Ͽ� ���� �׷�� �ϳ��� ����� ����(��: count())
-- > ������ �Լ� : �����Լ�, �����Լ�, ��¥�Լ�, ��ȯ�Լ�, �Ϲ��Լ�
--------------------------------------------------------------------------
-- �����Լ�
--------------------------------------------------------------------------

-- dual ���̺� : ����Ŭ ��ü���� ���� Ȯ���Ϸ��� �뵵�� �����ϴ� ���̺�
select * from dual;

-- initcap : �ܾ �������� ù ���ڸ� �빮�ڷ� �������� �ҹ��ڷ� ��ȯ�ϴ� �Լ�
select initcap('python specialist') from dual;
select initcap('pythonSpecialist') from dual;
-- lower : ��ü�� �ҹ��ڷ� ����� �Լ�
select lower('pythonSpecialist') from dual;
-- upper: ��ü�� �빮�ڷ� ����� �Լ�
select upper('pythonSpecialist') from dual;

-- length : ���ڿ� ���̼��� ��ȯ�ϴ� �Լ�
select length('pythonSpecialist') from dual;
select length('���̽�������') from dual;
-- �ѱ۵� byte���� �ƴ϶� ���ڼ��� ����Ͽ� ���̸� ��ȯ�Ѵ�

-- concat : �� ���ڿ��� �����Ͽ� ��ȯ�Ѵ�.
select concat('���̽�','������') from dual;

-- substr : substr(���ڿ�,�����ε���,���ε���)
-- ���ڿ��� �������� �����ε������� �� �ε����� ���ڿ��� ��ȯ�Ѵ�.
-- (���ڿ��� �����ε����� 1����)
select substr('���̽�������',4,6) from dual;

-- instr : instr(���ڿ�,ã�����ϴ� ���ڿ�)
-- ���ڿ��� �������� ã�����ϴ� ���ڿ��� �ε����� ��ȯ�Ѵ�.
select instr('���̽�������','��') from dual;
select instr('���̽�������','��') from dual;
-- ��ġ�� �Ǵ� ���ڿ��� ������ 0�� ��ȯ�Ѵ�.

-- rpad/lpad(���ڿ�,ä���ڸ���,ä�﹮��)
-- rpad/lpad: �־��� �ڸ�����ŭ ������(rpad)/����(lpad)�� ������ ���ڿ��� ä���.
-- byte�� ����ϹǷ� �ѱ��� �ѱ��ڿ� ���ڸ��� ����Ѵ�.
select rpad('ȫ�浿',10,'*') from dual;
select lpad('ȫ�浿',10,'*') from dual;
-- Q] ���� ���̺��� �̸� 10�ڸ��� ������ �������� '-'���� ä���
-- �޿� 10�ڸ��� ������ ������ '*'�� ä���� ����ϼ���.
select rpad(first_name,10,'-') as name, lpad(salary,10,'*') salary from employees;

-- ltrim/rtrim/trim(���ڿ�,������ ���ڿ�) ������ ���ڿ� �⺻���� ���鹮��
-- ltrim/rtrim : ���ڿ��� �������� ������ ���ڸ� ���� ����,���������� ����
-- trim(���ڿ�)
-- trim : ���ڿ��� �������� ���鹮�ڸ� �������� ����
select ltrim('    ���̽�   ������    ') as name from dual;
select ltrim('���̽����������̽�','���̽�') name from dual;
select rtrim('    ���̽�   ������    ') name from dual;
select rtrim('���̽� ������ ���̽�','���̽�') name from dual;
select trim(' ���̽� ������ ���̽� ') name from dual;
-- ltrim ��ȭ
select ltrim('JavaSpecialist','Java') name from dual;
-- ������ ���ڿ��� ������ ������ ������� �ʴ´�.
select ltrim('JavaSpecialist','Jav') name from dual;
-- ���Ŵ� �������� ���ϴ� ���ڸ� ���� �߰��� ������ �����Ѵ�.
select ltrim('JavaSpecialist','avJ') name from dual;
select ltrim('JavaSpecialist','aJv') name from dual;

-- replace
select replace('Python Specialist','Python','bigdata') from dual;
select replace('Python Specialist',' ','') from dual;
-- ���鹮�� �����Ѵ�.

-- translate(���� ���ڿ�,��Ī���ڿ�,��ȯ���ڿ�)
select translate('1234abcd','abcd','ABC') from dual;
select translate('hello world!!!','hw','HW') from dual;
select translate('hello world!!!','!','?') from dual;
select translate('$100','$','') from dual;
-- ��ȯ�� ���ڰ� ���ٸ� null ��ȯ�Ѵ�.
select translate('$100','$','��') as m from dual;
select translate('$1,000,000','$,',' ') from dual;
-- ��ȭ ��ȣ �� ������ȣ �����ϴ� ���

-- Q] ���� ���̺��� �̸��� �̸� �״��, �ҹ��ڷ�, ù���ڸ� �빮�ڷ�, ��� �빮�ڷ� ����غ�����.
select first_name || ' ' || last_name, lower(first_name || ' ' || last_name),
initcap(first_name || ' ' || last_name), upper(first_name || ' ' || last_name) from employees;

-- Q] �������̺��� �̸��� 'austin'�� ������ �̸��� �̸��״��, �ҹ��ڷ�, ù���ڸ� �빮�ڷ�, ��� �빮�ڷ� ����غ�����.
-- �˻��� �ҹ��ڷ� �� ��
select last_name, lower(last_name), initcap(last_name), upper(last_name) 
from employees where lower(last_name) = 'austin';

-- Q] �������̵� it_prog�� (�ݵ�� �ҹ��ڷ� �˻��ؾ���) ����� �̸� �տ� 3�ڸ��� ����ϰ� �������ڸ��� *�� ����ϸ�
-- salary�� ��ü 10�ڸ� �� ������ ����ϰ� �������� *�� ����Ѵ�.
select rpad(substr(first_name,1,3),length(first_name),'*'), lpad(salary,10,'*') from employees where lower(job_id) = 'it_prog';

--------------------------------------------------------------------------
-- �����Լ�
--------------------------------------------------------------------------
-- �ݿø� : round
select round(45.966,2), round(45.966,0), round(45.966,-1) from dual;

-- �ø� : ceil (default�� �Ҽ��� ù�ڸ�)
select ceil(7.3) from dual;

-- ���� : floor
select floor(7.3) from dual;

-- ���� : trunc(������,�ڸ���) �ڸ�����ŭ �������� ���� ����
select trunc(45.923,2), trunc(45.923), trunc(45.923,-1) from dual;

-- to_date(��¥��Ʈ��,����)
select to_date('2022-12-20','YYYY-MM-DD') as dt from dual;

-- floor�� �����ϳ� trunc�Լ��� ��¥Ÿ�Կ��� ������ �� �ִ�.
-- trunc�Լ��� �����Ͽ� �ſ� ù°���� ���ϱ�
select trunc(to_date('2022-12-20','YYYY-MM-DD'),'MM') as dt from dual;

-- Q] trunc�Լ��� �����Ͽ� 2022�� ù°���� ���ϱ�
select trunc(to_date('2022-12-20','YYYY-MM-DD'),'YYYY') as dt from dual;
-- DD�� �����ϸ� �ϴ����� ������ ��¥�� �����Ƿ� ������ ���� ��ȯ
select trunc(to_date('2022-12-20','YYYY-MM-DD'),'DD') as dt from dual;
-- DAY�� �����ϸ� �� ���� ù��° �Ͽ����� ��ȯ
select trunc(to_date('2022-12-31','YYYY-MM-DD'),'DAY') as dt from dual;

select trunc(to_date('2022-12-20','YYYY-MM-DD'),'WEEK') as dt from dual;

-- ���밪
select abs(-1000) abs from dual;

-- ������
select power(2,3) power from dual;

-- ������
select sqrt(100) sqrt from dual;

-- ������
select mod(10,3) mod from dual;

--------------------------------------------------------------------------
-- ��¥�Լ�
--------------------------------------------------------------------------

-- SYSDATE : ������ ��¥�� ��ȯ(YY/MM/DD)
select sysdate from dual;

-- SYSTIMESTAMP: ������ ��¥�� �ð��� ��ȯ
select systimestamp from dual;

-- Q] �μ���ȣ�� 60�� ����� �̸��� ������� �ٹ��� �ָ� 'Week' �� �̸����� ���
select first_name, ceil((sysdate - hire_date)/7) as Weeks from employees where department_id = 60;
--select to_date(hire_date,'DD') from employees;

-- MONTHS_BETWEEN : �� ���� ������ �� ���� ��ȯ�Ѵ�.
select first_name, sysdate, hire_date, ceil(months_between(sysdate, hire_date)) as workmonth from employees;

-- ADD_MONTHS : �����Ͽ� ���� ����
select first_name, hire_date, ADD_MONTHS(hire_date,1) from employees where first_name = 'Diana';

-- Q] �� ������ Ȱ���Ͽ� Diana�� ������ 200������ ���� ��¥�� ���ϼ���.
select first_name, hire_date, ADD_MONTHS(hire_date,200) from employees where first_name = 'Diana';

-- NEXT_DAY : ���ƿ��� ���� �ֱ� ���� ��¥
select sysdate, next_day(sysdate,'��') from dual;
select sysdate, next_day(sysdate,'��') from dual;

-- select sysdate, next_day(sysdate,'M') from dual;

-- LASR_DAY : �ش� ���� ���Ե� ���� ������ ��¥
select sysdate, last_day(sysdate) from dual;

-- Q] 1������ 12������ ���������� ����ϼ���.
select TO_CHAR(last_day('22/01/01'),'dd') AS "1", TO_CHAR(last_day('22/02/01'),'dd') as "2", TO_CHAR(last_day('22/03/01'),'dd') AS "3", TO_CHAR(last_day('22/04/01'),'dd') AS "4",
TO_CHAR(last_day('22/05/01'),'dd') AS "5", TO_CHAR(last_day('22/06/01'),'dd') AS "6", TO_CHAR(last_day('22/07/01'),'dd') AS "7", TO_CHAR(last_day('22/08/01'),'dd') AS "8",
TO_CHAR(last_day('22/09/01'),'dd') AS "9", TO_CHAR(last_day('22/10/01'),'dd') AS "10", TO_CHAR(last_day('22/11/01'),'dd') AS "11", TO_CHAR(last_day('22/12/01'),'dd') AS "12" from dual;

select last_day('22/05/01') as "12" from dual;
select TO_CHAR(to_date('22/05/31'),'dd')  as "12" from dual;