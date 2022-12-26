-- 급여의 편차가 가장 작은 부서의 번호를 출력하세요.

select department_id from (
select nvl(department_id,0) department_id, STDDEV(salary) stdd from employees group by department_id order by department_id)
where stdd = min(stdd);

min(STDDEV(salary))
select department_id, salary from employees group by department_id, salary order by department_id;



-- 103번 사원의 이름과 매니저의 이름을 출력하세요.
-- 사원의 정보는 employees, 매니저 정보는... employees에 있음
-- 같은 테이블에서 조인을 셀프조인이라고 합니다.
-- 테이블 별칭이 반드시 필요함
-- 열을 지정할 때 별칭을 이용해서 지정
select e.first_name, m.first_name from employees e
join employees m
on m.employee_id = e.manager_id
where e.employee_id = 103;

-- 60번 부서가 있는 지역의 우편번호를 출력하세요.
select * from departments where department_id = 60;
select * from locations where location_id = 1400;


-- 급여를 가장 많이 받이 받는 사람의 이름은?