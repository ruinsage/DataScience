------------------------------------------------------------------------------
--   그룹 함수를 이용한 데이터 집계
------------------------------------------------------------------------------

-- COUNT, SUM, AVG, MIN, MAX, VARIANCE, STDDEV
-- (salary)
select COUNT(salary) count, SUM(salary) sum, round(AVG(salary)), MIN(salary) MIN,
MAX(salary) MAX, round(VARIANCE(salary)) VARIANCE, round(STDDEV(salary)) STDDEV from employees;

SELECT min(hire_date), max(hire_date) from employees;

SELECT min(first_name), max(first_name) from employees;

-- Q] 가장 큰 급여액은?
select max(salary) from employees;

-- Q] 사원들의 급여의 총합, 평균, 표준편차, 분산을 구하세요.
select sum(salary) sum, round(avg(salary),2) avg,
round(variance(salary),2) variance, round(stddev(salary),2) stddev
from employees;

-- 평균함수 사용시 주의할 점
select commission_pct  from employees;
select round( sum(salary*commission_pct),2) sum_bonus,
       round( sum(salary*commission_pct)/count(*),2) avg_bonus1,
       -- sum함수를 사용한 인상분의 평균 count 함수는 null값도 센다
       round( avg(salary*commission_pct),2) avg_bonus2
       -- avg함수를 사용한 인상분의 평균 avg함수는 null값은 제외한다.
       from employees;

-- GROUP BY
select department_id from employees group by department_id;

-- GROUP BY와 집계 함수 응용
select department_id, round(avg(salary),2) avg from employees group by department_id;

-- 하나 이상의 열로 그룹화 하기
-- select/group by에 지정하는 열 이름이 일치해야 한다.
select department_id, job_id, round(avg(salary),2) avg  from employees 
group by department_id, job_id order by department_id desc;

-- 그룹 함수를 잘못 하용한 경우
-- 개별적인 열과 그룹함수를 혼합해서 사용할 때에는 개별적인 열을 명시하는
-- group by절을 반드시 포함해야 한다.
select department_id, count(first_name) from employees;

select department_id, count(first_name) from employees group by department_id;


-- group by 순서

-- select
-- from
-- where
-- group by <- 이 위치에서 사용
-- having
-- order by

-- having : group by한 결과를 필터링 할 때 사용한다.

select department_id, round(avg(salary),2) from employees 
group by department_id having avg(salary) >= 8000;

select job_id, avg(salary) payroll from employees
where job_id not like 'SA%' group by job_id having avg(salary) > 8000
order by payroll;

-- grouping set : 복수개의 그룹셋을 유연하게 처리, union all의 기능을 대체
select to_char(department_id), round(avg(salary),2) from employees
group by department_id;

select job_id, round(avg(salary),2) from employees group by job_id;

-- 열의 이름이 grouping한 대상과 일치하지는 않는다.
select to_char(department_id), round(avg(salary),2) from employees
group by department_id
union all
select job_id, round(avg(salary),2) from employees group by job_id;

-- 위 결과를 grouping sets 함수를 통해 구현
select department_id, job_id, round(avg(salary),2) from employees
group by grouping sets (department_id, job_id) order by department_id, job_id;

-- grouping set 확장
-- groupin set ((그룹셋1),(그룹셋2)...)
select department_id, job_id, manager_id, round(avg(salary),2) from employees
group by grouping sets ((department_id, job_id),(job_id, manager_id)) 
order by department_id, job_id, manager_id;

-- ROLLUP, CUBE
-- 부서별, 직무별 급여의 평균과 사원의 수를 출력하라.
select department_id, job_id, round(avg(salary),2), count(*) from employees
group by (department_id, job_id) order by department_id, job_id;

select department_id 부서코드, NVL(job_id, '부서평균') 직군과부서, round(avg(salary),2) 평균, count(*) 부서인원 from employees
group by rollup (department_id, job_id) order by department_id, job_id;
-- ROLLUP은 레벨별 집계가 가능하다. 마지막 행은 전체에대한 계산결과를 출력한다.

select count() from employees;