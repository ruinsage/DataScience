import io

file = open('data/test.txt',mode='r')
read = file.readlines()
#print('\n'.join(read))
read2 = file.readline(2)
print(read2)
