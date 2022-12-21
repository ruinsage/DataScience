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
select TO_CHAR(to_date('22/05/31'),'yyyy-mm-dd')  as "12" from dual;

-------------------------------------------------------------------------------
-- ��ȯ �Լ�
-------------------------------------------------------------------------------
-- �Ͻ��� �� ��ȯ
-- number <-> character <-> date

select first_name from employees where department_id = 40; 
-- 40�� ����Ÿ��

select first_name from employees where department_id = '40'; 
-- 40�� ����Ÿ���̺� �Ͻ��� ����ȯ�� ���̳���.

select first_name from employees where hire_date = '03/06/17';
-- 03/06/17 ����Ÿ�������� �Ͻ��� �� ��ȯ�� �Ͼ��.

select '5500.00' - 4000 from dual;
-- ������ ������ �� �����ʹ� �Ϲ��� �� ��ȯ�� ���� �ʴ´�.
select '$5,500.00' - 4000 from dual;
select first_name from employees where hire_date = '03�� 06�� 17��';

-- ����� ����ȯ
-- TO_CHAR : ����(��¥)���� ��¥������ �����Ͽ� ���ڷ� ��ȯ, TO_CHAR(��¥,��¥����)
select first_name, to_char(hire_date,'YYYY"��" MM"��" DD"��"') as HiredMonth from employees
where first_name = 'Steven';

-- TO_CHAR: ����(����)���� ���������� �����Ͽ� ���ڷ� ��ȯ, TO_CHAR(����,��������)
-- ex)$999,999 <- ���ڴ� 9�� ǥ��
-- ���亸�� ��ȯ ���̰� ū ��쿡�� '#'���� ǥ��
select to_char(2000000,'$999,999') salary from dual;
select to_char(2000000,'$9,999,999') salary from dual;

-- �տ� 0���� padding�ϰ� ���� ��� -> ��ǥ�ݾ��� �ڸ����� ����Ͽ� ǥ���ϰ� ���� ���
select to_char(2000000,'$009,999,999') salary from dual;

-- �Ҽ��� ���� �ڸ��� ���� ������ ���ٸ� �� ���� �����ȴ�.
select to_char(2000000.45,'$009,999,999') salary from dual;
-- �Ҽ��� ó��
select to_char(2000000.45,'$009,999,999.99') salary from dual;
-- ��������ȭ�� ��ȣ ��� (��ȣ'L' ���)
select to_char(2000000.45,'L9,999,999') salary from dual;

-- Q] ���� ���̺� �̸��� David�� �̸�, ��, �޿�, 15% �λ�� �ݾ��� salary1����
-- 15.23% �λ�� �ݾ��� ������ ���� ����($1,446,85)�� �����Ͽ� ����Ͻÿ�
select first_name, last_name, salary, salary*0.15 salary1,
to_char(salary *0.1523,'$99,999.99') as salary2 from employees where first_name = 'David';

-- ���ϴ� ��¥ �������� �˻��ϱ� (to_date: ���ڸ� ��¥ Ÿ������ ����)
select first_name, hire_date from employees where hire_date = To_date('2003/06/17','YYYY/MM/DD');
-- Q] '2003�� 06�� 17��'�� �Ի��� �����̸�, �Ի����� ����ϼ���.
select first_name, hire_date from employees where hire_date = To_date('2003�� 06�� 17��','YYYY"��"MM"��"DD"��"');
-- Q] ��¥ Ÿ���� �Ʒ��� ���� ��µǵ��� '03/06/17'�� �Ի��� ������ �����̸�, �Ի�����  ����ϼ���.
-- '2003-06-17'
select first_name, To_char(hire_date,'YYYY-MM-DD') from employees where hire_dat = '03/06/17';

-- NULL ��ȯ
-- NVL
-- NVL(������,���̸� ��ȯ�Ǵ� ��) <= ���� ���� ���� �ƴϸ� �������� ��ȯ�Ѵ�.
select nvl(1000,100) from dual;
select nvl(null,100) from dual;

select commission_pct from employees;
select first_name, salary, commission_pct, salary+salary*commission_pct as �λ��_�ѱ޿�
from employees;

-- Q] �� ������ NVL �Լ��� ����Ͽ� �λ�� �ѱ޿����� NULL�� ������ �ʵ��� �����ϼ���.
select first_name, salary, commission_pct, salary+salary*nvl(commission_pct,0) as �λ��_�ѱ޿�
from employees;

-- NVL2(������,���� �ƴϸ� ��ȯ�Ǵ� ��, ���̸� ��ȯ�Ǵ� ��)
select nvl2(0.2, 1000*0.2, 0) from dual;
select nvl2(null, 1000*0.2, 0) from dual;

-- Q] �� ������ NVL2�Լ��� �̿��Ͽ� Ǯ�����.
select first_name, salary, commission_pct, salary+nvl2(salary * commission_pct,salary,0) as �λ��_�ѱ޿�
from employees;

-- COALESCE(�� �Ǵ� ����1, �� �Ǵ� ����2) : ���� �ƴ� ù��° ������ ���� ����
-- ��) �� �����ͺ��̽����� ���� ������ ��ȣ�� �����ϰ��� �� ��
-- ���ð����� ��(�޴���, ����ȭ, ȸ���ȣ)�� ���� �ƴ� ���� �����ϰ��� �� �� �����ϴ�.
select coalesce('010-123-4567',null,null) from dual;
select coalesce(null,'070-123-4567',null) from dual;
select coalesce(null,null,'02-123-4567') from dual;

