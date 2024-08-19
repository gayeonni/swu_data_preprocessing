from urllib import request  # urllib 패키지에 있는 request 모듈 호출
from bs4 import BeautifulSoup

google = request.urlopen('http://www.google.com')  # request 모듈에 urlopen() 함수를 이용하여 주어진 URL 요청
google_html = google.read()  # 열린 페이지에서 html 문서 읽기

soup = BeautifulSoup(google_html, 'html.parser')  # html tree 형태로 문서를 parse
print(soup.prettify())

print(soup.title)  # 태그이름으로 바로 접근

print(soup.title.name)  # 태그의 이름 반환

print(soup.title.string)  # 태그 사이의 텍스트 반환

print(soup.title.get_text())  # 태그 사이의 텍스트 반환


print(soup.title.parent.name)  # parent 부모, contents 자식 목록

print(soup.head.contents)

print(soup.find_all('a'))  # 특정 조건을 만족하는 엘레멘트 반환

print(soup.find_all('p'))

