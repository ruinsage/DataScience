def a():
    print('a')
    def b():
        print('b')
    return b
b =a()
b()