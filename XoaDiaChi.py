import time
from selenium import webdriver
from selenium.webdriver.common.by import By as B

driver = webdriver.Chrome(executable_path="venv/chromedriver.exe")
driver.maximize_window()
driver.get("https://thegioiskinfood.com/")

# Đóng quảng cáo
driver.implicitly_wait(13)
driver.find_element(B.CLASS_NAME,'windownpopup_close').click()

# Đóng MessagesBox
time.sleep(2)
iframeMes = driver.find_element(B.XPATH, '//*[@id="fb-root"]/div[2]/span/iframe')
driver.switch_to.frame(iframeMes)
time.sleep(4)
driver.find_element(
    B.XPATH,
    "/html/body/div/div/div/div/div/div/div/div/div/div[1]/div[3]/div[2]/div/div",
).click()
driver.switch_to.default_content()

# Đăng nhập
driver.find_element(B.CLASS_NAME, "f-header-top-icon-account").click()
driver.find_element(B.CSS_SELECTOR, '#customer_login > div:nth-child(3) > input').send_keys("mailtest3@gmail.com")
time.sleep(3)
driver.find_element(B.CSS_SELECTOR, '#customer_login > div:nth-child(4) > input').send_keys("123456789hihi")
time.sleep(3)
driver.find_element(B.CSS_SELECTOR, '#customer_login > div:nth-child(6) > button.btn.btn-primary').click()

# Xóa địa chỉ
driver.find_element(B.CSS_SELECTOR,
                    '#account-page > div > div.account-page-wrap > div.account-page-sidebar > '
                    'div.account-sidebar-menu > ul > li:nth-child(3) > a').click()
time.sleep(3)
driver.find_element(B.XPATH,
                    "/html/body/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[4]/a[2]",).click()
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(2)

#Thoát account
driver.find_element(B.CSS_SELECTOR,
                    '#account-page > div > div > div.account-page-sidebar > '
                    'div.account-sidebar-menu > ul > li:nth-child(6) > a').click()

driver.quit()
