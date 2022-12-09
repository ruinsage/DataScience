import pandas as pd

input_file = 'sales_2013.xlsx'
output_file = 'output_files/9output_pandas.xlsx'

data_frame = pd.read_excel(input_file, sheet_name=None, index_col=None)
#print(data_frame)

sales_column_index = 3
threshold = 2000.0

row_list = []
for name, data in data_frame.items():
    row_list.append(data.loc[data['Sale Amount'] > threshold,:])
filtered_row = pd.concat(row_list, axis= 0, ignore_index= True)
#print(row_list)
#print(filtered_row)

writer = pd.ExcelWriter(output_file)
filtered_row.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()