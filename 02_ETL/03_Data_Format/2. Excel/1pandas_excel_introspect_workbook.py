
import pandas as pd

input_file = 'sales_2013.xls'
output_file = 'output_files/1pandas_output_basic.xls'

data_frame = pd.read_excel(input_file, sheet_name= 'january_2013')
print(data_frame)

data_frame.to_excel(output_file, index = False)