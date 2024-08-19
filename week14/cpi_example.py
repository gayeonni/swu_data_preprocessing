import xlrd
import agate
# 부패 인식 지수
from xlrd.sheet import ctype_text


def get_types(row):
    """
    데이터 타입을 자동으로 추출
    :param row: 데이터 타입을 추출할 샘플 행
    :return: 데이터 타입 리스트
    """
    types = []
    for value in row:
        value_type = ctype_text[value.ctype]
        if value_type == 'text':
            types.append(agate.Text())
        elif value_type == 'number':
            types.append(agate.Number())
        elif value_type == 'xldate':
            types.append(agate.Date())
        else:
            types.append(agate.Text())
    return types


def get_clean(old_data, function_to_clean):
    """
    데이터를 주어진 함수로 전처리
    :param old_data: 전처리를 할 대상, agate Table 객체  
    :param function_to_clean: 전처리 함수, 함수 이름
    :return: 전처리 완료된 데이터
    """
    cleand_data = []
    for row in old_data:
        cleaned_row = [function_to_clean(value) for value in row]  # 행의 개별 값에 function_to_clean 함수 적용
        cleand_data.append(cleaned_row)
    return cleand_data


def replace_none(value):
    """
    '-'로 된 값을 None으로 변경
    :param value: 입력 값
    :return: '-'인 경우 None, 아닌 경우 원래 값
    """
    if value == '-':
        return None
    return value


def to_lower_case(value):
    """
    모든 문자를 소문자로 변경
    :param value: 입력 값
    :return: 문자인 경우 소문자, 아닌 경우 원래 값
    """
    if type(value) == str:
        return value.lower()
    return value


# 아동 노동 비율 데이터
# 엑셀 파일 불러오기
workbook_child = xlrd.open_workbook('XLS_Child-labour-database_July-2021.xls')
# print(workbook_child.nsheets)  # 엑셀에 시트의 갯수 출력
# print(workbook_child.sheet_names())  # 엑셀에 시트의 이름 출력

# 첫번째 시트를 저장
sheet_child = workbook_child.sheets()[0]
# print(sheet_child.nrows)  # 시트의 행 갯수 출력
# print(sheet_child.row_values(0))  # 시트의 첫번째 행 출력

# for r in range(sheet_child.nrows):  # 모든 행을 돌면서, 행 번호와 행의 값 출력
#     print(r, sheet_child.row(r))

# 데이터 전처리
rows_child = [sheet_child.row_values(r) for r in range(11, 213)]  # 전처리 1 : 데이터 행으로만 구성된 데이터 반환 | 11번째 행부터 213행 이전까지!!
cleaned_rows_child = get_clean(rows_child, replace_none)  # 전처리 2 : '-' 기호를 None으로 변환
cleaned_rows_child = get_clean(cleaned_rows_child, to_lower_case)  # 전처리 3 : 영어를 소문자로 변환
# print(cleaned_rows_child)  # 최종 데이터 출력

# agate Table 객체로 저장
titles_child = ['Countries and areas', 'Total', 'Tag_1', 'Male', 'Tag_2', 'Female', 'Tag_3', 'Data source']  # 컬럼명
types_child = [agate.Text(), agate.Number(), agate.Text(), agate.Number(), agate.Text(), agate.Number(), agate.Text(), agate.Text()]  # 컬럼별 데이터 타입
table_child = agate.Table(cleaned_rows_child, titles_child, types_child)  # agate의 Table 객체 (데이터, 칼럼, 타입) 생성
# table_child.print_table(max_columns=8)  # 최종 table 출력
# print(len(table_child.rows))  # 칼럼 제외 데이터 행의 개수!

# 부패 인식 지수
# 데이터 불러오기
workbook_cpi = xlrd.open_workbook('CPI2020_GlobalTablesTS_210125.xls')
sheet_cpi = workbook_cpi.sheets()[0]
# for r in range(sheet_cpi.nrows):  # 모든 행을 돌면서, 행 번호와 행의 값 출력
#     print(r, sheet_cpi.row(r))    # 0부터 182까지 출력

