drop table review;
select * from review where rental_car_id > 112;
select * from electro_station;

select * from parking_area;

select * from gas_station;

drop table review;
select * from review;



create table ROAD_WORK(
id varchar2(255),
lat FLOAT,
lon float,
heading number(10,0),
link_id number(19,0),
whole_lane number(19,0),
block_lane varchar2(255),
text varchar2(255),
created_at timestamp(6),
last_updated_at timestamp(6)
);

drop table ROAD_WORK;
select * from ROAD_WORK;

create table ROAD_CLOSE(
id number(20,0),
lat number(10,5),
lon number(10,5),
heading number(10,5),
link_id varchar2(128),
whole_lane number(10),
block_lane VARCHAR2(128),
text clob,
created_at timestamp(6),
last_updated_at timestamp(6)
);

drop table ROAD_CLOSE;
select * from ROAD_CLOSE;

create table ROAD_EVENT(
id  varchar2(50),
lat number(10,6),
lon number(10,6),
heading number(10,2),
link_id varchar2(50),
code varchar2(50),
created_at timestamp(6),
last_updated_at timestamp(6)
);

drop table ROAD_EVENT;
select * from ROAD_EVENT;

drop table ROAD_CONDITION;
select * from ROAD_CONDITION;

create table ROAD_CONDITION(
id  number(19,0),
lat number(10,5),
lon number(10,5),
heading number(10,5),
link_id varchar2(128),
visibility number(10,0),
snow number(10,5),
road_temp number(5,2),
water_film number(10,5),
friction number(10,5),
code VARCHAR2(20),
current_time timestamp(6)
);


