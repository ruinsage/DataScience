import json
import pandas as pd

def open_json(file_name, encoding):
    with open(file_name, encoding = encoding) as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        json_data = json.loads(json_string)
    return json_data

json_data = open_json('student_zero2.json','cp949')
#print(json_data)

data = []
column_list = []
is_first = True
for student in json_data['response'] ['body']['student_list']:
    row_list = []
    for key, value in student.items():
        if is_first:
            #print(key)
            column_list.append(key)
        row_list.append(value)
        #print(value)
    data.append(row_list)
    is_first = False

print(data)