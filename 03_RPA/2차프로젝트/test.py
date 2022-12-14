from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import urllib.request
from bs4 import BeautifulSoup
import re
import urllib.request as ur
import pandas as pd

all_rent_page = ['https://place.map.kakao.com/10620530#comment',
 'https://place.map.kakao.com/24764839#comment',
 'https://place.map.kakao.com/17940761#comment',
 'https://place.map.kakao.com/1657351953#comment',
 'https://place.map.kakao.com/400227802#comment',
 'https://place.map.kakao.com/26887342#comment',
 'https://place.map.kakao.com/1762689033#comment',
 'https://place.map.kakao.com/25769803#comment',
 'https://place.map.kakao.com/10804673#comment',
 'https://place.map.kakao.com/452411056#comment',
 'https://place.map.kakao.com/26521408#comment',
 'https://place.map.kakao.com/777468585#comment',
 'https://place.map.kakao.com/1257647888#comment',
 'https://place.map.kakao.com/17673118#comment',
 'https://place.map.kakao.com/18801206#comment',
 'https://place.map.kakao.com/8433016#comment',
 'https://place.map.kakao.com/14951073#comment',
 'https://place.map.kakao.com/97285313#comment',
 'https://place.map.kakao.com/13128056#comment',
 'https://place.map.kakao.com/1278792865#comment',
 'https://place.map.kakao.com/1590587423#comment',
 'https://place.map.kakao.com/1573434157#comment',
 'https://place.map.kakao.com/26410926#comment',
 'https://place.map.kakao.com/1246504106#comment',
 'https://place.map.kakao.com/20435418#comment',
 'https://place.map.kakao.com/452179586#comment',
 'https://place.map.kakao.com/12396156#comment',
 'https://place.map.kakao.com/132616791#comment',
 'https://place.map.kakao.com/26794322#comment',
 'https://place.map.kakao.com/1040551334#comment',
 'https://place.map.kakao.com/1775530391#comment',
 'https://place.map.kakao.com/1279272310#comment',
 'https://place.map.kakao.com/23233462#comment',
 'https://place.map.kakao.com/801793631#comment',
 'https://place.map.kakao.com/17143332#comment',
 'https://place.map.kakao.com/23306577#comment',
 'https://place.map.kakao.com/25611578#comment',
 'https://place.map.kakao.com/19360327#comment',
 'https://place.map.kakao.com/227103139#comment',
 'https://place.map.kakao.com/490730093#comment',
 'https://place.map.kakao.com/17385746#comment',
 'https://place.map.kakao.com/11084802#comment',
 'https://place.map.kakao.com/251018047#comment',
 'https://place.map.kakao.com/1243270632#comment',
 'https://place.map.kakao.com/14935399#comment',
 'https://place.map.kakao.com/347472732#comment',
 'https://place.map.kakao.com/1095110680#comment',
 'https://place.map.kakao.com/21211496#comment',
 'https://place.map.kakao.com/1198801448#comment',
 'https://place.map.kakao.com/10594478#comment',
 'https://place.map.kakao.com/41971535#comment',
 'https://place.map.kakao.com/17868198#comment',
 'https://place.map.kakao.com/27600795#comment',
 'https://place.map.kakao.com/250792642#comment',
 'https://place.map.kakao.com/175179946#comment',
 'https://place.map.kakao.com/230685883#comment',
 'https://place.map.kakao.com/1935905180#comment',
 'https://place.map.kakao.com/10609822#comment',
 'https://place.map.kakao.com/27054790#comment',
 'https://place.map.kakao.com/25118589#comment',
 'https://place.map.kakao.com/386041191#comment',
 'https://place.map.kakao.com/18211713#comment',
 'https://place.map.kakao.com/1301477495#comment',
 'https://place.map.kakao.com/1409474938#comment',
 'https://place.map.kakao.com/27319953#comment',
 'https://place.map.kakao.com/26938542#comment',
 'https://place.map.kakao.com/317770652#comment',
 'https://place.map.kakao.com/24963077#comment',
 'https://place.map.kakao.com/1504713683#comment',
 'https://place.map.kakao.com/1526991673#comment',
 'https://place.map.kakao.com/2019292758#comment',
 'https://place.map.kakao.com/1969706027#comment',
 'https://place.map.kakao.com/1844324780#comment',
 'https://place.map.kakao.com/1423920787#comment',
 'https://place.map.kakao.com/20580988#comment',
 'https://place.map.kakao.com/13011546#comment',
 'https://place.map.kakao.com/849248412#comment',
 'https://place.map.kakao.com/18488643#comment',
 'https://place.map.kakao.com/2001392507#comment',
 'https://place.map.kakao.com/21733597#comment',
 'https://place.map.kakao.com/1294579489#comment',
 'https://place.map.kakao.com/1489147341#comment',
 'https://place.map.kakao.com/62974884#comment',
 'https://place.map.kakao.com/1327322844#comment',
 'https://place.map.kakao.com/55866338#comment',
 'https://place.map.kakao.com/26932836#comment',
 'https://place.map.kakao.com/429897533#comment',
 'https://place.map.kakao.com/7940644#comment',
 'https://place.map.kakao.com/531388305#comment',
 'https://place.map.kakao.com/328479733#comment',
 'https://place.map.kakao.com/14859018#comment',
 'https://place.map.kakao.com/1255542005#comment',
 'https://place.map.kakao.com/25996630#comment',
 'https://place.map.kakao.com/2055149896#comment',
 'https://place.map.kakao.com/1398782408#comment',
 'https://place.map.kakao.com/9085651#comment',
 'https://place.map.kakao.com/1448008031#comment',
 'https://place.map.kakao.com/1540062178#comment',
 'https://place.map.kakao.com/1056817069#comment',
 'https://place.map.kakao.com/12319035#comment',
 'https://place.map.kakao.com/479427491#comment',
 'https://place.map.kakao.com/292605954#comment',
 'https://place.map.kakao.com/11282390#comment',
 'https://place.map.kakao.com/8041449#comment',
 'https://place.map.kakao.com/27579449#comment',
 'https://place.map.kakao.com/323410970#comment',
 'https://place.map.kakao.com/1755386334#comment',
 'https://place.map.kakao.com/1811016114#comment',
 'https://place.map.kakao.com/15956601#comment',
 'https://place.map.kakao.com/268801150#comment',
 'https://place.map.kakao.com/24759364#comment',
 'https://place.map.kakao.com/2041764006#comment',
 'https://place.map.kakao.com/246672209#comment',
 'https://place.map.kakao.com/1438170576#comment',
 'https://place.map.kakao.com/241934269#comment',
 'https://place.map.kakao.com/374945386#comment',
 'https://place.map.kakao.com/801966900#comment',
 'https://place.map.kakao.com/1212373742#comment',
 'https://place.map.kakao.com/1271427954#comment',
 'https://place.map.kakao.com/736450682#comment',
 'https://place.map.kakao.com/954809763#comment',
 'https://place.map.kakao.com/14093548#comment',
 'https://place.map.kakao.com/993769549#comment',
 'https://place.map.kakao.com/2136501797#comment',
 'https://place.map.kakao.com/1107918238#comment',
 'https://place.map.kakao.com/183265029#comment',
 'https://place.map.kakao.com/690708751#comment',
 'https://place.map.kakao.com/1492123479#comment',
 'https://place.map.kakao.com/59064937#comment',
 'https://place.map.kakao.com/1200750242#comment',
 'https://place.map.kakao.com/656491018#comment',
 'https://place.map.kakao.com/1355326806#comment',
 'https://place.map.kakao.com/12156591#comment',
 'https://place.map.kakao.com/9314025#comment',
 'https://place.map.kakao.com/70983628#comment',
 'https://place.map.kakao.com/1058462594#comment',
 'https://place.map.kakao.com/210507257#comment',
 'https://place.map.kakao.com/16745877#comment',
 'https://place.map.kakao.com/1468895767#comment',
 'https://place.map.kakao.com/1831531117#comment',
 'https://place.map.kakao.com/1355550623#comment',
 'https://place.map.kakao.com/1998280041#comment',
 'https://place.map.kakao.com/24764839#comment',
 'https://place.map.kakao.com/17940761#comment',
 'https://place.map.kakao.com/10804673#comment',
 'https://place.map.kakao.com/17673118#comment',
 'https://place.map.kakao.com/27527607#comment',
 'https://place.map.kakao.com/400227802#comment',
 'https://place.map.kakao.com/1202775036#comment',
 'https://place.map.kakao.com/1082768527#comment',
 'https://place.map.kakao.com/540321788#comment',
 'https://place.map.kakao.com/18801206#comment',
 'https://place.map.kakao.com/1580657752#comment',
 'https://place.map.kakao.com/1098506214#comment',
 'https://place.map.kakao.com/635534881#comment',
 'https://place.map.kakao.com/1548026500#comment',
 'https://place.map.kakao.com/26418409#comment',
 'https://place.map.kakao.com/564676511#comment',
 'https://place.map.kakao.com/982377677#comment',
 'https://place.map.kakao.com/1690567036#comment',
 'https://place.map.kakao.com/10944941#comment',
 'https://place.map.kakao.com/17266597#comment',
 'https://place.map.kakao.com/437807628#comment',
 'https://place.map.kakao.com/687752220#comment',
 'https://place.map.kakao.com/571322596#comment',
 'https://place.map.kakao.com/42317428#comment',
 'https://place.map.kakao.com/20033987#comment',
 'https://place.map.kakao.com/2072893496#comment',
 'https://place.map.kakao.com/399961245#comment',
 'https://place.map.kakao.com/473769104#comment',
 'https://place.map.kakao.com/1981347324#comment',
 'https://place.map.kakao.com/1925542408#comment',
 'https://place.map.kakao.com/1619669498#comment',
 'https://place.map.kakao.com/1985385539#comment',
 'https://place.map.kakao.com/1658414980#comment',
 'https://place.map.kakao.com/1154520709#comment',
 'https://place.map.kakao.com/208784086#comment',
 'https://place.map.kakao.com/10874477#comment',
 'https://place.map.kakao.com/1903470188#comment',
 'https://place.map.kakao.com/27445705#comment',
 'https://place.map.kakao.com/561308584#comment',
 'https://place.map.kakao.com/1202518555#comment',
 'https://place.map.kakao.com/990921948#comment',
 'https://place.map.kakao.com/452411056#comment',
 'https://place.map.kakao.com/691654269#comment',
 'https://place.map.kakao.com/483777957#comment',
 'https://place.map.kakao.com/1568005762#comment',
 'https://place.map.kakao.com/762756110#comment',
 'https://place.map.kakao.com/399855285#comment',
 'https://place.map.kakao.com/27559439#comment',
 'https://place.map.kakao.com/369567086#comment',
 'https://place.map.kakao.com/1902777910#comment',
 'https://place.map.kakao.com/1471951086#comment']

base_options = Options()
base_options.add_experimental_option("detach", True)
base_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=base_service, options=base_options)


url2 = all_rent_page[1]
url2
driver.get(url2)
time.sleep(1)
soup6=BeautifulSoup(driver.page_source,'html.parser')
time.sleep(1)
tags6 = soup6.find_all('div', {"class": "cont_evaluation"})

while True:
    more_unfold = re.compile('none["].*class[=]["].*["][>](.*)[<]span\sclass.*[<][/]a[>]')
    more_review = more_unfold.findall(str(tags6))
    print(more_review)
    if '?????? ?????????' in more_review:
        print('stop')
        break
    else:
        driver.find_element(By.XPATH, '//*[@id="mArticle"]/div[6]/div[2]/a').click()

print('end')

