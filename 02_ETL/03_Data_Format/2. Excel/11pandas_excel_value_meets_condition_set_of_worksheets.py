import pandas as pd

input_file = 'sales_2013.xlsx'
output_file = 'output_files/11output_pandas.xlsx'

data_frame = pd.read_excel(input_file, sheet_name=None, index_col=None)

my_sheets = ['january_2013','february_2013'] # january_2013,february_2013
threshold = 1900.0
sales_column_index = 3
#print(data_frame)
#print(data_frame['january_2013'])

row_list = []
for name, data in data_frame.items():
    if name in my_sheets:
        #print(name)
        row_list.append(data.loc[data['Sale Amount'] > threshold, :])
    #print(row_list)
filtered_rows = pd.concat(row_list, axis= 0, ignore_index= True)
#print(filtered_rows)

writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()