import requests
from bs4 import BeautifulSoup

# 종목 코드 리스트
codes =[
    '005930',
    '000660',
    '035720'
]

for code in codes:
    # url에 파라미터를 적용할 경우 f-strings를 적어주어야한다
    url=f"https://finance.naver.com/item/sise.naver?code={code}"
    response=requests.get(url)
    html=response.text
    soup=BeautifulSoup(html, 'html.parser')
    price = soup.select_one("#_nowVal").text     #데이터의 id

    price=price.replace(',','')
    print(price)