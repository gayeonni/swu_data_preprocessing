import xlrd
import agate


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
    ''로 된 값을 None으로 변경
    :param value: 입력 값
    :return: ''인 경우 None, 아닌 경우 원래 값
    """
    if value == '':
        return None
    return value




# 동물 등록 현황 데이터
# 엑셀 파일 불러오기
workbook_animal = xlrd.open_workbook('animal.xls')
print(workbook_animal.nsheets)  # 엑셀에 시트의 갯수 출력
print(workbook_animal.sheet_names())  # 엑셀에 시트의 이름 출력

# 첫번째 시트를 저장
sheet_animal = workbook_animal.sheets()[0]
print(sheet_animal.nrows)  # 시트의 행 갯수 출력 396 출력
print(sheet_animal.row_values(0))  # 시트의 첫번째 행 출력

for r in range(sheet_animal.nrows):  # 모든 행을 돌면서, 행 번호와 행의 값 출력
    print(r, sheet_animal.row(r))    # 0부터 시작하기 때문에 마지막 인덱스 395


# 데이터 전처리
rows_animal = [sheet_animal.row_values(r) for r in range(1, 396)]  # 전처리 1 : 데이터 행으로만 구성된 데이터 반환 | 1행부터 396행 이전까지!!
cleaned_rows_animal = get_clean(rows_animal, replace_none)  # 전처리 2 : 공백인 경우 None으로 변환
print(cleaned_rows_animal)  # 최종 데이터 출력


# agate Table 객체로 저장
titles_animal = ['시군명', '동물원명', '정제도로명주소', '정제지번주소', '운영구분', '규모(m^2)', '종수', '개체수', '수의사수', '사육사수', '정제우편번호', '정제WGS84위도', '정제WGS84경도']  # 컬럼명
types_animal = [agate.Text(), agate.Text(), agate.Text(), agate.Text(), agate.Text(), agate.Number(), agate.Number(), agate.Number(), agate.Number(), agate.Number(), agate.Number(), agate.Number(), agate.Number()]  # 컬럼별 데이터 타입
table_animal = agate.Table(cleaned_rows_animal, titles_animal, types_animal)  # agate의 Table 객체 (데이터, 칼럼, 타입) 생성
table_animal.print_table(max_columns=8)  # 최종 table 출력
print(len(table_animal.rows))  # 칼럼 제외 데이터 행의 개수!

for row in table_animal:
    print(row['개체수'], row['수의사수'])


# null 값 처리 : 제거
table_animal_not_null = table_animal.where(lambda r: r['개체수'] is not None)


# outlier 처리
import agatestats  # pip install agate-stats

table_animal_not_null_no_outliers = table_animal_not_null.stdev_outliers('개체수', deviations=2, reject=False)

print(table_animal_not_null.aggregate(agate.Mean('개체수')))  # 함수 안에 인자에 해당하는 함수로 데이터 값을 요약 | 토탈 컬럼의 평균 값!
print(table_animal_not_null.aggregate(agate.StDev('개체수')))  # 토탈 컬럼의 표준편차 값!

print(len(table_animal_not_null.rows))  # 292
print(len(table_animal_not_null_no_outliers.rows))  # 274

# outlier 제거 후 평균과 표준편차
print(table_animal_not_null_no_outliers.aggregate(agate.Mean('개체수')))
print(table_animal_not_null_no_outliers.aggregate(agate.StDev('개체수')))

print(table_animal_not_null_no_outliers.print_table())

# Sorting
most_animal = table_animal_not_null_no_outliers.order_by('개체수', reverse=True)  # 가장 높은 개체수 순으로 출력
for row in most_animal:
    print(row['개체수'], row['수의사수'])

# correlation
correlation_value = agatestats.aggregations.PearsonCorrelation('개체수', '수의사수').run(table_animal_not_null_no_outliers)
print(correlation_value)  # 음수 = 음의 상관관계 = 한 변수가 증가(감소)하면 다른 변수는 감소(증가)
exit()
