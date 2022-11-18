import random

student_list = ['김유진','문성준','박종민','송지예','양석훈','이예지','임성혁','한권제','현재봉','이현구']
result_list = []
def coffee_lotto(student_list, target_num):
    print("<전체 명단>")
    new_student_list = ' '.join(student_list)
    print(new_student_list)
    #print(student_list)
    result = int(input("당첨자 수를 입력하세요: "))
    while len(result_list) < result :
        random_number = random.randint(0,9)
        name = student_list[random_number]
        if name in result_list:
            pass
        else:
            result_list.append(student_list[random_number])
    print("축하합니다!")
    for name in result_list:
        print(name,end=' ')
    print()
def presentation_order(student_list):
    student_list.pop(9)
    print("<학생 명단>")
    for name in student_list:
        print(name,end=' ')
    print()
    result = 9
    while len(result_list) < result :
        random_number = random.randint(0,8)
        name = student_list[random_number]
        if name in result_list:
            pass
        else:
            result_list.append(student_list[random_number])
    print("발표자 순서는 아래와 같습니다")
    for name in result_list:
        print(name,end=' ')
    print()

print("1.커피로또")
print("2.발표자순서")
target_num = input("메뉴를 선택하세요 (엔터는 종료): ")


if target_num == '1':
    coffee_lotto(student_list,target_num)
elif target_num == '2':
   presentation_order(student_list)
elif target_num == '':
    pass
else:
    pass