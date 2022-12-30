from bs4 import BeautifulSoup
import urllib.request

html = urllib.request.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html, 'html.parser')

ranks = soup.findAll('img', attrs={'width':'14'}) # 1번째 열: 순위
tags = soup.findAll('div', attrs={'class':'tit3'})   # 2번째 열: 영화이름
up_downs =  soup.findAll('img', attrs={'class':'arrow'}) # 3번째 열: 등락 여부
ranges = soup.findAll('td', attrs={'class':'range ac'})  # 4번째 열: 등락 범위

f = open('movie_rank_test.csv', 'w', encoding='utf-8')
f.write('rank, name, range\n')
i = 0
while i < len(ranks)-1:
    print('{0}, {1}, {2}, {3}'.format(int(ranks[i]['alt']), tags[i].a['title'], ranges[i].string, up_downs[i]['alt']))
    #             i번째 ranks 변수의 alt속성 값을 인티져한 포멧, i번째 tag 변수의 title 속성 값, i번째 ranges 변수의 값
    f.write('{0}, {1}, {2}, {3}\n'.format(int(ranks[i]['alt']), tags[i].a['title'], ranges[i].string, up_downs[i]['alt']))
    i += 1
f.close()