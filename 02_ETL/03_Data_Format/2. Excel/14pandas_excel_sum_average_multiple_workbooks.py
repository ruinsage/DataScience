import pandas as pd
import glob
import os

input_directory = '.'
input_files = glob.glob(os.path.join(input_directory,'*.xls'))
output_file = 'output_files/14output_pandas.xlsx'

data_frames = []
for file in input_files:
    files = pd.read_excel(file, sheet_name=None, index_col=None)

    for name, worksheet in files.items():
        print(name)
        #print(worksheet['Sale Amount'].sum())
        workbook_total_sales = worksheet['Sale Amount'].sum()
        number_of_sales = len(worksheet['Sale Amount'])
        #print(number_of_sheet)
        workbook_average_sales = workbook_total_sales / number_of_sales
        #print(average_sales)








#writer = pd.ExcelWriter(output_file)
#all_data_concatenated.to_excel(writer, sheet_name='all_data_all_workbooks', index=False)
#writer.save()