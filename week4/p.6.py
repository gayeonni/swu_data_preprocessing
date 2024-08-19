import csv                  # 파이썬 표준 라이브러리 csv 불러오기

csv_file = open('data.csv', 'r', encoding='UTF-8') # open() 함수를 파일 위치와 파일 오픈 모드를 인자로 실행, 열린 파일을 csv_file 변수에 저장
# reader = csv.reader(csv_file)        # Option 1 : csv 파일 형식의 파일 리더 함수 실행, reader 객체는 데이터의 행을 담고 있는 파이썬 컨테이너
reader = csv.DictReader(csv_file)   # Option 2 : 리스트 행을 딕셔너리 행으로 표현

for row in reader:  # reader의 행을 하나씩 row에 저장하여 block을 반복해서 실행
    print(row)      # row 변수에 저장된 값을 출력
    