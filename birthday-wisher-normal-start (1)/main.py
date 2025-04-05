import datetime as dt
import pandas as pd
import random
import smtplib
MY_EMAIL="madhavkrishnapython@gmail.com"
MY_PASSWORD="***your_app_password"

today_month = dt.datetime.now().month
today_day = dt.datetime.now().day

today = (today_month, today_day)

data = pd.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}

if today in birthday_dict:
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
        birthday_person = birthday_dict[today]
        components = file.read()
        components = components.replace("[NAME]", birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs="madhavkrishnapython@yahoo.com",msg=f"Subject:Happy Birthday\n\n{components}")








