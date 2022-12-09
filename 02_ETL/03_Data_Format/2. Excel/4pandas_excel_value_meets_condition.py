import pandas as pd

input_file = 'sales_2013.xls'
output_file = 'output_files/4pandas_output_basic.xls'

data_frame = pd.read_excel(input_file, sheet_name= 'january_2013')

data_frame2 = data_frame.loc[(data_frame['Sale Amount'] > 1400.0), :]
print(data_frame2)

writer = pd.ExcelWriter(output_file)
data_frame2.to_excel(writer, sheet_name= 'january_2013', index = False)
writer.save()