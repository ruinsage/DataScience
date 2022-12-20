select * from employees;

17. SUBSTR 함수를 사용하여 4월에 입사한 사원을 출력하시오.

select first_name, hire_date from employees where substr(hire_date,4,2) = '04';

18. MOD 함수를 사용하여 사원번호가 짝수인 사람만 출력하시오.
select first_name name, employee_id id from employees where mod(employee_id,2) = 0;

19. 입사일을 년도는 2자리(YY), 월은 숫자(MON)로 표시하고 요일은 약어 (DY)로 지정하여 출력하시오.
select to_char(hire_date,'YY') as YY, to_char(hire_date,'MON') as MON, to_char(hire_date,'DY') as DAY  from employees;

20. 올해 몇 칠이 지났는지 출력하시오. 현재날짜에서 올해 1월 1일을 뺀 결과를 출력하고
TO_DATE 함수를 사용하여 데이터 형을 일치 시키시오.
select round(sysdate - to_date('22/01/01')) as 올해날짜 from dual;

21. 사원들의 상관 사번을 출력하되 상관이 없는 사원에 대해서는 NULL 값 대신 0으로 출력하시오.

select NVL(manager_id,0) from employees;
-- 오라클에서는 NVL
-- select ifnull(manager_id,0) from employees; mysql에서는 ifnull 

23. 모든 사원의 급여 최고액, 최저액, 총액 및 평균 급여를 출력하시오. 평균에 대해서는 정수로 반올림하시오.
[출처] [SQL] 연습문제 (59문제) 풀이|작성자 하범핀

24. 각 담당 업무 유형별로 급여 최고액, 최저액, 총액 및 평균 액을 출력하시오. 평균에 대해서는 정수로 반올림 하시오.
[출처] [SQL] 연습문제 (59문제) 풀이|작성자 하범핀

25. COUNT(*) 함수를 이용하여 담당업무가 동일한 사원 수를 출력하시오.
[출처] [SQL] 연습문제 (59문제) 풀이|작성자 하범핀

26. 관리자 수를 나열하시오.
[출처] [SQL] 연습문제 (59문제) 풀이|작성자 하범핀




