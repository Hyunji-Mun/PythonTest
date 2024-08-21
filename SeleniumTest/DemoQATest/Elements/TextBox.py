from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ChromeDriver 경로 설정
service = Service(r"C:\Program Files\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# 웹페이지 열기
driver.get("https://demoqa.com/text-box")

# 요소가 로드될 때까지 기다림
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "userName")))

# 텍스트 박스에 입력
driver.find_element(By.ID, "userName").send_keys("MunHyunji")
driver.find_element(By.ID, "userEmail").send_keys("hjmoon9611@naver.com")
driver.find_element(By.ID, "currentAddress").send_keys("인천광역시")
driver.find_element(By.ID, "permanentAddress").send_keys("서울특별시")

# 제출 버튼 클릭
driver.find_element(By.ID, "submit").click()

# 결과 확인을 위해 잠시 대기
time.sleep(60)

# 브라우저 종료
driver.quit()
