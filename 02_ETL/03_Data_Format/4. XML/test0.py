from xml.etree.ElementTree import parse
import pandas as pd

tree = parse('students_zero.xml')
note = tree.getroot()

columns = ['name','sex','age','major']
student_list = []
for info in note.iter('student'):
    student = []
    student.append(info.get('name'))
    student.append(info.get('sex'))
    student.append(info.find('age').text)
    student.append(info.find('major').text)
    student_list.append(student)

student_df = pd.DataFrame(student_list,
                          index = list(range(3)),
                          columns = columns)

student_df.to_csv('student_zero.csv', index= False)