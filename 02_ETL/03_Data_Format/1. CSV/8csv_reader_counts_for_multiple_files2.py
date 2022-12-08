import csv
import glob
import os

input_path = '.'
file_counter = 0

for input_file in glob.glob(os.path.join(input_path,'sales_*')):
    row_counter = 1
    with open(input_file, 'r', newline= '') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        header = next(filereader)

        for row in filereader:
            row_counter += 1

        print(f'{os.path.basename(input_file)}, {row_counter}, {len(header)}')
        file_counter += 1
print(f'Number of files : {file_counter}')
