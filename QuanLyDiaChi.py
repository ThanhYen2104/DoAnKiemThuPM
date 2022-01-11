import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By as B
from selenium.webdriver.support.ui import Select as S

class QuanLyDiaChi():
    def demo_ThemDiaChiMoi(self):
        driver = webdriver.Chrome(executable_path='venv/chromedriver.exe')
        driver.maximize_window()
        driver.get('https://thegioiskinfood.com/')

        with open("QLTKDangKi/AccountListLogin.csv", newline="") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        Email = row["Email"]
                        Password = row["Password"]

        # Đóng quảng cáo
        driver.implicitly_wait(13)
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

        # Thêm địa chỉ mới
        driver.find_element(B.CSS_SELECTOR,
                            '#account-page > div > div.account-page-wrap > div.account-page-sidebar > '
                            'div.account-sidebar-menu > ul > li:nth-child(3) > a').click()
        driver.find_element(B.CSS_SELECTOR,
                            '#account-page > div > div > div.account-page-content > '
                            'div.account-page-detail.account-page-addresses > '
                            'div:nth-child(2) > div.new-address-btn > a').click()
        # driver.find_element(B.ID, 'address_last_name_new').send_keys("Le")
        # time.sleep(3)
        # driver.find_element(B.ID, 'address_first_name_new').send_keys("Ji")
        time.sleep(3)
        driver.find_element(B.ID, 'address_company_new').send_keys("TNHH 55555555")
        time.sleep(3)
        driver.find_element(B.ID, 'address_phone_new').send_keys("0825341236")
        time.sleep(3)
        driver.find_element(B.ID, 'address_address1_new').send_keys("123 Hoang Van Thu, Q.Phu Nhuan, TP.Ho Chi Minh")
        time.sleep(3)
        countryType = S(driver.find_element(B.ID, 'address_country_new'))
        countryType.select_by_value('Vietnam')
        time.sleep(3)
        cityType = S(driver.find_element(B.ID, 'address_province_new'))
        cityType.select_by_value('Hồ Chí Minh')
        time.sleep(3)
        driver.find_element(B.CSS_SELECTOR,
                            '#address_form_new > div:nth-child(5) > button').click()

        # Thoát account
        driver.find_element(B.CSS_SELECTOR,
                            '#account-page > div > div > div.account-page-sidebar > '
                            'div.account-sidebar-menu > ul > li:nth-child(6) > a').click()

        driver.quit()

    def demo_SuaDiaChi(self):
        driver = webdriver.Chrome(executable_path='venv/chromedriver.exe')
        driver.maximize_window()
        driver.get('https://thegioiskinfood.com/')

        with open("QLTKDangKi/AccountListLogin.csv", newline="") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        Email = row["Email"]
                        Password = row["Password"]

        # Đóng quảng cáo
        driver.implicitly_wait(13)
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

        # Sửa địa chỉ
        driver.find_element(B.CSS_SELECTOR,
                            '#account-page > div > div.account-page-wrap > div.account-page-sidebar > '
                            'div.account-sidebar-menu > ul > li:nth-child(3) > a').click()
        # Tìm đến phần tử sửa của địa chỉ phụ
        driver.find_element(B.CSS_SELECTOR,
                            'div.address-item-action > a:nth-child(1)').click()
        time.sleep(4)
        driver.find_element(B.XPATH,'/html/body/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/form/div[1]/div[1]/input').clear()
        driver.find_element(B.CLASS_NAME,'/html/body/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/form/div[1]/div[1]/input').send_keys("Le")
        time.sleep(3)
        driver.find_element(B.XPATH,
                            '/html/body/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/form/div[1]/div[2]/input').clear()
        driver.find_element(B.XPATH,
                            '/html/body/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/form/div[1]/div[2]/input').send_keys("Ji")
        time.sleep(3)
        driver.find_element(B.XPATH,
                            '/html/body/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/form/div[1]/div[3]/input').send_keys("TNHH 555555")
        time.sleep(3)
        driver.find_element(B.XPATH,
                            '/html/body/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/form/div[1]/div[3]/input').send_keys("0832325462")
        time.sleep(3)
        driver.find_element(B.XPATH,
                            '/html/body/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/form/div[1]/div[5]/input').send_keys("220 Nguyen Kiem, Q.Go Vap, TP.HCM")
        time.sleep(3)
        countryType = S(driver.find_element(B.XPATH,
                                          '/html/body/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/form/div[1]/div[7]/select'))
        countryType.select_by_value("Vietnam")
        time.sleep(3)
        provinceType = S(driver.find_element(B.XPATH,
                                           '/html/body/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/form/div[1]/div[8]/select'))
        provinceType.select_by_value("Hồ Chí Minh")
        time.sleep(3)
        driver.find_element(B.CSS_SELECTOR,
                            'div.edit-address > div:nth-child(5) > button').click()

        # Thoát account
        driver.find_element(B.CSS_SELECTOR,
                            '#account-page > div > div > div.account-page-sidebar > '
                            'div.account-sidebar-menu > ul > li:nth-child(6) > a').click()

        driver.quit()

    def demo_XoaDiaChi(self):
        driver = webdriver.Chrome(executable_path="venv/chromedriver.exe")
        driver.maximize_window()
        driver.get("https://thegioiskinfood.com/")

        with open("QLTKDangKi/AccountListLogin.csv", newline="") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        Email = row["Email"]
                        Password = row["Password"]

        # Đóng quảng cáo
        driver.implicitly_wait(13)
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

        # Thoát account
        driver.find_element(B.CSS_SELECTOR,
                            '#account-page > div > div > div.account-page-sidebar > '
                            'div.account-sidebar-menu > ul > li:nth-child(6) > a').click()

        driver.quit()


qlDiaChi = QuanLyDiaChi()
qlDiaChi.demo_ThemDiaChiMoi()
qlDiaChi.demo_SuaDiaChi()
qlDiaChi.demo_XoaDiaChi()
