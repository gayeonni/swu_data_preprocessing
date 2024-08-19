from urllib import request
from bs4 import BeautifulSoup

naver = request.urlopen('http://naver.com')
naver_html = naver.read()  # 열린 페이지에서 html 문서 읽기

soup = BeautifulSoup(naver_html, 'html.parser')  # html tree 형태로 문서를 parse

print(soup.title.string)

print(soup.find_all('a'))
