import io

try:
    text = open('data/test2.txt',mode= 'w')
    text.write('')
    #print(2)

    while True :
        message = input("저장할 내용을 입력하세요 (종료는 엔터): ")
        text2 = open('data/test2.txt',mode= 'a',encoding= 'utf-8')
        if message == '엔터' :
            quit()
        else:
            text2.write(f'\n{message}')
            text2.close()
            #print(text2)

except Exception as e :
    print(f"예외발생 : {e}")

finally:
    text.close()