rows_cpi = [sheet_cpi.row_values(r) for r in range(3, sheet_cpi.nrows)]
cleaned_rows_cpi = get_clean(rows_cpi, to_lower_case)  # 소문자로 변환

# agate Table 객체로 저장
titles_cpi = sheet_cpi.row_values(2)  # 3행(인덱스는 2)에 칼럼명 존재! 이걸 가져옴
# print(titles_cpi)
types_cpi = get_types(sheet_cpi.row(3))  # get_types 함수로 타입을 가져옴
table_cpi = agate.Table(cleaned_rows_cpi, titles_cpi, types_cpi)
# table_cpi.print_table()  # 최종 table 출력
# print(len(table_cpi.rows))  # 180 출력

# 데이터 전처리
# 테이블 조인                              # join할 테이블, 칼럼, 칼럼
table_child_cpi = table_child.join(table_cpi, 'Countries and areas', 'Country', inner=True)
# print(table_child_cpi.column_names)
# for row in table_child_cpi:
#     print(row['Countries and areas'], row['Total'], row['CPI score 2020'])
# print(len(table_child_cpi.rows))  # 164 출력

# 대륙 정보 추가
import json

# json load
with open('earth.json') as json_file:
    country_json = json.load(json_file)

# agate table generation
country_array = [(r['name'], r['parent']) for r in country_json]  # json을 array 형태로 변환
# print(country_array)

# agate table 생성
titles_country = ['country', 'continent']
types_country = [agate.Text(), agate.Text()]
table_country = agate.Table(country_array, titles_country, types_country)
# table_country.print_table()  # 테이블 출력
# print(len(table_country.rows))  # 631 출력

# join
table_child_cpi_country = table_country.join(table_child_cpi, 'country', 'Countries and areas', inner=True)
# table_child_cpi_country.print_table()  # 테이블 출력
# print(len(table_child_cpi_country.rows))  # 148 출력

# null 값 처리 : 제거
table_child_cpi_country_not_null = table_child_cpi_country.where(lambda r: r['Total'] is not None)

# outlier 처리
import agatestats  # pip install agate-stats

table_child_cpi_country_not_null_no_outliers = table_child_cpi_country_not_null.stdev_outliers('Total', deviations=2, reject=False)

# print(table_child_cpi_country_not_null.aggregate(agate.Mean('Total')))  # 함수 안에 인자에 해당하는 함수로 데이터 값을 요약 | 토탈 컬럼의 평균 값!
# print(table_child_cpi_country_not_null.aggregate(agate.StDev('Total')))  # 토탈 컬럼의 표준편차 값!

# print(len(table_child_cpi_country_not_null.rows))  # 71
# print(len(table_child_cpi_country_not_null_no_outliers.rows))  # 69

# outlier 제거 후 평균과 표준편차
# print(table_child_cpi_country_not_null_no_outliers.aggregate(agate.Mean('Total')))
# print(table_child_cpi_country_not_null_no_outliers.aggregate(agate.StDev('Total')))

# print(table_child_cpi_country_not_null_no_outliers.print_table())

# Sorting
most_child_labour = table_child_cpi_country_not_null_no_outliers.order_by('Total', reverse=True)  # 가장 높은 아동 노동률을 보유한 국가 나열
# for row in most_child_labour:
#     print(row['country'], row['continent'], row['Total'], row['CPI score 2020'])

# correlation
correlation_value = agatestats.aggregations.PearsonCorrelation('Total', 'CPI score 2020').run(table_child_cpi_country_not_null_no_outliers)
# print(correlation_value)  # 음수 = 음의 상관관계 = 한 변수가 증가(감소)하면 다른 변수는 감소(증가)
