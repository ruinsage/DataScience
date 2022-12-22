-- Q] sales_log ���̺��� �ǹ��غ���
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

-- Q] sales ���̺��� ���ǹ��غ���
SELECT * FROM sales;

select * from sales
unpivot(
        QUANTITY
        for WEEK_DAY
        in (SALES_MON,SALES_TUE,SALES_WED,SALES_THU,SALES_FRI)
        );

select week_day, sales_mon from sales_log cross join sales;

-- Q] job_history ���̺��� �� ������ �ټӿ����� ���غ���.

-- my answer
select TO_CHAR(END_DATE,'YY') - (decode(TO_CHAR(START_DATE,'YY'),97,-3,95,-5,TO_CHAR(START_DATE,'YY'))) as work_year from job_history;


select c.region_id, r.region_name,count(c.region_id) count
from COUNTRIES c join regions r
on c.region_id=r.region_id
group by c.region_id,r.region_name;

-- Q] regions ���̺�� countries ���̺��� region_id�� region_name,
-- �׸��� region_id�� region_name�� ���ڸ� ���� ���� �߰��Ͽ� ����Ͻÿ�.

-- my answer
select region_id, region_name, count(*) as count from countries
natural join regions
group by region_id, region_name;

select c.region_id, r.region_name,count(c.region_id) count
from COUNTRIES c join regions r
on c.region_id=r.region_id
group by c.region_id,r.region_name;

-- Q] 

        
