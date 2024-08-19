import json   # json 라이브러리를 불러온다

json_data = open('data-text.json').read()  # json 파일을 열어 문자열 형태로 반환
data = json.loads(json_data)  # 문자열을 json 형태로 반환

for item in data:   # 데이터에 각 item을 순차적으로 받아서 block 실행
    print(item)     # item 출력

print(type(open('data.csv', 'r', encoding='UTF-8')))
print(type(open('data-text.json').read()))

