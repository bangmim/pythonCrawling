from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options=Options()
chrome_options.add_experimental_option("detach",True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
browser= webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소로 이동
browser.get("https://www.naver.com")
browser.implicitly_wait(10) # 로딩이 끝날때까지 10초까지는 기다려줌

# 쇼핑 메뉴 클릭
menu=browser.find_element(By.CSS_SELECTOR,"a.nav.shop") 
menu.click()
time.sleep(2)

# 검색창 클릭
search=browser.find_element(By.CSS_SELECTOR,'input._searchInput_search_text_3CUDs') 
search.click()

#검색어 입력
search.send_keys('아이폰14')
search.send_keys(Keys.ENTER)

# 스크롤 전 높이
before_h = browser.execute_script("return window.scrollY")

# 무한 스크롤   //반복문
while True:
    # 맨 아래로 스크롤을 내린다.
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
    
    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1)
    
    # 스크롤 후 높이
    after_h=browser.execute_script("return window.scrollY")
    
    if after_h == before_h:
        break
    before_h=after_h

# 상품 정보 div
items = browser.find_elements(By.CSS_SELECTOR, ".basicList_info_area__TWvzp")

for item in items:
    name=item.find_element(By.CSS_SELECTOR,".basicList_title__VfX3c").text
    try:
        price = item.find_element(By.CSS_SELECTOR, ".price_price__LEGN7").text
    except:
        price="판매중단"
    link=item.find_element(By.CSS_SELECTOR,".basicList_title__VfX3c > a").get_attribute('href')
    # link = item.find_element(By.CSS_SELECTOR, ".basicList_link__JLQJf").get_attribute('href')
   # get_attribute(속성명)
    # print(name, price, link)
    print("name: ",name,"\nprice:",price,"\nlink: ",link)

# 크롤링 결과 csv 파일에 저장하기