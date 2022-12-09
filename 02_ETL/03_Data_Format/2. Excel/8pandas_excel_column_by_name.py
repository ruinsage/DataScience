import pandas as pd

input_file = 'sales_2013.xlsx'
output_file = 'output_files/8output_pandas.xlsx'

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

my_columns = ['Customer ID', 'Purchase Date']

data_frame_column_name = data_frame.loc[:, my_columns]


writer = pd.ExcelWriter(output_file)
data_frame_column_name.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()