2. 사원의 이름, 급여, 연간 총 수입을 총 수입이 많은 것부터 작은 순으로 출력하시오, 
연간 총수입은 월급에 12를 곱한 후 $100의 상여금을 더해서 계산하시오.

select first_name as 이름, salary as 급여, salary*12+100 as 연간_총_수입 from employees
order by 연간_총_수입 desc;

3. 급여가 2000을 넘는 사원의 이름과 급여를 표현, 급여가 많은 것부터 작은 순으로
출력하시오.

select first_name 이름, salary 급여 from employees where salary >= 2000
order by salary desc;

4. 사원번호가 203인 사원의 이름과 부서번호를 출력하시오.

select first_name, department_id from employees where EMPLOYEE_ID = '203';

5. 급여가 2000에서 3000 사이에 포함되지 않는 사원의 이름과 급여를 출력하시오.

select first_name, salary from employees where salary not between 2000 and 3000;

6. 2005년 3월 20일 부터 2005년 8월 1일 사이에 입사한 사원의 이름, 담당업무, 입사일을
출력하시오.

select first_name, job_id, hire_date from employees 
where hire_date between '05/03/20' and '05/08/01' order by hire_date;

7. 부서번호가 20 및 30에 속한 사원의 이름과 부서번호를 출력,
이름을 기준(내림차순)으로 영문자순으로 출력하시오.

select first_name, department_id from employees
where department_id = 20 or department_id = 30 order by first_name desc;

8. 사원의 급여가 2000에서 3000사이에 포함되고 부서번호가 20 또는 30인 사원의
이름, 급여와 부서번호를 출력, 이름순(오름차순)으로 출력하시오.

select first_name 이름, salary 급여, department_id 부서번호 from employees
where salary >= 2000 and salary <= 3000 and department_id = 20 or department_id = 30
order by first_name;

9. 2006년도에 입사한 사원의 이름과 입사일을 출력하시오.
-- (like 연산자와 와일드카드 사용)

select first_name, hire_date from employees where hire_date like '06%';

10. 관리자가 없는 사원의 이름과 담당 업무를 출력하시오.

select first_name name, job_id job from employees where manager_id is null;

11. 커미션을 받을 수 있는 자격이 되는 사원의 이름, 급여, 커미션을 출력하되
급여 및 커미션을 기준으로 내림차순 정렬하여 표시하시오.

select first_name name, salary, commission_pct commission from employees
where commission_pct is not null order by commission_pct desc;

12. 이름의 세번째 문자가 R인 사원의 이름을 표시하시오.

select first_name name from employees where first_name like '__r%';

13. 이름에 A와 E를 모두 포함하고 있는 사원의 이름을 표시하시오.

select first_name name from employees
where first_name like '%A%' or first_name like '%E%';

14. 담당업무가 CLERK, 또는 SALESMAN이면서 급여가 $1600, $950 또는 $1300이 아닌 사원의
이름, 담당업무, 급여를 출력하시오.

select first_name name, job_id job, salary from employees
where job_id like '%CLERK%' or job_id = 'SA_MAN';

15. 커미션이 $500 이상인 사원의 이름과 급여 및 커미션을 출력하시오.

select first_name name, salary, commission_pct*salary as com from employees
where comt*salary >= '500';

16. SUBSTR 함수를 사용하여 사원들의 입사한 년도와 입사한 달만 출력하시오.

select substr(hire_date,1,2) year, substr(hire_date,4,2) month from employees;










 
