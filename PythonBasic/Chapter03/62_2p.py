score = int (input('점수 입력 : '))
grade = ''

if (score >= 85) and (score <= 100) :
    grade = '우수'
elif (score  >= 70) and (score < 85):
    grade = '평범'
elif (score >= 0) and (score < 70) :
    grade = '저조'
else :
    grade = '올바른 점수를 입력하세요'

#print('당신의 점수는 %d이고, 등급은 %s'%(score,grade))
print(f'당신의 점수는 {score}이고, 등급은 {grade} 합니다')
#print(f'당신의 점수는 {format(score,"3,d")}이고, 등급은 {grade}')
