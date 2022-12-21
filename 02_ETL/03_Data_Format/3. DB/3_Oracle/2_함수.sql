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
select TO_CHAR(to_date('22/05/31'),'yyyy-mm-dd')  as "12" from dual;

-------------------------------------------------------------------------------
-- 변환 함수
-------------------------------------------------------------------------------
-- 암시적 형 변환
-- number <-> character <-> date

select first_name from employees where department_id = 40; 
-- 40은 숫자타입

select first_name from employees where department_id = '40'; 
-- 40은 문자타입이비만 암시적 형변환이 일이난다.

select first_name from employees where hire_date = '03/06/17';
-- 03/06/17 문자타입이지만 암시적 형 변환이 일어난다.

select '5500.00' - 4000 from dual;
-- 하지만 서식이 들어간 데이터는 암묵적 형 변환이 되지 않는다.
select '$5,500.00' - 4000 from dual;
select first_name from employees where hire_date = '03년 06월 17일';

-- 명시적 형변환
-- TO_CHAR : 문자(날짜)열에 날짜포멧을 적용하여 문자로 변환, TO_CHAR(날짜,날짜포멧)
select first_name, to_char(hire_date,'YYYY"년" MM"월" DD"일"') as HiredMonth from employees
where first_name = 'Steven';

-- TO_CHAR: 문자(숫자)열에 숫자포멧을 적용하여 문자로 변환, TO_CHAR(숫자,숫자포멧)
-- ex)$999,999 <- 숫자는 9로 표시
-- 포멧보다 변환 길이가 큰 경우에는 '#'으로 표기
select to_char(2000000,'$999,999') salary from dual;
select to_char(2000000,'$9,999,999') salary from dual;

-- 앞에 0으로 padding하고 싶은 경우 -> 목표금액의 자리수를 고려하여 표현하고 싶은 경우
select to_char(2000000,'$009,999,999') salary from dual;

-- 소수점 이하 자리에 대한 포멧이 없다면 그 값은 삭제된다.
select to_char(2000000.45,'$009,999,999') salary from dual;
-- 소수점 처리
select to_char(2000000.45,'$009,999,999.99') salary from dual;
-- 지역국가화폐 기호 사용 (기호'L' 사용)
select to_char(2000000.45,'L9,999,999') salary from dual;

-- Q] 직원 테이블에 이름이 David인 이름, 성, 급여, 15% 인상분 금액을 salary1열에
-- 15.23% 인상분 금액은 다음과 같은 형식($1,446,85)을 적용하여 출력하시오
select first_name, last_name, salary, salary*0.15 salary1,
to_char(salary *0.1523,'$99,999.99') as salary2 from employees where first_name = 'David';

-- 원하는 날짜 포멧으로 검색하기 (to_date: 문자를 날짜 타입으로 변경)
select first_name, hire_date from employees where hire_date = To_date('2003/06/17','YYYY/MM/DD');
-- Q] '2003년 06월 17일'에 입사한 직원이름, 입사일을 출력하세요.
select first_name, hire_date from employees where hire_date = To_date('2003년 06월 17일','YYYY"년"MM"월"DD"일"');
-- Q] 날짜 타입이 아래와 같이 출력되도록 '03/06/17'에 입사한 직원의 직원이름, 입사일을  출력하세요.
-- '2003-06-17'
select first_name, To_char(hire_date,'YYYY-MM-DD') from employees where hire_dat = '03/06/17';

-- NULL 변환
-- NVL
-- NVL(원본값,널이면 변환되는 값) <= 원본 값이 널이 아니면 원본값을 반환한다.
select nvl(1000,100) from dual;
select nvl(null,100) from dual;

select commission_pct from employees;
select first_name, salary, commission_pct, salary+salary*commission_pct as 인상된_총급여
from employees;

-- Q] 위 예제를 NVL 함수를 사용하여 인상된 총급여액이 NULL이 나오지 않도록 변경하세요.
select first_name, salary, commission_pct, salary+salary*nvl(commission_pct,0) as 인상된_총급여
from employees;

-- NVL2(원본값,널이 아니면 변환되는 값, 널이면 변환되는 값)
select nvl2(0.2, 1000*0.2, 0) from dual;
select nvl2(null, 1000*0.2, 0) from dual;

-- Q] 위 예제를 NVL2함수를 이용하여 풀어보세요.
select first_name, salary, commission_pct, salary+nvl2(salary * commission_pct,salary,0) as 인상된_총급여
from employees;

-- COALESCE(값 또는 구문1, 값 또는 구문2) : 널이 아닌 첫번째 인자의 값을 선택
-- 예) 고객 데이터베이스에서 연락 가능한 번호를 추출하고자 할 때
-- 선택가능한 값(휴대폰, 집전화, 회사번호)중 널이 아닌 값을 추출하고자 할 때 유용하다.
select coalesce('010-123-4567',null,null) from dual;
select coalesce(null,'070-123-4567',null) from dual;
select coalesce(null,null,'02-123-4567') from dual;

