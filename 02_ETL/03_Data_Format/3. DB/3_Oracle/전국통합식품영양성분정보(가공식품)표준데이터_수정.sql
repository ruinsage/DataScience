describe ii2;

alter table ii2 rename to processed_food;
describe processed_food;

select * from processed_food order by ź��ȭ�� desc;


select * from processed_food
where ��ǰ��з��� in ('��갡����ǰ��','������������ǰ��','�κη� �Ǵ� ����','���갡����ǰ��','��������ǰ �� ������',
                       '�˰���ǰ��','������ǰ��','�����','���ӷ� �Ǵ� ������','���̽�ǰ','�Ｎ��ǰ��','Ư�������ǰ','Ư���Ƿ�뵵��ǰ' )and Ʈ��������� = 0
order by �ݷ����׷�;


select ��ǰ�Һз���, count(*) from processed_food 
where ��ǰ��з��� in ('��갡����ǰ��','������������ǰ��','�κη� �Ǵ� ����','���갡����ǰ��','��������ǰ �� ������',
                       '�˰���ǰ��','������ǰ��','�����','���ӷ� �Ǵ� ������','���̽�ǰ','�Ｎ��ǰ��','Ư�������ǰ','Ư���Ƿ�뵵��ǰ' )
                       and Ʈ��������� = 0
                       
group by ��ǰ�Һз��� order by count(*) desc;


select ��ǰ��, ź��ȭ��, ����, �ܹ��� , ��ǰ��з���, NTILE(4) over(order by ź��ȭ�� desc) as ź��ȭ��NT, NTILE(4) over(order by �ܹ��� desc) as �ܹ���NT,
NTILE(4) over(order by ���� desc) as ����NT
from processed_food
where ��ǰ��з��� in ('��갡����ǰ��','������������ǰ��','�κη� �Ǵ� ����','���갡����ǰ��','��������ǰ �� ������',
                       '�˰���ǰ��','������ǰ��','���ӷ� �Ǵ� ������','���̽�ǰ','�Ｎ��ǰ��','Ư�������ǰ','Ư���Ƿ�뵵��ǰ' )
                       and Ʈ��������� = 0
                       and ��ǰ�� not like '%����%'
                       and ��ǰ�� not like '%�̼�����%'
                       and ź��ȭ�� < 100
order by �ܹ��� desc, ź��ȭ�� asc, ���� asc, ������ asc;



select ��ǰ��з��� from processed_food group by ��ǰ��з���;
where ��ǰ��з��� is not in();


select ��ǰ��, ź��ȭ��, �ܹ���, ����
from processed_food
where ź��ȭ�� != 0 or �ܹ��� != 0 or ���� != 0
;



select ��ǰ��, RANK() over(order by (select ź��ȭ�� from processed_food where rownum < 11 order by ź��ȭ�� desc) desc) as RANK from processed_food
;

select ź��ȭ�� from processed_food where rownum < 11 order by ź��ȭ�� desc;



