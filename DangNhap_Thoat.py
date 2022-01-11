import csv
from selenium import webdriver
from selenium.webdriver.common.by import By as B
import time

class QuanLyTaiKhoan():
    def demo_DangNhap(self):
        driver = webdriver.Chrome(executable_path='venv/chromedriver.exe')
        driver.maximize_window()
        driver.get('https://thegioiskinfood.com/')

        with open("QLTKDangKi/AccountListLogin.csv", newline="") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        Email = row["Email"]
                        Password = row["Password"]

        # Đóng quảng cáo
        driver.implicitly_wait(15)
        driver.find_element(B.CLASS_NAME, 'windownpopup_close').click()

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
        driver.find_element(B.CSS_SELECTOR, '#customer_login > div:nth-child(3) > input').send_keys(Email)
        time.sleep(3)
        driver.find_element(B.CSS_SELECTOR, '#customer_login > div:nth-child(4) > input').send_keys(Password)
        time.sleep(3)
        driver.find_element(B.CSS_SELECTOR, '#customer_login > div:nth-child(6) > button.btn.btn-primary').click()

        #Thoát account
        driver.find_element(B.CSS_SELECTOR,
                            '#account-page > div > div > div.account-page-sidebar > '
                            'div.account-sidebar-menu > ul > li:nth-child(6) > a').click()

        driver.quit()


qlDiaChi = QuanLyTaiKhoan()
qlDiaChi.demo_DangNhap()
