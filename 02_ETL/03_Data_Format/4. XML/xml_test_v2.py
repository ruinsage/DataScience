from xml.etree.ElementTree import Element, parse,dump
import xml.etree.ElementTree as ET

def whole_xml():
    tree = parse('students_zero.xml')
    student_list = tree.getroot()

    for student in student_list.iter('student'):
        print(f"* {student.get('name')}")
        print(f"- 성별 : {student.get('sex')}")

        print(f"- 나이 : {student.find('age').text}")
        print(f"- 전공 : {student.find('major').text}")


while True:
    print("학생정보 XML 데이터 분석 시작")
    print("\n1. 요약정보\n2. 전체데이터 조회\n3. 종료")
    menu = int(input("메뉴입력 : "))

    if menu == 1:
        whole_xml()

    elif menu == 2:
        whole_xml()

    elif menu == 3:
        break