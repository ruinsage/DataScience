import io
def search_visitor(name):
    with open('data/방명록.txt',mode='r',encoding='utf-8') as visitor:
        new_one = visitor.read()
        if new_one.find(name) == -1 :
            return False
        return True

while True:
    name = input("이름을 입력하세요:")
    is_new = search_visitor(name)
    if is_new == True :
        print(f"{name}님 방문해주셔서 감사합니다. 즐거운 시간 되세요")
    else:
        new_birth = input("생년월일을 입력하세요 (예:801212):")
        print(f"{name}님 환영합니다 아래 내용을 입력하셨습니다")
        print(f"{name} {new_birth}")
        with open('data/방명록.txt', mode='a', encoding='utf-8') as Add_name:
            Add_name.write(f"\n{name} {new_birth}")