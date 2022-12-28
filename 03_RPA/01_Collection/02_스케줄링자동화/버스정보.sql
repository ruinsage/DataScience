create table bus(
정류소ID varchar2(16),
정류소명 varchar2(64),
첫번째도착정보메시지 varchar2(64),
두번째도착정보메시지 varchar2(64)
);

drop table bus;

select * from bus;

create table bus_753(
    정류소ID               varchar2(64),
    정류소명               varchar2(64),
    첫번째도착정보메시지      varchar2(64),
    두번째도착정보메시지      varchar2(64),
    제공시각               timestamp
);
select * from bus_753;

select * from bus_753 where 첫번째도착정보메시지 = '곧 도착' and 제공시각 = (select max(제공시각) from bus_753);