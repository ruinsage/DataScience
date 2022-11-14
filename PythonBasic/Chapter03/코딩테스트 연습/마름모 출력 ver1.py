input_num = int(input("홀수를 입력하세요(0 <- 종료):"))

if (input_num %2) == 1:
    for i in range (0,(int(input_num /2 +1))):
        for j in range (0,input_num):
            print(f"' '*{input_num /2-i}",end=' ')
            print(f"'*'*{(2*i+1)}",end=' ')
            print(f"' '*{input_num /2-i}",end=' ')
            j += 1
        i += 1
        print()

else:
    print("홀수를 입력하세요")

