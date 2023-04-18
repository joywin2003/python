##################### Extra Hard Starting Project ######################
import smtplib

# 1. Update the birthdays.csv
import pandas as pd
import datetime
import smtplib
import random

my_email = "joyben0987@gmail.com"
password = "mkxqzmkouxopmblq"

df = pd.read_csv("birthdays.csv")
letters = ["letter_1.txt","letter_2.txt","letter_3.txt"]

with open(f"letter_templates/{random.choice(letters)}") as letters:
    letter = letters.read()
    letter = letter.replace("[NAME]",df.loc[0,"name"])



# 2. Check if today matches a birthday in the birthdays.csv
now = datetime.datetime.now()
if now.day == df.loc[0,"day"] and now.month == df.loc[0,"month"]:
    print("happy birthday")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="joywinbennis0987@gmail.com",
                            msg=f"subject:Happy Birthday\n\n{letter}"
                            )









