import csv

with open("AccountList.csv", "w", newline="") as f:
    fieldName = ["LastName", "FirstName", "Email", "CreatePassword", "PhoneNumber"]
    writer = csv.DictWriter(f, fieldnames=fieldName)
    writer.writeheader()
    writer.writerow(
        {
            "LastName": "Le",
            "FirstName": "Ji",
            "Email": "mailtest7@gmail.com",
            "CreatePassword": "123456789yen",
            "PhoneNumber": "0274548392",
        }
    )

with open("AccountList.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        L = row["LastName"]
        F = row["FirstName"]
        E = row["Email"]
        P = row["CreatePassword"]
        PN = row["PhoneNumber"]

print(L)
print(F)
print(E)
print(P)
print(PN)
