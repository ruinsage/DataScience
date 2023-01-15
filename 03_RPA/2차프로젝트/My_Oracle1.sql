drop table review;
select * from review where rental_car_id > 112;
select * from electro_station;

select * from parking_area;

select * from gas_station;

drop table review;
select * from review;

create table ROAD_WORK(
id varchar2(38),
lat varchar2(128),
lon varchar2(128),
heading number(38),
link_id varchar2(64),
whole_lane number(38),
block_lane number(38),
text varchar2(64),
created_at timestamp,
last_updated_at timestamp
);

create table ROAD_WORK(
id varchar2(64),
lat varchar2(128),
lon varchar2(128),
heading number(38),
link_id varchar2(64),
whole_lane number(38),
block_lane number(38),
text varchar2(128),
created_at timestamp,
last_updated_at timestamp
);

drop table ROAD_WORK;
select * from ROAD_WORK;

create table ROAD_CLOSE(
id varchar2(64),
lat varchar2(128),
lon varchar2(128),
heading number(38),
link_id varchar2(64),
whole_lane number(38),
block_lane number(38),
text varchar2(128),
created_at timestamp,
last_updated_at timestamp
);

drop table ROAD_CLOSE;
select * from ROAD_CLOSE;

create table ROAD_EVENT(
id  varchar2(256),
lat varchar2(128),
lon varchar2(128),
heading number(16,10),
link_id varchar2(64),
code number(16,10),
created_at timestamp,
last_updated_at timestamp
);

drop table ROAD_EVENT;
select * from ROAD_EVENT;

drop table ROAD_CONDITION;
select * from ROAD_CONDITION;

create table ROAD_CONDITION(
id  varchar2(256),
lat varchar2(128),
lon varchar2(128),
heading number(16,10),
link_id varchar2(64),
visibility number(16,10),
snow varchar2(128),
road_temp varchar2(128),
water_film varchar2(128),
friction varchar2(128),
code number(16,10),
current_time timestamp
);

create table wave2(
관측소코드 varchar2(16),
관측소명 varchar2(32),
관측시간 TIMESTAMP,
파도높이 number(8,3)
);

drop table wave2;
select * from wave2;

