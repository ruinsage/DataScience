select * from employees;

17. SUBSTR �Լ��� ����Ͽ� 4���� �Ի��� ����� ����Ͻÿ�.

select first_name, hire_date from employees where substr(hire_date,4,2) = '04';

18. MOD �Լ��� ����Ͽ� �����ȣ�� ¦���� ����� ����Ͻÿ�.
select first_name name, employee_id id from employees where mod(employee_id,2) = 0;

19. �Ի����� �⵵�� 2�ڸ�(YY), ���� ����(MON)�� ǥ���ϰ� ������ ��� (DY)�� �����Ͽ� ����Ͻÿ�.
select to_char(hire_date,'YY') as YY, to_char(hire_date,'MON') as MON, to_char(hire_date,'DY') as DAY  from employees;

20. ���� �� ĥ�� �������� ����Ͻÿ�. ���糯¥���� ���� 1�� 1���� �� ����� ����ϰ�
TO_DATE �Լ��� ����Ͽ� ������ ���� ��ġ ��Ű�ÿ�.
select round(sysdate - to_date('22/01/01')) as ���س�¥ from dual;

21. ������� ��� ����� ����ϵ� ����� ���� ����� ���ؼ��� NULL �� ��� 0���� ����Ͻÿ�.

select NVL(manager_id,0) from employees;
-- ����Ŭ������ NVL
-- select ifnull(manager_id,0) from employees; mysql������ ifnull 

23. ��� ����� �޿� �ְ��, ������, �Ѿ� �� ��� �޿��� ����Ͻÿ�. ��տ� ���ؼ��� ������ �ݿø��Ͻÿ�.
[��ó] [SQL] �������� (59����) Ǯ��|�ۼ��� �Ϲ���

24. �� ��� ���� �������� �޿� �ְ��, ������, �Ѿ� �� ��� ���� ����Ͻÿ�. ��տ� ���ؼ��� ������ �ݿø� �Ͻÿ�.
[��ó] [SQL] �������� (59����) Ǯ��|�ۼ��� �Ϲ���

25. COUNT(*) �Լ��� �̿��Ͽ� �������� ������ ��� ���� ����Ͻÿ�.
[��ó] [SQL] �������� (59����) Ǯ��|�ۼ��� �Ϲ���

26. ������ ���� �����Ͻÿ�.
[��ó] [SQL] �������� (59����) Ǯ��|�ۼ��� �Ϲ���




