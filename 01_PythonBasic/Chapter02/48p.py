single_q_str = '안녕하세요.'
print(single_q_str)

#single_q_str =''안녕하세요' 라고 철수가 말했다.' # ' 가 있는 인용부호를 처리 못하는 문제
double_q_str ="'안녕하세요' 라고 철수가 말했다."
print(double_q_str)
#double_q_str =""안녕하세요" 라고 철수가 말했다." # " 가 있는 인용부호를 처리 못하는 문제
double_q_str ='"안녕하세요" 라고 철수가 말했다.'
print((double_q_str))
#mix_str = ""수리수리!" 이것은 말그대로 '괴변' 이야!!" # '," 공존하는 문자열은 처리하기 어렵다
mix_str = "\"수리수리!\" 이것은 말그대로 '괴변' 이야!!" # \로 "를 특수문자처리하여 문제를 해결
print(mix_str)
str_escape = "수리수리! \t마수리!"
print(str_escape)
str_escape = "수리수리! \n마수리!"
print(str_escape)
str_escape = "수리수리! \n마수리! \n일어나라!"
print(str_escape)
tripple_str ="""
수리수리!
마수리!
일어나라!
"""
print(tripple_str)

print("수리"*5)


print(num)
