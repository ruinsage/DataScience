
while True:
    line = blank = int(input("홀수를 입력하세요(0 <-종료):"))
    if line == 0 or line %2 == 0:
        break
    else:
        for i in range(1, line + 2, 2):
            print(' ' * int(blank / 2), end='')
            print('*' * i, end='')
            print(' ' * int(blank / 2))
            blank -= 2

        blank = blank + 2

        for i in range(1, line + 2, 2):
            blank += 2
            print(' ' * int(blank / 2), end='')
            print('*' * int(line - i - 1), end='')
            print(' ' * int(blank / 2))

