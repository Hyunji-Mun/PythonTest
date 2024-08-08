from appium import webdriver
from appium.options.common.base import AppiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Appium 서버와 통신하기 위한 Desired Capabilities 설정
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "14",
    "appium:deviceName": "R3CR5062Q0J",
    "appium:automationName": "uiautomator2",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True,
    "appium:appPackage": "com.android.chrome",
    "appium:appActivity": "com.google.android.apps.chrome.Main"
})

# Appium 서버에 연결
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# 크롬 앱이 실행되도록 대기
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "com.android.chrome:id/signin_fre_dismiss_button")))

# "계정 없이 사용" 버튼 클릭
dismiss_button_selector = "com.android.chrome:id/signin_fre_dismiss_button"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, dismiss_button_selector))).click()

# Chrome의 개선된 광고 개인 정보 보호 페이지 "확인" 버튼 클릭
ack_button_selector = "com.android.chrome:id/ack_button"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, ack_button_selector))).click()

# Naver 웹 페이지 열기
driver.get('https://naver.com')


# 크롬 앱 종료
#driver.quit()
