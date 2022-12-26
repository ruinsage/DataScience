line = int(input("홀수를 입력하세요(0 <-종료):"))

for i in range(1,line+2,2):
    print(' ' * int(line/2),end='')
    print('*' * i, end= '')
    print(' ' * int(line/2))
    line -= 2

