import glob
import os
import pandas as pd

input_directory = '.'
input_files = glob.glob(os.path.join(input_directory,'*.xls'))
Workbook = []
for data in input_files:
    print(f"Workbook: {os.path.basename(data)}")
    Workbook.append(pd.read_excel(data, sheet_name=None, index_col=None))
    for dataframe in Workbook:
        print(f"Number of worksheets: {len(Workbook)}")
        for name,data in dataframe.items():

            print(f'Worksheet name: {name}\t Rows:{len(data.index)}\t Columns:{len(data.columns)}')

print(f'Number of Excel workbooks: {len(Workbook)}')