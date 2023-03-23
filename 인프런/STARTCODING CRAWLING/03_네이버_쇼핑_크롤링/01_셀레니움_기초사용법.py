from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
'''
# 브라우저 생성
browser =  webdriver.Chrome('D:\새 폴더\chromedriver.exe')

# 웹사이트 열기
browser.get('https://www.naver.com')
browser.implicitly_wait(10) # 로딩이 끝날때까지 10초까지는 기다려줌

# 쇼핑 메뉴 클릭
browser.find_element_by_css_selector('a.nav.shop').click()
time.sleep(2)

# 검색창 클릭
search = browser.find_element_by_css_selector('input._searchInput_search_text_3CUDs')
search.click()

#검색어 입력
search.send_keys('아이폰13')
search.send_keys(Keys.ENTER)
'''

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
driver= webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소로 이동
driver.get("https://www.naver.com")
driver.implicitly_wait(10) # 로딩이 끝날때까지 10초까지는 기다려줌

# 쇼핑 메뉴 클릭
menu=driver.find_element(By.CSS_SELECTOR,"a.nav.shop") 
menu.click()
time.sleep(2)

# 검색창 클릭
search=driver.find_element(By.CSS_SELECTOR,'input._searchInput_search_text_3CUDs') 
search.click()

#검색어 입력
search.send_keys('아이폰13')
search.send_keys(Keys.ENTER)
