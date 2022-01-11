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

    def demo_DangKy(self):
        driver = webdriver.Chrome(executable_path="venv/chromedriver.exe")
        driver.maximize_window()
        driver.get("https://thegioiskinfood.com/")

        #Khai bao input
        with open("QLTKDangKi/AccountList.csv", newline="") as f:
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
        driver.find_element(B.CSS_SELECTOR,'div.sidenav-account-foot-wrap > div.sidenav-account-foot-signup > a').click()


        # Điền thông tin
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

        #Thoát account
        driver.find_element(B.CSS_SELECTOR,
                            '#account-page > div > div > div.account-page-sidebar > '
                            'div.account-sidebar-menu > ul > li:nth-child(6) > a').click()

        driver.quit()


qlTaiKhoan = QuanLyTaiKhoan()
qlTaiKhoan.demo_DangKy()
# qlTaiKhoan.demo_DangNhap()
