import glob
import os
import pandas as pd

input_directory = '.'
input_files = glob.glob(os.path.join(input_directory,'*.xls'))
output_file = 'output_files/13output_pandas.xls'

Workbook = []
for data in input_files:
    files = (pd.read_excel(data, sheet_name=None, index_col=None))
    #print(files)
    for name, dataframe in files.items():
        Workbook.append(dataframe)
        #print(dataframe)
#all_dataframe = pd.concat(Workbook, axis= 0, ignore_index= True)
print(Workbook)
#writer = pd.ExcelWriter(output_file)
#all_dataframe.to_excel(writer, sheet_name='all_data_all_workbooks', index=False)
#writer.save()