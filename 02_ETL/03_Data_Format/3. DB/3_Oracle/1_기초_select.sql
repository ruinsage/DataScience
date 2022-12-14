-- 주석 : 첫번째 SQL문
--SELECT * from employees;

-- 컬럼 및 기본 정보 조회
-- 테이블 이름은 '대문자'로 입력할 것
SELECT * from cols where table_name = 'employees';

SELECT * from cols where table_name = 'EMPLOYEES';

-- 현재 오라클 버전 정보
SELECT * FROM v$version;

-- 접속한 계정에서 테이블 목록 조회
SELECT * FROM TABS;

-- select (Projection => 열 선택)
select first_name, last_name, salary from employees;

-- date 타입은 YY/MM/DD 형식으로 보여줌 (Default는 DD/MM/YY)
-- SQL Developer에서 현지 date타입으로 변경해서 보여주므로 YY/MM/DD로 표현됨
select first_name, last_name, hire_date, salary from employees;

-- 연산자 우선순위
-- 0.1은 급여 인상비율, salary*0.1: 인상된 급여
select first_name, last_name,salary, salary+salary*0.1 from employees;

-- 미정의 값, Null 표시
select first_name, department_id, commission_pct from employees;

-- 열 별칭 (alias) 정의
select first_name as 이름, salary as 급여 from employees;
-- 응용 프로그램에서 열 이름을 인식하기 위한 용도로 반드시 열 별칭을 사용해야 한다.
select first_name, last_name,salary, salary+salary*0.1 as 급여인상분 from employees;
-- 가능하면 영문 별칭 사용을 권장한다.
select first_name, last_name,salary, salary+salary*0.1 as raise_income from employees;

-- 리터럴(literal) 문자 스트링과 연결 연산자
select first_name || ' ' || last_name || '''s salary is $' || salary as "사원 상세정보" from employees;

-- 중복 행과 DISTINCT
select department_id from employees;
select distinct department_id from employees;

-- ROWNUM, ROWID 의사열(Pseudo column)
-- 오라클에서는 행의 인덱스는 1부터 시작한다.
-- rowid : 유일값으로 생성, 행에 유일하게 접근 가능한 키 (PK로도 활용 가능)
-- rownum : 검색 결과에 대하여 1부터 값을 부여한다.
select employee_id, first_name from employees;
select rowid, rownum, employee_id, first_name from employees;

-- 행의 제한 (Selection) : where 구문에서 지정
select first_name, last_name, hire_date from employees
where last_name = 'King';

-- 비교 연산자
select first_name, salary, hire_date from employees
where salary >= 15000;

-- 날짜 비교
select first_name, salary, hire_date from employees
WHERE hire_date = '04/01/30';  -- 암묵적 형변환이 일어났기 때문에 가능

-- between 연산자 ( between 시작조건 and 끝조건) 시작조건, 끝조건 포함
select first_name, salary from employees
where salary between 10000 and 12000;

-- In 연산자
select manager_id from employees;
-- Q] 직원 테이블에서 manager_id가 101,102,103인 직원 id,이름,급여,매니쳐id를 출력하세요
select employee_id, first_name, salary, manager_id from employees
where manager_id in ('101', '102', '103');

-- like 연산자
-- % 기호 활용

select job_id from employees;

select first_name, last_name, job_id, department_id from employees
where job_id like 'IT%';

-- Q] 2003년 1월 1일부터 2003년 12월 31일 사이에 입사한 모든 사원의 이름과 입사일
select first_name, hire_date from employees
where hire_date between '03/01/01' and '03/12/31';

select first_name, hire_date from employees
where hire_date like '03%';

-- '_'기호 활용 : '_'는 임의의 한 글자와 매칭된다
-- 이메일의 두 번째 문자가 'A'인 모든 사원의 이름과 이메일을 출력
select first_name, email from employees
where email like '_A%';

-- IS NULL 연산자 : null인 값을 찾을 때
select first_name, manager_id from employees
where manager_id is null;

-- 논리 연산자
-- and 연산
-- Q] 직무 id가 IT_PROG이고 급여가 5000 이상인 직원의 이름, 직무 id, 급여를 출력하시오.
select first_name, job_id, salary from employees
where job_id = 'IT_PROG' and salary >= 5000;

-- or 연산
-- Q] 직무 id가 IT_PROG이거나 급여가 5000 이상인 직원의 이름, 직무 id, 급여를 출력하시오.
select first_name, job_id, salary from employees
where job_id = 'IT_PROG' or salary >= 5000;

-- Q] 직무 아이디가 'IT_PROG' 또는 'FI_MGR' 이고 급여가 6000이상인 직원의 이름, 직무 id, 급여를 출력하세요.
-- 오라클에서 and 연산자의 우선순위가 or 연산자 보다높다.
-- 따라서 의미를 분명하게 하기 위해서 () 연산자를 활용할 것
select first_name, job_id, salary from employees
where (job_id = 'IT_PROG' or job_id = 'FI_MGR') and salary >= 6000;

-- 데이터 정렬
-- oder by (기본은 오름차순 정렬)
-- select * from * where * order by <- 이 위치에서 사용
select first_name, hire_date from employees order by hire_date;

select first_name, hire_date from employees order by hire_date asc;
-- 명시적으로 오름차순임을 지정

-- 내림차순 정렬 (desc)
select first_name, hire_date from employees order by hire_date desc;

-- 열 별칭 응용
select first_name, salary from employees order by salary;

select first_name, salary*1.2 from employees order by salary*1.2;
-- <- salary*1.2 : 급여의 20% 인상이 반영된 금액

select first_name, salary*1.2 as increas_salary from employees order by increas_salary;

