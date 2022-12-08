# 목적: 파이썬 기본 문법으로 특정 행을 필터링하기
import csv
import sys

input_file = 'supplier_data.csv'
output_file = 'output/3output_basic.csv'

with open(input_file, 'r', newline= '') as csv_in_file:
    with open(output_file, 'w', newline= '') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        rilewriter = csv.writer(csv_out_file)
        #header = csv_in_file.readline()
        header = next(filereader)
