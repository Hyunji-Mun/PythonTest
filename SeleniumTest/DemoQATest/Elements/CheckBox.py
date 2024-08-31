from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ChromeDriver 경로 설정
service = Service(r"C:\Program Files\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    # 사이트 열기
    driver.get("https://demoqa.com/checkbox")

    # 'Expand all' 버튼 클릭
    expand_all_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[title="Expand all"]'))
    )
    expand_all_button.click()

    # 'Home' 체크박스가 로드될 때까지 기다리기
    home_checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="tree-node"]/ol/li/span/label/span[1]'))
    )

    # 'Home' 체크박스 클릭 (체크 상태)
    home_checkbox.click()

    # 잠시 대기 (2초)
    time.sleep(2)

    # 'Home' 체크박스 클릭 (체크 해제)
    home_checkbox.click()

    # 잠시 대기 (2초)
    time.sleep(2)

    # 'Collapse all' 버튼 클릭
    collapse_all_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[title="Collapse all"]'))
    )
    collapse_all_button.click()

    # 잠시 대기 (2초)
    time.sleep(2)

    # 'Expand all' 버튼 클릭
    expand_all_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[title="Expand all"]'))
    )
    expand_all_button.click()

    # 잠시 대기 (2초)
    time.sleep(2)

    # 'Downloads' 체크박스 클릭
    downloads_label = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/span/label'))
    )
    downloads_label.click()

    # 잠시 대기 (2초) - 작업 완료를 위한 대기
    time.sleep(2)

    # 'Word File' 체크박스 클릭 (해제하기)
    word_file_label = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[1]/span/label'))
    )
    word_file_label.click()

    # 잠시 대기 (2초) - 작업 완료를 위한 대기
    time.sleep(2)

finally:
    # 웹 드라이버 종료
    driver.quit()
