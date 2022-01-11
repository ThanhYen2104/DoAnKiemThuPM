import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class QuanLySanPham():
    def demo_DanhGiaSanPham(self):
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
        driver.find_element(By.CLASS_NAME,'windownpopup_close').click()

        # Đóng MessagesBox
        time.sleep(2)
        iframeMes = driver.find_element(By.XPATH, '//*[@id="fb-root"]/div[2]/span/iframe')
        driver.switch_to.frame(iframeMes)
        time.sleep(4)
        driver.find_element(
            By.XPATH,
            "/html/body/div/div/div/div/div/div/div/div/div/div[1]/div[3]/div[2]/div/div",
        ).click()
        driver.switch_to.default_content()

        # Login
        driver.find_element(By.CLASS_NAME, 'f-header-top-icon-account').click()
        # driver.find_element(By.NAME, "customer[email]").send_keys("phuong211zz@gmail.com")
        # driver.find_element(By.NAME, "customer[password]").send_keys("A2345768")
        driver.find_element(By.NAME, "customer[email]").send_keys(Email)
        driver.find_element(By.NAME, "customer[password]").send_keys(Password)
        driver.find_element(By.CSS_SELECTOR, '#customer_login > div:nth-child(6) > button.btn.btn-primary').click()

        # Choose_prodution
        driver.find_element(By.CSS_SELECTOR, '#f-menu > div > div > div.f-menu-list > ul > li:nth-child(3) > a').click()
        driver.implicitly_wait(1)
        driver.find_element(By.LINK_TEXT, value='[Mini 30g] Mặt Nạ Có Hạt Tẩy Tế Bào Chết, Dưỡng Da Mịn Màng Chiết Xuất Xương Rồng Huxley Scrub Mask Sweet Therapy').click()
        time.sleep(4)
        driver.find_element(By.CSS_SELECTOR, "a.starbap-write-rev-link").click()

        # Number
        driver.find_element(By.NAME, "reviewer_phone").send_keys("0965462562")

        # Vote
        driver.find_element(By.XPATH, '//*[@title="Excellent"]').click()

        # Comment
        driver.find_element(By.NAME, "review_title").send_keys("comment")
        driver.find_element(By.NAME, "review_body").send_keys("Sản phẩm tốt, đúng như quảng cáo!")

        # driver.find_element(By.LINK_TEXT, value='Gửi đánh giá').click()

        driver.quit()


qlDiaChi = QuanLySanPham()
qlDiaChi.demo_DanhGiaSanPham()
