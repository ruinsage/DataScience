import pandas as pd

input_file = 'sales_2013.xlsx'
output_file = 'output_files/7output_pandas.xlsx'

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

data_frame_column_index = data_frame.iloc[:,[1,4]]

writer = pd.ExcelWriter(output_file)
data_frame_column_index.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()