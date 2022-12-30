import re
import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html, 'html.parser')
print(soup.tbody.prettify())
p1 = re.compile('\\s+?.*alt[=]["](?P<target>.*)["]\\swid',re.MULTILINE)
m1 = re.search(p1,soup.tbody.prettify())
print(m1.group("target"))
p2 = re.findall('.*(title)?(class)?\=\"\\w.*\"\>(\\w)\<\$')
m2 = re.search(p2,soup.prettify())
print(m2)