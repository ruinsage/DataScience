------------------------------------------------------------------------------
-- 분석함수 : 데이터 분석을 위한 다양한 기능을 제공한다.
------------------------------------------------------------------------------
-- RANK : 데이터 우선순위를 결정 (중복순위 계산함)
-- DENSE_RANK : 데이터 우선순위를 결정 (중복순위 계산 안함)
-- CUME_DIST : 최대값 1을 기준으로 분산된 값을 제공
-- PERCENT_RANK : 최대값 1을 기준으로 백분율(Persent)값을 제공
-- 첫번째 위치가 0부터 시작하고 두번째 row부터 위치는
-- (Row의 rank-1 / (전체 row 개수 -1)
-- rank를 기준으로 동일한 rank의 개수가 전체 대비 몇 %인지로 해석
-- ROW_NUMBER : 검색 결과에 따라 순차적으로 부여되는 행번호를 제공
-- NTILE (n) : 전체 데이터를 n분위로 나누어 n분위 값을 제공한다.
-- 문법
-- 분석함수() over(order by)   <-- order by는 옵션

select first_name, salary, 
      RANK() over(order by salary desc) as RANK,
      DENSE_RANK() over(order by salary desc) as DENSE_RANK,
round(CUME_DIST() over(order by salary desc),5) as CUME_DIST,
round(PERCENT_RANK() over(order by salary desc),5) as PERCENT_RANK,
      NTILE(4) over(order by salary desc) as NTILE,
      ROWNUM, -- 의사열(최초 테이블에 부여된 행번호) 즉 입력한 순서
      ROW_NUMBER() over(order by salary desc) as ROW_NUMBER
from employees;

-- RATIO_TO_REPORT
-- 조회하는 값을 해당 컬럼 값의 백분율로 제공
-- 예) 매출
--      30 <- 0.3
--      50 <- 0.5
--      20 <- 0.2
select first_name, salary, round(ratio_to_report(salary) over (), 4) as salary_ratio
from employees;
-- where job_id = 'IT_PROG';

-- LAG / LEAD (이전/이후 값에 대한 검색)
-- LAG(열이름, 이전 이동수, 값이 없을 경우 반환값)
-- LEAD(열이름, 이후 이동수, 값이 없을 경우 반환값)
select employee_id, lag(salary, 1, 0) over (order by salary) as lower_sal,
salary, lead(salary, 1, 0) over (order by salary) as higer_sal
from employees order by salary;
-- 직원 아이디, 현재 급여 다음으로 적은 급여, 현재 급여, 현재 급여 다음으로 높은 급여

-- LISTAGG
-- LISTAGG(값 또는 구문,구분자)
--      WITHIN GROUP(ORDER BY 열이름)
-- 기능 : 수집되는 값을 구분자로 JOIN(연결)

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

-- PIVOT : 행으로 나열된 여러개의 데이터를 공통의 속성으로 묶어 집계(평균, 합계등)하고
-- 열로 나타낸다.
-- 로그성 데이터(Long 포멧)을 분석용 데이터(Wide 포멧)로 전환하는 과정
-- 문법
-- SELECT
-- FROM
-- PIVOT(
--       그룹함수(집계대상컬럼)
--       for 피벗기준컬럼
--       in 피벗컬럼 나열
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

-- UNPIVOT : 여러개의 열로 나열된 여러개의 데이터를 공통의 열로 묶어(Stack) 나열
-- 복합 속성을 단일 속성으로 전환하는 과정
-- 형식
-- SELECT
-- FROM
-- UNPIVOT(
--          통합할 열의 이름 : 기준 데이터의 값을 나타내는 이름
--          for 통합할 열의 이름 : 기준 데이터에서 나열된 열의 공통 특성을 나타내는 이름
--          in (기준데이터의 통합대상열1, 기준데이터의 통합대상열2,.....)
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