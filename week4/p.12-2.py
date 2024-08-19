# 딕셔너리의 리스트 형태로 반환
from xml.etree import ElementTree as ET # ElementTree 라이브러리를 불러온다.

tree = ET.parse('data-text.xml')  # 데이터를 파싱해서 XML 객체로 반환
root = tree.getroot()  # root : XML의 첫번째 태그, root를 반환
data = root.find('Data')  # Tag가 data인 child 반환 - find() vs. findall()

all_data = []

for observation in data:

    record = {}

    for item in observation:
        lookup_key = list(item.attrib.keys())[0]  # key 리스트의 첫번째 원소를 반환

        if lookup_key == 'Numeric':  # attribte key가 Numeric인지 여부에 따라 다르게 처리
            record_key = 'Numeric'
            record_value = item.attrib['Numeric']  # Numeric 키에 대응하는 값을 저장

        else:
            record_key = item.attrib[lookup_key]
            record_value = item.attrib['Code']  # Code 키에 대응하는 값을 저장

        record[record_key] = record_value  # record 딕셔너리에 key-value 쌍 저장

    all_data.append(record)  # record를 리스트에 저장

print(all_data)
