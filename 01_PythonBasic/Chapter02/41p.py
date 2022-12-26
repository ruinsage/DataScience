i = tot = 10  # i = 10 , tot = 10
i += 1  # i(10) + 1 = i(11)
tot += i # tot(10) + i(11) = tot(21)

print(i, tot)

#print('출력')
print('출력', end=' , ') # 줄 끝을 의미하는 end를 ,키로 변환한다
print('출력')

#안녕하세요 반갑습니다.

print('안녕하세요', end=' ') # 줄 끝을 의미하는 end를  (공백)키로 변환한다
print('반갑습니다')

print(f'su 주소 : {id(i)}')