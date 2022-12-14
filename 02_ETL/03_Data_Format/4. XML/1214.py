from xml.etree.ElementTree import Element, parse,dump
import xml.etree.ElementTree as ET
def while_xml(): #전체 xml 정보를 출력
    tree=parse("students_info.xml")
    students_info=tree.getroot()
    # dump(students)
    for student in students_info:
        name = student.get("name")
        sex = student.get("sex")
        age = student.findtext("age")
        major = student.findtext("major")
        print(f'* {name}')
        print(f'-성별: {sex}')
        print(f'-나이: {age}')
        print(f'-전공: {major}')

        for language_info in student.iter("language"):
            lan_name=language_info.get("name")
            lan_level=language_info.get("level")
            for period_info in student.iter("period"):
                lan_period=period_info.get("value")
            print(f'> {lan_name} 학습기간:{lan_period} level: {lan_level}')

        print()

def sumup_xml():
    tree = parse("students_info.xml")
    students_info = tree.getroot()

    student_num=0
    man_num=0
    wom_num=0
    major_num=0
    language_experienced=0
    highlevel_num=0
    python_experienced=0
    twenties=[]
    thirties=[]
    forties=[]

    for student in students_info:
        student_num+=1
        name = student.get("name")
        age = int(student.findtext("age"))
        if student.get("sex") == '남':
            man_num+=1
        else:
            wom_num+=1

        if ('컴퓨터 공학' in student.findtext("major")) or ('통계' in student.findtext("major")):
            major_num+=1

        if (age<30):
            twenties.append(f'{name}:{age}')
        elif (age<40):
            thirties.append(f'{name}:{age}')
        else:
            forties.append(f'{name}:{age}')

        for practical_info in student.iter("practicable_computer_languages"):
            if practical_info.text:
                language_experienced+=1
            for language_info in student.iter("language"):
                if '상' in language_info.get("level"):
                    highlevel_num+=1
                if language_info.get("name").lower()=='python' or language_info.get("name").lower()=='파이썬':
                    python_experienced+=1


    print(f'* 전체 학생수: {student_num}')
    print(f'* 성별')
    print(f'\t- 남학생: {man_num}명 ({man_num/student_num*100}%)')
    print(f'\t- 여학생: {wom_num}명 ({wom_num/student_num*100}%)')
    print(f'* 전공여부')
    print(f'\t- 전공자(컴퓨터 공학, 통계): {major_num}명 ({major_num/student_num*100}%)')
    print(f'\t- 프로그래밍 언어 경험자: {language_experienced}명 ({(language_experienced/student_num*100)}%)')
    print(f'\t- 프로그래밍 언어 상급자: {highlevel_num}명 ({(highlevel_num / student_num * 100)}%)')
    print(f'\t- 파이썬 경험자: {python_experienced}명 ({(python_experienced / student_num * 100)}%)')
    print('* 연령대')
    print(f'\t- 20대: {len(twenties)}명 ({len(twenties)/student_num*100}%) {twenties}')
    print(f'\t- 30대: {len(thirties)}명 ({len(thirties)/student_num*100}%) {thirties}')
    print(f'\t- 40대: {len(forties)}명 ({len(forties)/student_num*100}%) {forties}')
    print()

while(True):
    print("1. 요약정보")
    print("2. 전체 데이터 조회")
    print("3. 종료")

    option=input("메뉴입력 >> ")

    if option == "3":
        break
    elif option == "1":
        while_xml()
    elif option == "2":
        sumup_xml()
