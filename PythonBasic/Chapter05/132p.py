x=50
def func(y):
    y += 30
    print(f"지역변수 y: {y}")

def print_x():
    global x
    print(f'함수에서 전역변수 읽기 시도: {x}')
    x += 50

func(x)
print(f"전역변수 x: {x}")
print_x()