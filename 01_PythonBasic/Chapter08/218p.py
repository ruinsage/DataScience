import os
print(f'\n현재경로 : {os.getcwd()}')

try:
    ftest1 = open('data/ftest.txt',mode= 'r')
    print(ftest1.read())

    ftest2 = open('data/ftest2.txt',mode= 'w')
    ftest2.write(f'my first text~~~~')

    ftest3 = open('data/ftest2.txt',mode= 'a')
    ftest3.write(f'\nmy second text~~~~')


except Exception as e:
    print(f'에러발생 : {e}')

finally:
    ftest1.close()
    ftest2.close()
    ftest3.close()
