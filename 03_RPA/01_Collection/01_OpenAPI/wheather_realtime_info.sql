create table weather(
    DATE_TIME   varchar2(32),
    NX          number(8,3),
    NY          number(8,3),
    ���        number(8,3),
    �ð��簭���� number(8,3),
    ��������     number(8,3),
    ����         number(8,3),
    ǳ��         number(8,3),
    ǳ��         number(8,3),
    �����ٶ�����  number(8,3),
    ���Ϲٶ�����  number(8,3)
);
drop TABLE weather;
delete from weather;
select * from weather;

-- �ڵ� ���� sql
INSERT INTO WEATHER (DATE_TIME, NX, NY, "���", "�ð��簭����", "��������", "����", "ǳ��", "ǳ��", "�����ٶ�����", "���Ϲٶ�����")
VALUES (to_timestamp('202212271500'),58,125,3.4,0.0,0.0,46.0,1.4,225.0,1.0,1.0);

INSERT INTO WEATHER (DATE_TIME, NX, NY, "���", "�ð��簭����", "��������", "����", "ǳ��", "ǳ��", "�����ٶ�����", "���Ϲٶ�����")
VALUES ('20221227 1500',58,125,3.4,0.0,0.0,46.0,1.4,225.0,1.0,1.0);