from xml.etree.ElementTree import parse
import pandas as pd

tree = parse('전국공공시설개방정보표준데이터.xml')
response = tree.getroot()
items = response.find('records')

def get_record_column_names(items):
    for item in items.iter('record'):
        colum_list = []
        first_flag = True
        for column in item.iter():
            if first_flag == True :
                first_flag = False
                continue
            else:
                colum_list.append(column.tag)
    return colum_list

def get_all_records(items):
    row_list = []
    for item in items.iter('record'):
        row = []
        first_flag = True
        for row_data in item.iter():
            if first_flag == True:
                first_flag = False
                continue
            #print(rows.text)
            row.append(row_data.text)
            #print(row)
        row_list.append(row)
    return row_list

data = get_all_records(items)
#print(data)
columns = get_record_column_names(items)
#print(columns)
df = pd.DataFrame(data,columns = columns )

#print(df)
df.to_csv('전국공공시설개방정보표준데이터.csv', index = False, encoding='cp949')