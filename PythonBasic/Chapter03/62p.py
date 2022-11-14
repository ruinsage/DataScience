score = int (input('점수 입력 : '))
grade = ''

if (score >= 85) and (score <=100) :
    grade = '우수'
elif score >= 70 :
    grade = '보통'
else:
    grade = '저조'

#print('당신의 점수는 %d이고, 등급은 %s'%(score,grade))
print(f'당신의 점수는 {score}이고, 등급은 {grade}')
#print(f'당신의 점수는 {format(score,"3,d")}이고, 등급은 {grade}')
