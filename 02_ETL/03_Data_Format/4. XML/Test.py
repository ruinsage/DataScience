from xml.etree.ElementTree import parse
from xml.etree.ElementTree import dump


def whole_xml():
    tree = parse("students_info.xml")
    note = tree.getroot()

    for parent in note.iter('student'):
        print(f'*{parent.get("name")}')
        print(f'-성별: {parent.get("sex")}')
        print(f'-나이: {parent.find("age").text}')
        print(f'-전공: {parent.find("major").text}')
        computer_lang = parent.find('practicable_computer_languages')
        print(parent.find('practicable_computer_languages').get('name'))
        #if computer:
            #if parent

        #print(parent.find("language").text)




    #for key in student.keys():
    #if key == 'name':
    #elif key == 'sex':
    #else:
    #for info in student.ag
    #print(f'나이 : {key.text}')
    #for key in student.iter():
    #for key in student.keys():
    # if key == 'age':
    #  print(f'-나이: {student.get(key)}')

    #if :
    #print(student_list.get(key))

    #for student in student_list.iter():
    #dump(student)




#while True:
print('학생정보 XML데이터 분석 시작')
print((' 1.요약정보\n 2.전체 데이터 조회\n 3.종료\n'))
select = int(input('메뉴 입력: '))

if select == 3:
    print('학생 정보 분석 완료!')
    quit()
elif select == 2:
    whole_xml()