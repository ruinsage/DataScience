height = int(input('height : '))
#print(height)

def StarCount(height) :
    cnt = 0
    for star in range(1, height + 1):
        print("*" * star)
        cnt += star
    return cnt
print('start 개수 : %d'%StarCount(height))