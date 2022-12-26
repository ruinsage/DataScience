string = input("열개의 문자을 입력하세요")
def print_5xn(string):
    for i in range(0,len(string),5) :
        print(string[i:i+5])

print_5xn(string)