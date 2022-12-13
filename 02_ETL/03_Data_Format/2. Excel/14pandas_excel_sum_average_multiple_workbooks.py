import pandas as pd
import glob
import os

input_directory = '.'
input_files = glob.glob(os.path.join(input_directory,'*.xls'))
output_file = 'output_files/14output_pandas.xlsx'

data_frames = []
for data in input_files:
    dataframes = (pd.read_excel(data, sheet_name=None, index_col=None))
    for name, dataframe in dataframes.items():
        #print(dataframe)
        data_frames.append()








#writer = pd.ExcelWriter(output_file)
#all_data_concatenated.to_excel(writer, sheet_name='all_data_all_workbooks', index=False)
#writer.save()