
#line = blank = int(input("홀수를 입력하세요(0 <-종료):"))
line = blank = 5
print(int(blank/2))
if line == 0 or line %2 == 0:
    pass
else:
    print('-' * int(line))
    for i in range(1, line + 2, 2):
        #print('|',end= ' ')
        print(' ' * int(blank / 2),end='')
        print('*' * i, end='')
        print(' ' * int(blank / 2))
        #print('|')
        blank -= 2

    blank = blank + 2

    for i in range(1, line, 2):
        blank += 2
        #print('|',end= ' ')
        print(' ' * int(blank / 2),end='')
        print('*' * int(line - i - 1),end='')
        print(' ' * int(blank / 2))
        #print('|')
    print('-' * int(line))