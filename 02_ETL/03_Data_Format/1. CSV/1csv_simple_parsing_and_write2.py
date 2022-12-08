# 목적: CSV 파일 읽고 쓰기
input_file = 'supplier_data.csv'
output_file = 'output_files/1output_index_false2.csv'

# with open(input_file, 'r', newline = '') as filereader:
with open(input_file, 'r') as filereader:
    with open(output_file, 'w', newline = '') as filewriter:
        # readline() 현재 줄을 읽고 파일 포인터의 위치가 다음 라인으로 이동한다.
        # 파일 포인터는 현재 파일에서 읽기 또는 쓰기 작업을 하기 위한 텍스트 위치이다.
        header = filereader.readline() # 헤더행

        # 데이터 분석을 위한 기본 템플릿
        header = header.strip() # 헤더행 양끝에 공백문자가 있는 경우를 대비하여 strip()
        header_list = header.split(',') # 열단위로 구분하기 위해서 ,로 분리
        print(header_list)
        filewriter.write(','.join(map(str,header_list))+'\n')

        # 데이터 분석이 필요하지 않은 경우에는 아래와 같이 코드를 간소화할 수 있다.
        #filewriter.write(header)

        for row in filereader:
            # 데이터 분석을 위한 기본 템플릿
            row = row.strip()
            row_list = row.split(',')
            print(row_list)
            filewriter.write(','.join(map(str,row_list))+'\n')

