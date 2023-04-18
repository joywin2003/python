import requests
import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()

parameter = {
    "lat": "12.904110",
    "lng": "75.041367",
    "formatted" : 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameter)
response.raise_for_status()
sunrise = response.json()["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = response.json()["results"]["sunset"].split("T")[1].split(":")[0]
print(sunset, sunrise)
now = datetime.datetime.now()
print(now.hour)
