from xml.etree.ElementTree import parse
import pandas as pd

tree = parse('12월14일_코로나_예방접종현황.xml')
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
    pass
    #row_list = []

    #for item in items.iter('item'):
        #row = []
        #print(item.tag)


    #print(row_list)

#data = get_all_records(items)
columns = get_record_column_names(items)
print(columns)
#df = pd.DataFrame(data,columns = columns )

#print(df)
#df.to_csv('covid_19_ver1.csv', index = False, encoding='cp949')