from xml.etree.ElementTree import parse
from xml.etree.ElementTree import dump

tree = parse("students_info.xml")
note = tree.getroot()
def sumup_xml():
    data = []
    for parent in note.iter('student'):
        student_list = []
        student_list.append(parent.get('name'))
        student_list.append(parent.get('sex'))
        student_list.append(parent.get('name'))
        student_list.append(parent.find('age').text)
        student_list.append(parent.find('major').text)
        data.append(student_list)
    print(data)

def whole_xml():
    for parent in note.iter('student'):
        print(f'*{parent.get("name")}')
        print(f'-성별: {parent.get("sex")}')
        print(f'-나이: {parent.find("age").text}')
        print(f'-전공: {parent.find("major").text}')
        computer_lang = parent.find('practicable_computer_languages')
        #print(parent.find('language').text)
        if computer_lang:
            for language in computer_lang.iter('language'):
                print(f"{language.get('name')} 학습기간 : {language.find('period').get('value')} level : {language.get('level')}")

while True:
    print('학생정보 XML데이터 분석 시작')
    print((' 1.요약정보\n 2.전체 데이터 조회\n 3.종료\n'))
    select = int(input('메뉴 입력: '))

    if select == 3:
        print('학생 정보 분석 완료!')
        quit()
    elif select == 2:
        whole_xml()
    elif select == 1:
        sumup_xml()
    else:
        quit()