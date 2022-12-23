describe ii2;

alter table ii2 rename to processed_food;
describe processed_food;

select * from processed_food order by 탄수화물 desc;


select * from processed_food
where 식품대분류명 in ('농산가공식품류','동물성가공식품류','두부류 또는 묵류','수산가공식품류','식육가공품 및 포장육',
                       '알가공품류','유가공품류','음료류','절임류 또는 조림류','조미식품','즉석식품류','특수영양식품','특수의료용도식품' )and 트랜스지방산 = 0
order by 콜레스테롤;


select 식품소분류명, count(*) from processed_food 
where 식품대분류명 in ('농산가공식품류','동물성가공식품류','두부류 또는 묵류','수산가공식품류','식육가공품 및 포장육',
                       '알가공품류','유가공품류','음료류','절임류 또는 조림류','조미식품','즉석식품류','특수영양식품','특수의료용도식품' )
                       and 트랜스지방산 = 0
                       
group by 식품소분류명 order by count(*) desc;


select 식품명, 탄수화물, 지방, 단백질 , 식품대분류명, NTILE(4) over(order by 탄수화물 desc) as 탄수화물NT, NTILE(4) over(order by 단백질 desc) as 단백질NT,
NTILE(4) over(order by 지방 desc) as 지방NT
from processed_food
where 식품대분류명 in ('농산가공식품류','동물성가공식품류','두부류 또는 묵류','수산가공식품류','식육가공품 및 포장육',
                       '알가공품류','유가공품류','절임류 또는 조림류','조미식품','즉석식품류','특수영양식품','특수의료용도식품' )
                       and 트랜스지방산 = 0
                       and 식품명 not like '%음료%'
                       and 식품명 not like '%미숫가루%'
                       and 탄수화물 < 100
order by 단백질 desc, 탄수화물 asc, 지방 asc, 에너지 asc;



select 식품대분류명 from processed_food group by 식품대분류명;
where 식품대분류명 is not in();


select 식품명, 탄수화물, 단백질, 지방
from processed_food
where 탄수화물 != 0 or 단백질 != 0 or 지방 != 0
;



select 식품명, RANK() over(order by (select 탄수화물 from processed_food where rownum < 11 order by 탄수화물 desc) desc) as RANK from processed_food
;

select 탄수화물 from processed_food where rownum < 11 order by 탄수화물 desc;



