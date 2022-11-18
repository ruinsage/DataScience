import sys

def myargv(number_list):
    result = 0
    for i in number_list:
        result += int(i)
    return result
    
number_list = sys.argv[1:]
print(myargv(number_list))