import pandas as pd

input_file = 'sales_2013.xlsx'
output_file = 'output_files/10output_pandas.xlsx'

data_frame = pd.read_excel(input_file, sheet_name=None, index_col=None)

my_columns = ['Customer Name', 'Sale Amount']

column_list = []
for name, data in data_frame.items():
    column_list.append(data.loc[:,my_columns])
#print(column_list)
filtered_columns = pd.concat(column_list, axis= 0, ignore_index= True)
#print(filtered_columns)

writer = pd.ExcelWriter(output_file)
filtered_columns.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()