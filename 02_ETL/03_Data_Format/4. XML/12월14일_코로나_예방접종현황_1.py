from xml.etree.ElementTree import parse
import pandas as pd

def covid_19_12_14():
    tree = parse('12월14일_코로나_예방접종현황.xml')
    response = tree.getroot()
    items = response.find('body')
    row_list = []

    for item in items.iter('item'):
        row = []
        #print(item.tag)
        row.append(item.find('tpcd').text)
        row.append(item.find('firstCnt').text)
        row.append(item.find('secondCnt').text)
        row.append(item.find('thirdCnt').text)
        row.append(item.find('fourCnt').text)
        row.append(item.find('winCnt').text)
        row.append(item.find('vrate').text)
        row.append(item.find('wrate').text)
        row_list.append(row)

    #print(row_list)
    columns = ['tpcd','firstCnt','secondCnt','thirdCnt','fourCnt','winCnt','vrate','wrate']
    return pd.DataFrame(row_list,columns = columns)

df = covid_19_12_14()
#print(df)
df.to_csv('covid_19_ver1.csv', index = False, encoding='cp949')
