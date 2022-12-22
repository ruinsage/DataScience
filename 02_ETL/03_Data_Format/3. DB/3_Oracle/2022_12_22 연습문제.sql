-- Q] sales_log 테이블을 피벗해보자
select * from sales_log;

select * from sales_log
pivot(
        sum(quantity)
        for week_day
        in ('SALES_MON' as sales_mon,
            'SALES_TUE' as sales_tue,
            'SALES_WED' as sales_wed,
            'SALES_THU' as sales_thu,
            'SALES_FRI' as sales_fri)
);

-- Q] sales 테이블을 언피벗해보자
SELECT * FROM sales;

select * from sales
unpivot(
        QUANTITY
        for WEEK_DAY
        in (SALES_MON,SALES_TUE,SALES_WED,SALES_THU,SALES_FRI)
        );

select week_day, sales_mon from sales_log cross join sales;

-- Q] job_history 테이블에서 각 직원의 근속연수를 구해보자.

-- my answer
select TO_CHAR(END_DATE,'YY') - (decode(TO_CHAR(START_DATE,'YY'),97,-3,95,-5,TO_CHAR(START_DATE,'YY'))) as work_year from job_history;


select c.region_id, r.region_name,count(c.region_id) count
from COUNTRIES c join regions r
on c.region_id=r.region_id
group by c.region_id,r.region_name;

-- Q] regions 테이블과 countries 테이블에서 region_id와 region_name,
-- 그리고 region_id와 region_name의 숫자를 세는 열을 추가하여 출력하시오.

-- my answer
select region_id, region_name, count(*) as count from countries
natural join regions
group by region_id, region_name;

select c.region_id, r.region_name,count(c.region_id) count
from COUNTRIES c join regions r
on c.region_id=r.region_id
group by c.region_id,r.region_name;

-- Q] 

        
