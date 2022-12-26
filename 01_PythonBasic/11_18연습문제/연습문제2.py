import io
def write(message):
    with open("data/메세지.txt", mode='w',encoding='utf-8') as file:
        for i in range(1,11):
            file.write(message+f"{i}\n\n")

message = input("메시지를 입력하세요: ")
write(message)
