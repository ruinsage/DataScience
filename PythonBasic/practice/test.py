def solution(slice, n):
    answer = 0
    if n >= 1 and n <= 100 and slice >=2 and slice <=10:
        if n % slice == 0:
            answer = n // slice
        else:
            answer = n // slice + 1
    return answer

slice = 7
n = 16
print(solution(slice, n))
print(((n - 1) // slice) + 1)