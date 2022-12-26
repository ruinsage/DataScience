import random
def coin(n) :
    result = []
    for i in range(n) :
        r = random.randint(0,1)
        if r == 1 :
            result.append(1)
        else:
            result.append(0)
    return result

print(coin(10))
#print(coin(1)[0])
def monta_coin(n):
    cnt = 0
    for i in range(n) :

        cnt += coin(1)[0]

    result = cnt / n
    return result

print(monta_coin(10))