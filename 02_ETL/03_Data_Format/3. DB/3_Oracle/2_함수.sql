-- * 함수
-- -단일행 함수 : 단일 행에서만 적용 가능하고 행별로 하나의 결과를 리턴
-- -다중행 함수 : 복수 행을 조작하여 행의 그룹당 하나의 결과를 리턴(예: count())
-- > 단일행 함수 : 문자함수, 숫자함수, 날짜함수, 변환함수, 일반함수
--------------------------------------------------------------------------
-- 문자함수
--------------------------------------------------------------------------

-- dual 테이블 : 오라클 자체에서 값을 확인하려는 용도로 제공하는 테이블
select * from dual;

-- initcap : 단어를 기준으로 첫 문자만 대문자로 나머지는 소문자로 변환하는 함수
select initcap('python specialist') from dual;
select initcap('pythonSpecialist') from dual;
-- lower : 전체를 소문자로 만드는 함수
select lower('pythonSpecialist') from dual;
-- upper: 전체를 대문자로 만드는 함수
select upper('pythonSpecialist') from dual;

-- length : 문자열 길이수를 반환하는 함수
select length('pythonSpecialist') from dual;
select length('파이썬전문가') from dual;
-- 한글도 byte수가 아니라 글자수로 계산하여 길이를 반환한다

-- concat : 두 문자열을 연결하여 반환한다.
select concat('파이썬','전문가') from dual;

-- substr : substr(문자열,시작인덱스,끝인덱스)
-- 문자열을 기준으로 시작인덱스에서 끝 인덱스의 문자열을 반환한다.
-- (문자열의 시작인덱스는 1부터)
select substr('파이썬전문가',4,6) from dual;

-- instr : instr(문자열,찾고자하는 문자열)
-- 문자열을 기준으로 찾고자하는 문자열의 인덱스를 반환한다.
select instr('파이썬전문가','전') from dual;
select instr('파이썬전문가','정') from dual;
-- 매치가 되는 문자열이 없으면 0을 반환한다.

-- rpad/lpad(문자열,채울자리수,채울문자)
-- rpad/lpad: 주어진 자릿수만큼 오른쪽(rpad)/왼쪽(lpad)에 지정한 문자열을 채운다.
-- byte로 계산하므로 한글은 한글자에 두자리로 계산한다.
select rpad('홍길동',10,'*') from dual;
select lpad('홍길동',10,'*') from dual;
-- Q] 직원 테이블에서 이름 10자리중 나머지 오른쪽은 '-'으로 채우고
-- 급여 10자리중 나머지 왼쪽은 '*'로 채워서 출력하세요.
select rpad(first_name,10,'-') as name, lpad(salary,10,'*') salary from employees;

-- ltrim/rtrim/trim(문자열,제거할 문자열) 제거할 문자열 기본값은 공백문자
-- ltrim/rtrim : 문자열을 기준으로 제거할 문자를 각각 왼쪽,오른쪽으로 제거
-- trim(문자열)
-- trim : 문자열을 기준으로 공백문자를 양쪽으로 제거
select ltrim('    파이썬   전문가    ') as name from dual;
select ltrim('파이썬전문가파이썬','파이썬') name from dual;
select rtrim('    파이썬   전문가    ') name from dual;
select rtrim('파이썬 전문가 파이썬','파이썬') name from dual;
select trim(' 파이썬 전문가 파이썬 ') name from dual;
-- ltrim 심화
select ltrim('JavaSpecialist','Java') name from dual;
-- 제거할 문자열의 문자의 순서는 고려하지 않는다.
select ltrim('JavaSpecialist','Jav') name from dual;
-- 제거는 제거하지 못하는 문자를 최초 발견할 때까지 제거한다.
select ltrim('JavaSpecialist','avJ') name from dual;
select ltrim('JavaSpecialist','aJv') name from dual;

-- replace
select replace('Python Specialist','Python','bigdata') from dual;
select replace('Python Specialist',' ','') from dual;
-- 공백문자 제거한다.

-- translate(원본 문자열,매칭문자열,변환문자열)
select translate('1234abcd','abcd','ABC') from dual;
select translate('hello world!!!','hw','HW') from dual;
select translate('hello world!!!','!','?') from dual;
select translate('$100','$','') from dual;
-- 변환할 문자가 없다면 null 반환한다.
select translate('$100','$','￦') as m from dual;
select translate('$1,000,000','$,',' ') from dual;
-- 통화 기호 및 단위기호 제거하는 방법

-- Q] 직원 테이블에서 이름을 이름 그대로, 소문자로, 첫글자만 대문자로, 모두 대문자로 출력해보세요.
select first_name || ' ' || last_name, lower(first_name || ' ' || last_name),
initcap(first_name || ' ' || last_name), upper(first_name || ' ' || last_name) from employees;

-- Q] 직원테이블에서 이름이 'austin'인 직원의 이름을 이름그대로, 소문자로, 첫글자만 대문자로, 모두 대문자로 출력해보세요.
-- 검색을 소문자로 할 것
select last_name, lower(last_name), initcap(last_name), upper(last_name) 
from employees where lower(last_name) = 'austin';

