------------------------------------------------------------------------------
-- �м��Լ� : ������ �м��� ���� �پ��� ����� �����Ѵ�.
------------------------------------------------------------------------------
-- RANK : ������ �켱������ ���� (�ߺ����� �����)
-- DENSE_RANK : ������ �켱������ ���� (�ߺ����� ��� ����)
-- CUME_DIST : �ִ밪 1�� �������� �л�� ���� ����
-- PERCENT_RANK : �ִ밪 1�� �������� �����(Persent)���� ����
-- ù��° ��ġ�� 0���� �����ϰ� �ι�° row���� ��ġ��
-- (Row�� rank-1 / (��ü row ���� -1)
-- rank�� �������� ������ rank�� ������ ��ü ��� �� %������ �ؼ�
-- ROW_NUMBER : �˻� ����� ���� ���������� �ο��Ǵ� ���ȣ�� ����
-- NTILE (n) : ��ü �����͸� n������ ������ n���� ���� �����Ѵ�.
-- ����
-- �м��Լ�() over(order by)   <-- order by�� �ɼ�

select first_name, salary, 
      RANK() over(order by salary desc) as RANK,
      DENSE_RANK() over(order by salary desc) as DENSE_RANK,
round(CUME_DIST() over(order by salary desc),5) as CUME_DIST,
round(PERCENT_RANK() over(order by salary desc),5) as PERCENT_RANK,
      NTILE(4) over(order by salary desc) as NTILE,
      ROWNUM, -- �ǻ翭(���� ���̺� �ο��� ���ȣ) �� �Է��� ����
      ROW_NUMBER() over(order by salary desc) as ROW_NUMBER
from employees;

-- RATIO_TO_REPORT
-- ��ȸ�ϴ� ���� �ش� �÷� ���� ������� ����
-- ��) ����
--      30 <- 0.3
--      50 <- 0.5
--      20 <- 0.2
select first_name, salary, round(ratio_to_report(salary) over (), 4) as salary_ratio
from employees;
-- where job_id = 'IT_PROG';

-- LAG / LEAD (����/���� ���� ���� �˻�)
-- LAG(���̸�, ���� �̵���, ���� ���� ��� ��ȯ��)
-- LEAD(���̸�, ���� �̵���, ���� ���� ��� ��ȯ��)
select employee_id, lag(salary, 1, 0) over (order by salary) as lower_sal,
salary, lead(salary, 1, 0) over (order by salary) as higer_sal
from employees order by salary;
-- ���� ���̵�, ���� �޿� �������� ���� �޿�, ���� �޿�, ���� �޿� �������� ���� �޿�

-- LISTAGG
-- LISTAGG(�� �Ǵ� ����,������)
--      WITHIN GROUP(ORDER BY ���̸�)
-- ��� : �����Ǵ� ���� �����ڷ� JOIN(����)

select department_id, 
listagg(first_name, ',') within group (order by hire_date) as names
from employees GROUP BY department_id;

-- PIVOT, UNPIVOT
CREATE TABLE   sales_log(
  employee_id  NUMBER(6),
  week_id      NUMBER(2),
  week_day     VARCHAR2(10),
  quantity     NUMBER(8,2)
); 

INSERT INTO sales_log values(1101, 4, 'SALES_MON', 100);
INSERT INTO sales_log values(1101, 4, 'SALES_TUE', 150);
INSERT INTO sales_log values(1101, 4, 'SALES_WED', 80);
INSERT INTO sales_log values(1101, 4, 'SALES_THU', 60);
INSERT INTO sales_log values(1101, 4, 'SALES_FRI', 120);
INSERT INTO sales_log values(1102, 5, 'SALES_MON', 300);
INSERT INTO sales_log values(1102, 5, 'SALES_TUE', 300);
INSERT INTO sales_log values(1102, 5, 'SALES_WED', 230);
INSERT INTO sales_log values(1102, 5, 'SALES_THU', 120);
INSERT INTO sales_log values(1102, 5, 'SALES_FRI', 150);
COMMIT;
SELECT * FROM sales_log;

-- PIVOT : ������ ������ �������� �����͸� ������ �Ӽ����� ���� ����(���, �հ��)�ϰ�
-- ���� ��Ÿ����.
-- �α׼� ������(Long ����)�� �м��� ������(Wide ����)�� ��ȯ�ϴ� ����
-- ����
-- SELECT
-- FROM
-- PIVOT(
--       �׷��Լ�(�������÷�)
--       for �ǹ������÷�
--       in �ǹ��÷� ����
-- )
-- WHERE
-- ORDER BY
select * from sales_log
pivot(
        sum(quantity)
        for week_day in ('SALES_MON' as sales_mon,
                         'SALES_TUE' as sales_tue,
                         'SALES_WED' as sales_wed,
                         'SALES_THU' as sales_thu,
                         'SALES_FRI' as sales_fri)
        )
order by employee_id, week_id;

select rownum from sales_log order by sales_log.quantity;

select  department_id, sum(salary)  from employees group by department_id order by department_id;

select * from employees 
pivot (
        sum(salary)
        for department_id in( '10' as id_10,
                            '20' as id_20,
                            '30' as id_30,
                            '40' as id_40,
                            '50' as id_50,
                            '60' as id_60,
                            '70' as id_70,
                            '80' as id_80,
                            '90' as id_90,
                            '100' as id_100,
                            '110' as id_110
                            )
      )
;
                              
                              
                              


CREATE TABLE sales(
  employee_id  NUMBER(6),
  week_id      NUMBER(2),
  sales_mon    NUMBER(8,2),
  sales_tue    NUMBER(8,2),
  sales_wed    NUMBER(8,2),
  sales_thu    NUMBER(8,2),
  sales_fri    NUMBER(8,2)
);

INSERT INTO sales VALUES(1101, 4, 100, 150, 80,  60,  120);
INSERT INTO sales VALUES(1102, 5, 300, 300, 230, 120, 150);
COMMIT;

SELECT * FROM sales;

-- UNPIVOT : �������� ���� ������ �������� �����͸� ������ ���� ����(Stack) ����
-- ���� �Ӽ��� ���� �Ӽ����� ��ȯ�ϴ� ����
-- ����
-- SELECT
-- FROM
-- UNPIVOT(
--          ������ ���� �̸� : ���� �������� ���� ��Ÿ���� �̸�
--          for ������ ���� �̸� : ���� �����Ϳ��� ������ ���� ���� Ư���� ��Ÿ���� �̸�
--          in (���ص������� ���մ��1, ���ص������� ���մ��2,.....)
--        )
-- where
-- order by
select employee_id, week_id, week_day, quantity
from sales unpivot(
                   quantity
                   for week_day
                   in(sales_mon, sales_tue, sales_wed, sales_thu, sales_fri)
                    );
                    
select * from sales_log;                
SELECT * FROM sales;