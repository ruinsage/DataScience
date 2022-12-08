
import pandas as pd
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = 'sales_2013.xls'
output_file = 'output_files/9pandas_output_basic.xls'