-- Q] �� ������ coalesce�Լ��� �̿��Ͽ� Ǯ�����.
select first_name, salary, commission_pct,
coalesce(salary + salary*commission_pct,salary) as �λ��_�ѱ޿� from employees;

-- Q] ���ʽ��� 650�޷����� �۰ų� ���ʽ��� ���� ����鿡�� ��ǰ���� �����Ϸ��� �մϴ�.
-- �ش� ������� �̸��� ���ʽ��� ����ϼ���. (coalesce �Լ� ����� ��)
select first_name, replace(coalesce(salary*commission_pct,0),0,'gift card') bonus 
from employees where coalesce(salary*commission_pct,0) < 650 ;

-- LNNVL: LNNVL(����) ������ ����� FALSE �Ǵ� UNKKNOWN�̸� TRUE�� ��ȯ
-- ������ �ݴ� ��쿡 ���� �˻��ϰ� ���� �� Ȱ��
select first_name, replace(coalesce(salary*commission_pct,0),0,'gift card') bonus 
from employees where LNNVL(salary*commission_pct >= 650) ;

-- DECODE : DECODE(Column or expression, serch1, result1
--                                       serch2, result2,....)
-- �� Ȥ�� ǥ������ serch ���� ������ result ���� ��ȯ�� �ش�.
select decode('java','java','�鿣�� ���') as language from dual;
select decode('java','java','�鿣�� ���'
                    ,'html','����Ʈ ���'
                    ,'python','�����ͻ��̾� ���'
            ) as language from dual;
select decode('html','java','�鿣�� ���','html','����Ʈ ���','python','�����ͻ��̾� ���') as language from dual;
select decode('java','java','�鿣�� ���'
                    ,'html','����Ʈ ���'
                    ,'python','�����ͻ��̾� ���'
            ) as language from dual;
select decode('css','java','�鿣�� ���'
                    ,'html','����Ʈ ���'
                    ,'python','�����ͻ��̾� ���'
                    ,'��Ÿ���'  -- ����Ʈ search ��
            ) as language from dual;

-- Q] ���� ���̺��� ���� ID, �޿�, �׸��� '�޿��λ���'�� ����Ѵ�.
-- �޿��λ����� ���� ID�� IT_PROG, FI_MGR, FI_ACCOUNT�� ���� ���� 10,15,20% �λ����� �����Ѵ�.
-- decode ����� ��
select job_id, salary, floor(salary*decode(job_id,'IT_PROG',1.1,
                                                  'FI_MGR',1.15,
                                                  'FI_ACCOUNT',1.2,
                                                  1)) rise_salary
                                                  from employees;

-- CASE ~ WHEN ~ THEN ~ ELSE ~ END 
select job_id, salary, 
    floor(salary* case job_id when 'IT_PROG' then 1.1
                              when 'FI_MGR' then 1.15
                              when 'FI_ACCOUNT' then 1.2
                              else 1 
                              end) as rise_salary
                              from employees;
-- ���� ���� �����
select job_id, salary, 
    floor(salary* case when job_id = 'IT_PROG' then 1.1
                       when job_id = 'FI_MGR' then 1.15
                       when job_id = 'FI_ACCOUNT' then 1.2
                       else 1 
                       end) as rise_salary
                       from employees;

-- ��ø�Լ� ����ϱ�
-- �Լ�1(�Լ�2(�Լ�3))
-- step1
select add_months(hire_date, 6) from employees order by hire_date;
-- �Ի��� 6����
-- step2
select next_day(add_months(hire_date, 6),'��') from employees order by hire_date;
-- �Ի��� 6������ ���� �ݿ��� ��¥
-- step3
select to_char(next_day(add_months(hire_date, 6),'��'),'YYYY-MM-DD') from employees order by hire_date;
-- �Ի��� 6������ ���� �ݿ��� ��¥�� '��-��-��' ���ĺ���

-- Q] �Ի�⵵�� 2010�� ���ĸ� 10% �λ�, �Ի�⵵�� 2005�� ���ĸ� 5% �λ�, 2005�� �����̸� �λ� ����
--  �̸�, ����, �Ի�⵵, �Ի����, �����λ���� ����Ͻÿ�
select first_name, salary, to_char(hire_date,'YYYY"�� �Ի�"') as Year, to_char(hire_date,'DAY') as DAY,
        case when to_number(to_char(hire_date,'YY')) >= 10 
                then to_char(salary*1.1,'$999,999')
            when to_number(to_char(hire_date,'YY')) >= 5 
                then to_char(salary*1.05,'$999,999')
            else to_char(salary*1,'$999,999') 
            end
            from employees;

-- ���տ�����
-- UNION : �ΰ� �̻��� ���� ����� ��ġ�� ���� (������, �ߺ��Ǵ� ��� ������)
select employee_id, first_name from employees where hire_date like '04%'
union
select employee_id, first_name from employees where department_id=20;

-- UNION ALL (������, �ߺ��Ǵ� ��� ����)
select employee_id, first_name from employees where hire_date like '04%'
union all
select employee_id, first_name from employees where department_id=20;

-- INTERSECT (������)
select employee_id, first_name from employees where hire_date like '04%'
intersect
select employee_id, first_name from employees where department_id=20;

-- MINUS (������)
select employee_id, first_name from employees where hire_date like '04%'
minus
select employee_id, first_name from employees where department_id=20;

select employee_id, first_name from employees where department_id=20
minus
select employee_id, first_name from employees where hire_date like '04%';

