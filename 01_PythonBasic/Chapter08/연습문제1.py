import io
file = open("data/ftest.txt", mode= 'r')

lines = file.readlines() #줄 단위 전체 읽기
docs = []
words = []
#print(lines)

for sent in lines :
    docs.append(sent.strip())

print(docs)
print(f"문장 수 : {len(docs)}")

for word in docs :
    words.append(word.split())
print("단어 내용")

print(words)

