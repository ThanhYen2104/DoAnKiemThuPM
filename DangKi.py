import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By as B

driver = webdriver.Chrome(executable_path="venv/chromedriver.exe")
driver.maximize_window()
driver.get("https://thegioiskinfood.com/")

#Khai bao input
with open("AccountList.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        L_Name = row["LastName"]
        F_Name = row["FirstName"]
        Email = row["Email"]
        Password = row["CreatePassword"]
        PhoneNumber = row["PhoneNumber"]

# Đóng quảng cáo
driver.implicitly_wait(13)
driver.find_element(B.CLASS_NAME,'windownpopup_close').click()

# Đóng MessagesBox
time.sleep(5)
iframeMes = driver.find_element(B.XPATH, '//*[@id="fb-root"]/div[2]/span/iframe')
driver.switch_to.frame(iframeMes)
time.sleep(4)
driver.find_element(
    B.XPATH,
    "/html/body/div/div/div/div/div/div/div/div/div/div[1]/div[3]/div[2]/div/div",
).click()
driver.switch_to.default_content()
# Đăng kí
driver.find_element(B.CLASS_NAME, "f-header-top-icon-account").click()
driver.find_element(B.XPATH,'//*[@id="sidenav"]/div/div[5]/div[3]/div/div[2]/a').click()


#Điền thông tin
driver.find_element(B.NAME, "customer[last_name]").send_keys(L_Name)
time.sleep(2)
driver.find_element(B.NAME, "customer[first_name]").send_keys(F_Name)
time.sleep(2)
driver.find_element(B.CSS_SELECTOR, "#create_customer > div:nth-child(5) > input").send_keys(Email)
time.sleep(2)
driver.find_element(B.CSS_SELECTOR, "#create_customer > div:nth-child(6) > input").send_keys(Password)
time.sleep(2)
driver.find_element(B.CSS_SELECTOR,'#create_customer > div:nth-child(7) > input').send_keys(PhoneNumber)
time.sleep(2)
driver.find_element(B.XPATH, '//*[@id="create_customer"]/div[6]/button').click()

driver.quit()
