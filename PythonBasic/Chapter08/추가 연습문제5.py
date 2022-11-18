import io

idol_list = open("data/연습생.txt", mode= 'r', encoding="utf-8")
idol_list2 = '\n'.join(idol_list.read())
print(idol_list2)
for idol in idol_list2:
   print({idol})
   #print(f"신예 아이돌 {idol} 인기 급상승")

