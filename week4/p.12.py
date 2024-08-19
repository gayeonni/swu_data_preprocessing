# 구조 파악
from xml.etree import ElementTree as ET  # ElementTree 라이브러리를 불러온다.

tree = ET.parse('data-text.xml')  # 데이터를 파싱해서 XML 객체로 반환
root = tree.getroot()  # root : XML의 첫번째 태그, root를 반환
print(root)      # root의 tag를 출력
print(list(root))  # root의 child tag를 출력

data = root.find('Data')  # Tag가 data인 child 반환 - find() vs. findall()
print(data)
print(list(data))  # data의 child tag를 출력

for observation in data:  # data 태그 하위의 observation을 하나씩 돌면서
    for item in observation:  # observation 하위의 element를 하나씩 돌면서
        print(item)
        exit()
        print(item.text)  # text : 태그 사이의 텍스트 반환
        print(item.attrib)  # attrib : 태그의 속성을 반환 (딕셔너리 형태로 반환)

        print(item.attrib.keys())  # keys(): 딕셔너리의 키를 반환 - 두 종류가 있음 ['Category', 'Code']와 ['Numeric']

