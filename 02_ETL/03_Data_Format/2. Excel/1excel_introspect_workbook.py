# xlrd 모듈 설치
# 목적: 엑셀 기본 정보 확인
import sys
from xlrd import open_workbook

input_file = 'sales_2013.xls'

# 파이썬에서는 워크시트를 모두 포함한 엑셀 데이터를 workbook으로 표기한다.
# 워크시트 : 단일 목적으로 데이터를 수집한 데이터셋
workbook = open_workbook(input_file)
print('Number of worksheets:', workbook.nsheets)
for worksheet in workbook.sheets(): # sheets() 워크북 안의 모든 워크시트들을 리스트로 반환
	print("Worksheet name:", worksheet.name, "\tRows:", worksheet.nrows, "\tColumns:", worksheet.ncols)
print(workbook.nsheets)
