import smtplib
import datetime as dt
from random import randint
my_email = "joyben0987@gmail.com"
password = "mkxqzmkouxopmblq"


now = dt.datetime.now()
week = 0

with open("quotes.txt") as quote:
    my_quote = quote.readlines()
    today_quote = my_quote[randint(0,len(my_quote)-1)]

if week == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="joywinbennis0987@gmail.com",
                            msg=f"subject:Today Quote\n\n{today_quote}"
                            )
else:
    print("its not monday")
#
#
# with open("quotes.txt") as quote:
#
#
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="vyasamnayak@gmail.com",
#                         msg="HELLO\n\nThis is a email sent using python smtp library."
#                         )