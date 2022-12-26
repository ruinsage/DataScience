class Person:
    #생성자
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    #메서드(display)
    def display(self):
        if self.gender == "female":
            gender2 = "여자"
        else:
            gender2 = "남자"
        print("=" *30)
        print(f"이름: {self.name}",end=', ')
        print(f"성별: {gender2}")
        print(f"나이: {self.age}")
        print("=" *30)

name = input("이름입력:")
age = int(input("나이입력"))
gender = input("성별(male/female) 입력:")
p =  Person(name,age,gender)
p.display()