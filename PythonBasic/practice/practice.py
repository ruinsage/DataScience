array = [149,180,192,170]
height = 167
def solution(array, height):
    if len(array) >= 1 and len(array) <= 100 and height >= 1 and height <= 100:
        for class_height in array:
            if class_height >= 1 and class_height <= 200:
                if class_height > height:
                    answer = + 1
                    return answer

print(len(array))
print(solution(array, height))