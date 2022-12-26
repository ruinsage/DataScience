import io
try:
    text = open('data/test.txt',mode= 'w')
    text.write('Life is too short')

    text = open('data/test.txt',mode= 'r')
    print(text.read())

except Exception as e :
    print('예외발생 :',e)

finally:
    text.close()