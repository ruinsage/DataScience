import pandas as pd

input_file = 'sales_2013.xlsx'
output_file = 'output_files/5output_pandas.xlsx'

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

data_frame_value_meets_condition = \
	data_frame[(data_frame['Purchase Date'] == '01/24/2013') | (data_frame['Purchase Date'] == '01/31/2013') ]

writer = pd.ExcelWriter(output_file)
data_frame_value_meets_condition.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()