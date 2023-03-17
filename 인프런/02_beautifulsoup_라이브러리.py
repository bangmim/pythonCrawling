import requests
from bs4 import BeautifulSoup

# naver 서버에 대화를 시도
response = requests.get("https://www.naver.com/")

# naver에서 html 줌
html = response.text

# html 번역 선생님으로 수프 만듦
soup = BeautifulSoup(html, 'html.parser')
# select : 다중, select_one : 한 개

# id 값이 NM_set_home_btn인 것 한 개를 찾아
word = soup.select_one('#NM_set_home_btn') 

    # 출력한다
print(word.text)
