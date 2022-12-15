from xml.etree.ElementTree import parse
import pandas as pd

tree = parse('12월13일_시도별_코로나백신_접종현황.xml')
response = tree.getroot()
items = response.find('body')

def get_record_column_names(items):
    for item in items.iter('item'):
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
    for item in items.iter('item'):
        row = []
        first_flag = True
        for rows in item.iter():
            if first_flag == True:
                first_flag = False
                continue
            else:
                #print(rows.text)
                row.append(rows.text)
                #print(row)
        row_list.append(row)
    return row_list

data = get_all_records(items)
#print(data)
columns = get_record_column_names(items)
#print(columns)
df = pd.DataFrame(data,columns = columns )

#print(df)
df.to_csv('12월13일_시도별_코로나백신_접종현황.csv', index = False, encoding='cp949')






















