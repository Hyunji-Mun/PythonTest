from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys  # Keys 모듈 임포트
import time

# ChromeDriver 경로 설정
service = Service(r"C:\Program Files\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# 웹페이지 열기
driver.get("https://google.com")

# 페이지 타이틀 출력
print(driver.title)

# 검색창 요소를 기다리고 가져오기
try:
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    # 검색어 입력
    search_box.send_keys("Python Selenium")

    # Enter 키 누르기
    search_box.send_keys(Keys.RETURN)

    # 결과 페이지의 첫 번째 링크가 로드될 때까지 기다리기
    first_result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h3"))
    )
    print(first_result.text)

finally:
    # 몇 초 후 브라우저 닫기
    time.sleep(5)
    driver.quit()
