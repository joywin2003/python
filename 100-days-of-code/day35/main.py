api_key ="d8da4f52f93381a763c648fde97abb6f"
api_link ="https://api.openweathermap.org/data/2.8/onecall"
MY_EMAIL = "joyben0987@gmail.com"
PASSWORD = "mkxqzmkouxopmblq"
import requests
import smtplib
parameter = {
    "lat":12.904110,
    "lon": 75.041367,
    "exclude":"current,minutely,daily,alerts",
    "appid": api_key
}

response = requests.get(api_link,params=parameter)
response.raise_for_status()
data =response.json()

is_raining = False

for i in range(0,11):
    id = data["hourly"][i]["weather"][0]["id"]
    if id>700:
        print("take your umbrella")
        is_raining=True
        break



if is_raining:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="joywinbennis0987@gmail.com",
                            msg=f"subject:REMINDER\n\nMake sure you bring a umbrella"
                            )


