from xlrd import open_workbook

input_file = 'sales_2013.xls'

workbook = open_workbook(input_file)
print(f'Number of worksheet: {workbook.nsheets}')
for worksheet in workbook.sheets():
    print(f'Worksheet name: {worksheet.name}, Rows: {worksheet.nrows}, Columns: {worksheet.ncols}')
print(workbook.nsheets)