-- Q] 위 예제를 coalesce함수를 이용하여 풀어보세요.
select first_name, salary, commission_pct,
coalesce(salary + salary*commission_pct,salary) as 인상된_총급여 from employees;

-- Q] 보너스가 650달러보다 작거나 보너스가 없는 사원들에게 상품권을 지급하려고 합니다.
-- 해당 사원들의 이름과 보너스를 출력하세요. (coalesce 함수 사용할 것)
select first_name, replace(coalesce(salary*commission_pct,0),0,'gift card') bonus 
from employees where coalesce(salary*commission_pct,0) < 650 ;

-- LNNVL: LNNVL(구문) 구문의 결과가 FALSE 또는 UNKKNOWN이면 TRUE를 반환
-- 조건의 반대 경우에 대해 검색하고 싶을 때 활용
select first_name, replace(coalesce(salary*commission_pct,0),0,'gift card') bonus 
from employees where LNNVL(salary*commission_pct >= 650) ;

-- DECODE : DECODE(Column or expression, serch1, result1
--                                       serch2, result2,....)
-- 열 혹은 표현식이 serch 값과 같으면 result 값을 반환해 준다.
select decode('java','java','백엔드 언어') as language from dual;
select decode('java','java','백엔드 언어'
                    ,'html','프론트 언어'
                    ,'python','데이터사이언스 언어'
            ) as language from dual;
select decode('html','java','백엔드 언어','html','프론트 언어','python','데이터사이언스 언어') as language from dual;
select decode('java','java','백엔드 언어'
                    ,'html','프론트 언어'
                    ,'python','데이터사이언스 언어'
            ) as language from dual;
select decode('css','java','백엔드 언어'
                    ,'html','프론트 언어'
                    ,'python','데이터사이언스 언어'
                    ,'기타언어'  -- 디폴트 search 값
            ) as language from dual;

-- Q] 직원 테이블에서 직무 ID, 급여, 그리고 '급여인상율'을 출력한다.
-- 급여인상율은 직무 ID가 IT_PROG, FI_MGR, FI_ACCOUNT에 따라 각각 10,15,20% 인상율을 적용한다.
-- decode 사용할 것
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
-- 개별 조건 적용시
select job_id, salary, 
    floor(salary* case when job_id = 'IT_PROG' then 1.1
                       when job_id = 'FI_MGR' then 1.15
                       when job_id = 'FI_ACCOUNT' then 1.2
                       else 1 
                       end) as rise_salary
                       from employees;

-- 중첩함수 사용하기
-- 함수1(함수2(함수3))
-- step1
select add_months(hire_date, 6) from employees order by hire_date;
-- 입사후 6개월
-- step2
select next_day(add_months(hire_date, 6),'금') from employees order by hire_date;
-- 입사후 6개월인 주의 금요일 날짜
-- step3
select to_char(next_day(add_months(hire_date, 6),'금'),'YYYY-MM-DD') from employees order by hire_date;
-- 입사후 6개월인 주의 금요일 날짜를 '년-월-일' 형식변경

-- Q] 입사년도가 2010년 이후면 10% 인상, 입사년도가 2005년 이후면 5% 인상, 2005년 이전이면 인상 없음
--  이름, 연봉, 입사년도, 입사요일, 연봉인상액을 출력하시오
select first_name, salary, to_char(hire_date,'YYYY"년 입사"') as Year, to_char(hire_date,'DAY') as DAY,
        case when to_number(to_char(hire_date,'YY')) >= 10 
                then to_char(salary*1.1,'$999,999')
            when to_number(to_char(hire_date,'YY')) >= 5 
                then to_char(salary*1.05,'$999,999')
            else to_char(salary*1,'$999,999') 
            end
            from employees;

-- 집합연산자
-- UNION : 두개 이상의 질의 결과를 합치는 연산 (합집합, 중복되는 결과 미포함)
select employee_id, first_name from employees where hire_date like '04%'
union
select employee_id, first_name from employees where department_id=20;

-- UNION ALL (합집합, 중복되는 결과 포함)
select employee_id, first_name from employees where hire_date like '04%'
union all
select employee_id, first_name from employees where department_id=20;

-- INTERSECT (교집합)
select employee_id, first_name from employees where hire_date like '04%'
intersect
select employee_id, first_name from employees where department_id=20;

-- MINUS (차집합)
select employee_id, first_name from employees where hire_date like '04%'
minus
select employee_id, first_name from employees where department_id=20;

select employee_id, first_name from employees where department_id=20
minus
select employee_id, first_name from employees where hire_date like '04%';

