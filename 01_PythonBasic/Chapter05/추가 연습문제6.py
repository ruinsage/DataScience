annual_salary = int(input("연봉을 입력하세요"))
def calc_monthly_salary(annual_salary) :
    monthly_salary = annual_salary //12
    print(f"월급은 ",format(monthly_salary,"3,d"),"원 입니다")

calc_monthly_salary(annual_salary)