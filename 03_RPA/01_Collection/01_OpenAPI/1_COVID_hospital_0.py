## 목적: 수동으로 OpenAPI 호출하기
# OpenAPI 호출/응답 이해하기

# base URL
# http://apis.data.go.kr/B551182/pubReliefHospService/getpubReliefHospList

# OpenAPI 호출방식
# baseURL?파라미터1=값&파라메터2=값....
# servicekey= 공공데이터포털-마이페이지-해당 활용신청 서비스 정보란
# 그 외 파라메터는 참고문서 참조
# ServiceKey= pnWEl7Muj6PpSyrC35SaqRjYnKAAL0xedWtDdUQDmfsWvqDxK1ORAkSg2/axQsJNCKZjQlf98A3TRAuuIzJ0GQ==

# http://apis.data.go.kr/B551182/pubReliefHospService/getpubReliefHospList?ServiceKey=pnWEl7Muj6PpSyrC35SaqRjYnKAAL0xedWtDdUQDmfsWvqDxK1ORAkSg2/axQsJNCKZjQlf98A3TRAuuIzJ0GQ==&numOfRows=10&pageNo=1

# TPS (Transaction Per Second):
# Transaction: 처리 데이터
