create table weather(
    DATE_TIME   timestamp,
    NX          number(8,3),
    NY          number(8,3),
    ���        number(8,3),
    �ð�1_������ number(8,3),
    ��������     number(8,3),
    ����         number(8,3),
    ǳ��         number(8,3),
    ǳ��         number(8,3),
    �����ٶ�����  number(8,3),
    ���Ϲٶ�����  number(8,3)
);

create table weather(
    date_time       timestamp,
    nx              number(8,3),
    ny              number(8,3),
    �ð�1_������      number(8,3),
    ��������        number(8,3),
    ���              number(8,3),
    ����          number(8,3),
    ǳ��          number(8,3),
    ǳ��          number(8,3),
    �����ٶ�����  number(8,3),
    ���Ϲٶ�����  number(8,3)
);

drop TABLE weather;
delete from weather;
select * from weather;
COMMIT;

insert into weather values (
'202212281000',
58,125,0,0,-2.8,60,270,2,2.8,-0.8
);

insert into weather values (
'202212281100',
58,125,0,0,-1.8,60,250,3,2.8,-0.8
);

insert into weather values (
'202212281200',
58,125,0,0,1,58,280,3,2.6,-0.7
);

insert into weather values (
'202212281300',
58,125,0,0,2,58,230,2,2.3,-0.5
);


-- �ڵ� ���� sql
INSERT INTO WEATHER (DATE_TIME, NX, NY, "���", "�ð��簭����", "��������", "����", "ǳ��", "ǳ��", "�����ٶ�����", "���Ϲٶ�����")
VALUES (to_timestamp('202212271500'),58,125,3.4,0.0,0.0,46.0,1.4,225.0,1.0,1.0);

INSERT INTO WEATHER (DATE_TIME, NX, NY, "���", "�ð��簭����", "��������", "����", "ǳ��", "ǳ��", "�����ٶ�����", "���Ϲٶ�����")
VALUES ('20221227 1500',58,125,3.4,0.0,0.0,46.0,1.4,225.0,1.0,1.0);