-- Q] 직무아이디가 it_prog인 (반드시 소문자로 검색해야함) 사원의 이름 앞에 3자리만 출력하고 나머지자리는 *을 출력하며
-- salary는 전체 10자리 중 오른쪽 출력하고 나머지는 *을 출력한다.
select rpad(substr(first_name,1,3),length(first_name),'*'), lpad(salary,10,'*') from employees where lower(job_id) = 'it_prog';

--------------------------------------------------------------------------
-- 숫자함수
--------------------------------------------------------------------------
-- 반올림 : round
select round(45.966,2), round(45.966,0), round(45.966,-1) from dual;

-- 올림 : ceil (default는 소수점 첫자리)
select ceil(7.3) from dual;

-- 버림 : floor
select floor(7.3) from dual;

-- 절삭 : trunc(데이터,자리수) 자리수만큼 데이터의 값을 절삭
select trunc(45.923,2), trunc(45.923), trunc(45.923,-1) from dual;

-- to_date(날짜스트링,포멧)
select to_date('2022-12-20','YYYY-MM-DD') as dt from dual;

-- floor와 유사하나 trunc함수는 날짜타입에도 적용할 수 있다.
-- trunc함수를 응용하여 매월 첫째날을 구하기
select trunc(to_date('2022-12-20','YYYY-MM-DD'),'MM') as dt from dual;

-- Q] trunc함수를 응용하여 2022년 첫째날을 구하기
select trunc(to_date('2022-12-20','YYYY-MM-DD'),'YYYY') as dt from dual;
-- DD로 절삭하면 일단위로 절삭할 날짜가 없으므로 동일한 값을 반환
select trunc(to_date('2022-12-20','YYYY-MM-DD'),'DD') as dt from dual;
-- DAY로 절삭하면 그 주의 첫번째 일요일을 반환
select trunc(to_date('2022-12-31','YYYY-MM-DD'),'DAY') as dt from dual;

select trunc(to_date('2022-12-20','YYYY-MM-DD'),'WEEK') as dt from dual;

-- 절대값
select abs(-1000) abs from dual;

-- 제곱값
select power(2,3) power from dual;

-- 제곱근
select sqrt(100) sqrt from dual;

-- 나머지
select mod(10,3) mod from dual;

--------------------------------------------------------------------------
-- 날짜함수
--------------------------------------------------------------------------

-- SYSDATE : 현재의 날짜를 반환(YY/MM/DD)
select sysdate from dual;

-- SYSTIMESTAMP: 현재의 날짜와 시간을 반환
select systimestamp from dual;

-- Q] 부서번호가 60인 사원의 이름과 현재까지 근무한 주를 'Week' 열 이름으로 출력
select first_name, ceil((sysdate - hire_date)/7) as Weeks from employees where department_id = 60;
--select to_date(hire_date,'DD') from employees;

-- MONTHS_BETWEEN : 두 날자 사이의 월 수를 반환한다.
select first_name, sysdate, hire_date, ceil(months_between(sysdate, hire_date)) as workmonth from employees;

-- ADD_MONTHS : 기준일에 월을 더함
select first_name, hire_date, ADD_MONTHS(hire_date,1) from employees where first_name = 'Diana';

-- Q] 위 예제를 활용하여 Diana가 입하후 200개월이 지난 날짜를 구하세요.
select first_name, hire_date, ADD_MONTHS(hire_date,200) from employees where first_name = 'Diana';

-- NEXT_DAY : 돌아오는 가장 최근 요일 날짜
select sysdate, next_day(sysdate,'월') from dual;
select sysdate, next_day(sysdate,'금') from dual;

-- select sysdate, next_day(sysdate,'M') from dual;

-- LASR_DAY : 해당 날이 포함된 월의 마지막 날짜
select sysdate, last_day(sysdate) from dual;

-- Q] 1월부터 12월까지 마지막날을 출력하세요.
select TO_CHAR(last_day('22/01/01'),'dd') AS "1", TO_CHAR(last_day('22/02/01'),'dd') as "2", TO_CHAR(last_day('22/03/01'),'dd') AS "3", TO_CHAR(last_day('22/04/01'),'dd') AS "4",
TO_CHAR(last_day('22/05/01'),'dd') AS "5", TO_CHAR(last_day('22/06/01'),'dd') AS "6", TO_CHAR(last_day('22/07/01'),'dd') AS "7", TO_CHAR(last_day('22/08/01'),'dd') AS "8",
TO_CHAR(last_day('22/09/01'),'dd') AS "9", TO_CHAR(last_day('22/10/01'),'dd') AS "10", TO_CHAR(last_day('22/11/01'),'dd') AS "11", TO_CHAR(last_day('22/12/01'),'dd') AS "12" from dual;

select last_day('22/05/01') as "12" from dual;
select TO_CHAR(to_date('22/05/31'),'dd')  as "12" from dual;