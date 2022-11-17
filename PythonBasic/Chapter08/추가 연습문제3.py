import io
try:
    life = open('data/life.txt', mode= 'r')
    lines = life.readlines()
    #print(lines)
    doc = []
    for sent in lines :
        doc.append(sent.strip())
    #print(doc)
    sentance = doc[1]
    #print(sentance)
    sentance = sentance.replace('java','python')
    #print(sentance)
    sentance1 = doc[0]
    #print(sentance1)
    sentance2 = sentance1 + sentance
    #print(sentance2)
    change = open('data/life.txt', mode= 'w')
    change.write(sentance2)
    change.close()

except Exception as e :
    print(f"예외 발생: {e}")

finally:
    life.close()




