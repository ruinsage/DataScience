create table bus(
������ID varchar2(16),
�����Ҹ� varchar2(64),
ù��°���������޽��� varchar2(64),
�ι�°���������޽��� varchar2(64)
);

drop table bus;

select * from bus;

create table bus_753(
    ������ID               varchar2(64),
    �����Ҹ�               varchar2(64),
    ù��°���������޽���      varchar2(64),
    �ι�°���������޽���      varchar2(64),
    �����ð�               timestamp
);
select * from bus_753;

select * from bus_753 where ù��°���������޽��� = '�� ����' and �����ð� = (select max(�����ð�) from bus_753);