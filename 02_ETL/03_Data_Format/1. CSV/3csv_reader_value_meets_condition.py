# 목적: 파이썬 기본 문법으로 특정 행을 필터링하기
import csv
import sys

input_file = 'supplier_data.csv'
output_file = 'output_files/3output_basic.csv'

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		header = next(filereader) # next() 현재라인을 읽고 다름 라인으로 파일 포인터를 이동시킨다 (readline()과 같다)
		filewriter.writerow(header)
		for row_list in filereader:
			supplier = str(row_list[0]).strip() # 검색어 변수
			# cost = str(row_list[3]).strip('$').replace(',', '')
			cost = str(row_list[3]).strip('$') # 검색어2 변수

			# if (float(cost) > 600.00) and (float(cost) < 620.00): # cost의 가격이 600보다 크고 620보다 작은 행. 필터링 조건
			# 	filewriter.writerow(row_list)

			# 같은 결과의 검색 => Supplier Name열의 값이 Z인 경우
			# if supplier == 'Supplier Z':
			# 	filewriter.writerow(row_list)

			# 복합검색
			if supplier == 'Supplier Y' and float(cost) < 200.0:
				filewriter.writerow(row_list)