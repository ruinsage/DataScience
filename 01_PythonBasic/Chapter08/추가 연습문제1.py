import io
try:
    text = open('data/test.txt',mode= 'w')
    text.write('Life is too short')

    text = open('data/test.txt',mode= 'r')
    print(text.read())

except Exception as e :
    print('μμΈλ°μ :',e)

finally:
    text.close()