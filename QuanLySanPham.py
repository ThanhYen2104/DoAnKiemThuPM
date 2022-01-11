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

        # tímsanpham
        time.sleep(2)
        driver.find_element(B.CSS_SELECTOR, '#f-header > section.f-header-top > '
                                            'div > div > div.f-header-top-search > '
                                            'form > div > input').send_keys("sữa rửa mặt")
        driver.find_element(B.CSS_SELECTOR,
                            '#f-header > section.f-header-top > div > div > div.f-header-top-search > '
                            'form > div > button').click()

        # xemthongtinmotsanpham
        time.sleep(3)
        driver.find_element(B.LINK_TEXT, value='Sữa Rửa Mặt Dịu Nhẹ Freeplus Mild Soap A 100g').click()
        tensanpham = driver.find_element(B.CSS_SELECTOR, '#page-product > section.page-product-info > '
                                                         'div > div > div.page-product-info-right > '
                                                         'div.page-product-info-top > h1').text

        giagiam = driver.find_element(B.CSS_SELECTOR,
                                      '#page-product > section.page-product-info > div > div > div.page-product-info-right > '
                                      'div.page-product-info-price > div.page-product-info-pricewrap >'
                                      'div.page-product-info-newprice > span').text

        chitietsanpham = driver.find_element(B.CSS_SELECTOR,
                                             '#page-product > div:nth-child(3) > div > div.page-product-content-detail-wrap >'
                                             ' div.page-product-content-detail > div.page-product-description > '
                                             'div > div.product-section-title').text
        time.sleep(3)

        driver.find_element(B.CSS_SELECTOR, '#page-product > div:nth-child(3) > div > '
                                            'div.page-product-content-detail-wrap > div.page-product-content-detail > '
                                            'div.page-product-description > div > div.page-product-description-detail-wrap > '
                                            'div.page-product-description-detail-viewmore > button > span:nth-child(1)').click()

        mota = driver.find_element(B.CSS_SELECTOR,
                                   '#page-product > div:nth-child(3) > div > div.page-product-content-detail-wrap > '
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

        # xemthongtinsanpham
        time.sleep(2)
        driver.find_element(B.CSS_SELECTOR, '#f-header > section.f-header-top > '
                                            'div > div > div.f-header-top-search > '
                                            'form > div > input').send_keys("sữa rửa mặt")
        driver.find_element(B.CSS_SELECTOR,
                            '#f-header > section.f-header-top > div > div > div.f-header-top-search > '
                            'form > div > button').click()
        thongtinsanpham = driver.find_elements(B.CLASS_NAME, 'proLoop-wrap')
        time.sleep(5)
        for item in thongtinsanpham:
            try:
                nhanhang = item.find_element(B.CSS_SELECTOR, 'div.proLoop-wrap-info > div.loopvendor > a ').text
                tieude = item.find_element(B.CSS_SELECTOR, 'div.proLoop-wrap-info > p > a').text
                giagoc = item.find_element(B.CSS_SELECTOR,
                                           'div.proLoop-wrap-info > div.productPrice-wrap > p > del').text
                giagiam = item.find_element(B.CSS_SELECTOR,
                                            'div.proLoop-wrap-info > div.productPrice-wrap > p > b').text
                print('****')
                print(tieude)
                print(giagiam)
                print(giagoc)
            except NoSuchElementException:
                print('Loi roi!')

        driver.quit()

    def demo_DatCauHoi(self):
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

        # Xem sản phẩm
        driver.find_element(B.LINK_TEXT, value="BÁN CHẠY").click()
        driver.find_element(
            B.LINK_TEXT,
            value="[Sample 2ml] Mặt Nạ Sủi Bọt Thải Độc Da Sum37 Bright Award Bubble-De Mask",
        ).click()
        driver.implicitly_wait(2)
        driver.find_element(B.CLASS_NAME, 'starbap-ask-question-btn').click()
        # Number
        driver.find_element(B.CSS_SELECTOR, "#startbap_product_reviews > div > div.starbap-rev-widg__header >"
                                            " div.starbap-question-form-wrapper > form > div.starbap-form__phone-fieldset > "
                                            "input[type=phone]").send_keys("0902759295")
        driver.implicitly_wait(2)
        # Đặt câu hỏi
        driver.find_element(B.CSS_SELECTOR, "#startbap_product_reviews > div > div.starbap-rev-widg__header >"
                                            " div.starbap-question-form-wrapper > form > "
                                            "div.starbap-form__question-fieldset > textarea").send_keys(
            "Sản phẩm này có chính hãng không ạ?")
        driver.find_element(B.CSS_SELECTOR, '#startbap_product_reviews > div > div.starbap-rev-widg__header > '
                                            'div.starbap-question-form-wrapper > form >'
                                            ' div.starbap-form__question-fieldset > input').click()
        time.sleep(5)
        driver.quit()

    def demo_VietDanhGia(self):
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

        # Choose_prodution
        driver.find_element(B.CSS_SELECTOR, '#f-menu > div > div > div.f-menu-list > ul > li:nth-child(3) > a').click()
        driver.implicitly_wait(1)
        driver.find_element(B.LINK_TEXT,
                            value='[Mini 30g] Mặt Nạ Có Hạt Tẩy Tế Bào Chết, Dưỡng Da Mịn Màng Chiết Xuất Xương Rồng Huxley Scrub Mask Sweet Therapy').click()

        driver.find_element(B.LINK_TEXT, value='Viết đánh giá').click()

        # Number
        driver.find_element(B.NAME, "reviewer_phone").send_keys("0965462562")

        # Vote
        driver.find_element(B.XPATH, '//*[@title="Excellent"]').click()

        # Comment
        driver.find_element(B.NAME, "review_title").send_keys("comment")
        driver.find_element(B.NAME, "review_body").send_keys("Sản phẩm tốt, đúng như quảng cáo!")

        driver.find_element(B.LINK_TEXT, value='Gửi đánh giá').click()

        driver.quit()

    def demo_XemDanhGia1SP(self):
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

        # Tìm sản phẩm
        driver.find_element(B.LINK_TEXT, value='BÁN CHẠY').click()
        # sanpham1
        driver.implicitly_wait(5)
        driver.find_element(B.LINK_TEXT,
                            value='[Sample 2ml] Mặt Nạ Sủi Bọt Thải Độc Da Sum37 Bright Award Bubble-De Mask').click()
        tensanpham1 = driver.find_element(B.TAG_NAME, 'h1').text
        print(tensanpham1)
        danhgia = driver.find_elements(B.CSS_SELECTOR, 'div.starbap-rev')
        for item in danhgia:
            try:
                name = item.find_element(B.CSS_SELECTOR, 'SPAN.starbap-rev__author').text
                rate = item.find_element(B.TAG_NAME, 'b').text
                rate2 = item.find_element(B.CSS_SELECTOR, 'div.starbap-rev__body > p').text
                print(name)
                print(rate)
                print(rate2)
                print('-------------------')
            except NoSuchElementException:
                print("Loi")
        # sanpham2
        driver.implicitly_wait(5)
        driver.find_element(B.LINK_TEXT, value='BÁN CHẠY').click()
        driver.find_element(B.LINK_TEXT,
                            value='[30ml] Tinh Chất Tăng Cường Sáng Da Mờ Thâm Garnier Light Complete Vitamin C 30X Booster Serum').click()
        tensanpham2 = driver.find_element(B.TAG_NAME, 'h1').text
        print(tensanpham2)
        danhgia2 = driver.find_elements(B.CSS_SELECTOR, 'div.starbap-rev')
        for item in danhgia2:
            try:
                name1 = item.find_element(B.CSS_SELECTOR, 'SPAN.starbap-rev__author').text
                rate3 = item.find_element(B.TAG_NAME, 'b').text
                rate4 = item.find_element(B.CSS_SELECTOR, 'div.starbap-rev__body > p').text
                print(name1)
                print(rate3)
                print(rate4)
                print('-------------------')
            except NoSuchElementException:
                print("Loi")
        # Thoát account
        driver.implicitly_wait(5)
        driver.find_element(B.CLASS_NAME, 'f-header-top-icon-account').click()
        driver.find_element(B.CSS_SELECTOR,
                            '#account-page > div > div > div.account-page-sidebar > '
                            'div.account-sidebar-menu > ul > li:nth-child(6) > a').click()
        time.sleep(5)
        driver.quit()


qlDiaChi = QuanLySanPham()
qlDiaChi.demo_XemThongTin1SP()
# qlDiaChi.demo_XemThongTinNhieuSP()
# qlDiaChi.demo_DatCauHoi()
# qlDiaChi.demo_VietDanhGia()
# qlDiaChi.demo_XemDanhGia1SP()
