from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = 'sales_2013.xls'
output_file = 'output_files/9output_basic.xls'

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('filtered_rows_all_worksheets')

sales_column_index = 3
thredhold = 2000.0

first_worksheet = True
with open_workbook(input_file) as workbook:
    data = []
    for worksheet in workbook.sheets():
        if first_worksheet:
            header_row = worksheet.row_values(0)
            data.append(header_row)
            first_worksheet = False
        for row_index in range(1,worksheet.nrows):
            row_list = []
            sales_amount = worksheet.cell_value(row_index,sales_column_index)
            if sales_amount > thredhold:
                for colum_index in range(worksheet.ncols):
                    cell_value = worksheet.cell_value(row_index, colum_index)
                    cell_type = worksheet.cell_type(row_index, colum_index)
                    if cell_type == 3:
                        date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                        date_cell = date(*date_cell[0:3]).strftime('%Y-%m-%d')
                        row_list.append(date_cell)
                    else:
                        row_list.append(cell_value)
            if row_list:
                data.append(row_list)
    for list_index, output_list in enumerate(data):
        for element_list, element in enumerate(output_list):
            output_worksheet.write(list_index, element_list, element)
output_workbook.save(output_file)