import requests
from bs4 import BeautifulSoup
import openpyxl

fpath=r'D:\새 폴더\인프런\STARTCODING CRAWLING\02_파이썬 엑셀 다루기\주식현재가_data.xlsx'
wb= openpyxl.load_workbook(fpath)
# ws=wb.active #현재 활성화된 시트 선택
ws= wb['주식현재가']

# 종목 코드 리스트
codes =[
    '005930',
    '000660',
    '035720'
]

# 데이터 추가하기 위한 엑셀 번호 변수 만들기
row=2
for code in codes:
    # url에 파라미터를 적용할 경우 f-strings를 적어주어야한다
    url=f"https://finance.naver.com/item/sise.naver?code={code}"
    response=requests.get(url)
    html=response.text
    soup=BeautifulSoup(html, 'html.parser')
    price = soup.select_one("#_nowVal").text     #데이터의 id

    price=price.replace(',','')
    print(price)
    ws[f'B{row}'] = int(price)
    row=row+1

wb.save(fpath)