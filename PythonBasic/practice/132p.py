x=50
def func(x):
    x += 50
    print(f"지역변수 y: {x}")

func(x)
print(f"전역변수 x: {x}")
