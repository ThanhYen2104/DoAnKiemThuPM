import csv

class QuanLyInput_Output():
    def demo_Input_Output_DangKy(self):
        with open("AccountListSignUp.csv", "w", newline="") as f:
            fieldName = ["LastName", "FirstName", "Email", "CreatePassword", "PhoneNumber"]
            writer = csv.DictWriter(f, fieldnames=fieldName)
            writer.writeheader()
            writer.writerow(
                {
                    "LastName": "Le",
                    "FirstName": "Ji",
                    "Email": "mailtest9@gmail.com",
                    "CreatePassword": "123456789hihi",
                    "PhoneNumber": "0274548392",
                }
            )

        with open("AccountListSignUp.csv", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                l_Name = row["LastName"]
                f_Name = row["FirstName"]
                email = row["Email"]
                passwordCreate = row["CreatePassword"]
                phoneNumber = row["PhoneNumber"]

        print(l_Name)
        print(f_Name)
        print(email)
        print(passwordCreate)
        print(phoneNumber)

    def demo_Input_Output_DangNhap(self):
        with open("AccountListLogin.csv", "w", newline="") as f:
            fieldName = ["Email", "Password"]
            writer = csv.DictWriter(f, fieldnames=fieldName)
            writer.writeheader()
            writer.writerow(
                {
                    "Email": "mailtest9@gmail.com",
                    "Password": "123456789hihi",
                }
            )

        with open("AccountListLogin.csv", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                email = row["Email"]
                password = row["Password"]
        print(email)
        print(password)


qlDiaChi = QuanLyInput_Output()
qlDiaChi.demo_Input_Output_DangKy()

# qlDiaChi.demo_Input_Output_DangNhap()
