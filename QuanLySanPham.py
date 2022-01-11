import csv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By as B
import time

class QuanLySanPham():
    def demo_XemThongTin1SP(self):
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
        driver.find_element(B.CSS_SELECTOR, '#customer_login > div:nth-child(3) > input').send_keys(Email)
        time.sleep(3)
        driver.find_element(B.CSS_SELECTOR, '#customer_login > div:nth-child(4) > input').send_keys(Password)
        time.sleep(3)
        driver.find_element(B.CSS_SELECTOR, '#customer_login > div:nth-child(6) > button.btn.btn-primary').click()

        #tímsanpham
        time.sleep(2)
        driver.find_element(B.CSS_SELECTOR,'#f-header > section.f-header-top > '
                                           'div > div > div.f-header-top-search > '
                                           'form > div > input').send_keys("sữa rửa mặt")
        driver.find_element(B.CSS_SELECTOR,
                            '#f-header > section.f-header-top > div > div > div.f-header-top-search > '
                            'form > div > button').click()

        #xemthongtinmotsanpham
        time.sleep(3)
        driver.find_element(B.LINK_TEXT,value='Sữa Rửa Mặt Dịu Nhẹ Freeplus Mild Soap A 100g').click()
        tensanpham = driver.find_element(B.CSS_SELECTOR,'#page-product > section.page-product-info > '
                                                        'div > div > div.page-product-info-right > '
                                                        'div.page-product-info-top > h1').text

        giagiam = driver.find_element(B.CSS_SELECTOR,'#page-product > section.page-product-info > div > div > div.page-product-info-right > '
                                           'div.page-product-info-price > div.page-product-info-pricewrap >'
                                           'div.page-product-info-newprice > span').text

        chitietsanpham = driver.find_element(B.CSS_SELECTOR,'#page-product > div:nth-child(3) > div > div.page-product-content-detail-wrap >'
                                           ' div.page-product-content-detail > div.page-product-description > '
                                           'div > div.product-section-title').text
        time.sleep(3)

        driver.find_element(B.CSS_SELECTOR,'#page-product > div:nth-child(3) > div > '
                                           'div.page-product-content-detail-wrap > div.page-product-content-detail > '
                                           'div.page-product-description > div > div.page-product-description-detail-wrap > '
                                           'div.page-product-description-detail-viewmore > button > span:nth-child(1)').click()

        mota = driver.find_element(B.CSS_SELECTOR,'#page-product > div:nth-child(3) > div > div.page-product-content-detail-wrap > '
                                           'div.page-product-content-detail > div.page-product-description > div > '
                                           'div.page-product-description-detail-wrap.expanded > '
                                           'div.page-product-description-detail').text
        print(tensanpham)
        print(giagiam)
        print(chitietsanpham)
        print(mota)

        driver.close()

    def demo_XemThongTinNhieuSP(self):
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
        driver.find_element(B.CSS_SELECTOR, '#customer_login > div:nth-child(3) > input').send_keys(Email)
        time.sleep(3)
        driver.find_element(B.CSS_SELECTOR, '#customer_login > div:nth-child(4) > input').send_keys(Password)
        time.sleep(3)
        driver.find_element(B.CSS_SELECTOR, '#customer_login > div:nth-child(6) > button.btn.btn-primary').click()

        #xemthongtinsanpham
        time.sleep(2)
        driver.find_element(B.CSS_SELECTOR,'#f-header > section.f-header-top > '
                                           'div > div > div.f-header-top-search > '
                                           'form > div > input').send_keys("sữa rửa mặt")
        driver.find_element(B.CSS_SELECTOR,
                            '#f-header > section.f-header-top > div > div > div.f-header-top-search > '
                            'form > div > button').click()
        thongtinsanpham = driver.find_elements(B.CLASS_NAME,'proLoop-wrap')
        time.sleep(5)
        for item in thongtinsanpham:
            try:
                 nhanhang = item.find_element(B.CSS_SELECTOR,'div.proLoop-wrap-info > div.loopvendor > a ').text
                 tieude = item.find_element(B.CSS_SELECTOR,'div.proLoop-wrap-info > p > a').text
                 giagoc= item.find_element(B.CSS_SELECTOR,'div.proLoop-wrap-info > div.productPrice-wrap > p > del').text
                 giagiam = item.find_element(B.CSS_SELECTOR,'div.proLoop-wrap-info > div.productPrice-wrap > p > b').text
                 print('****')
                 print(tieude)
                 print(giagiam)
                 print(giagoc)
            except NoSuchElementException:
                print('Loi roi!')

        driver.quit()


qlDiaChi = QuanLySanPham()
qlDiaChi.demo_XemThongTin1SP()
# qlDiaChi.demo_XemThongTinNhieuSP()
