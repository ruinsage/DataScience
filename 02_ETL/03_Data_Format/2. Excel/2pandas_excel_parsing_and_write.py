
from xlrd import open_workbook
from xlwt import Workbook
import pandas as pd

input_file = 'sales_2013.xls'
output_file = 'output_files/2pandas_output_basic.xls'

data_frame = pd.read_excel(input_file)
#print(data_frame)

data_frame.to_excel(output_file, index = False)
