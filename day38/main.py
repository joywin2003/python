import requests
from datetime import datetime
import os
# API_KEY = "0c44f1bb2e89ddc60409c4dd6dc33880"
APP_ID = "7cbe3133"
NUTRIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
GSHEET_ENDPOINT = "https://api.sheety.co/f8124bfad201c0625b7ce04ebaa80c7b/myWorkout/workouts"
API_KEY = os.getenv('API_KEY')
HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}
TOKEN = {"Authorization": "Bearer rv23njn23vif345ew234ncjei43"}
workout = input("Tell me which exercises you did: ")



NUTRIX_CONFIG = {
    "query": workout,
    "gender": "male",
    "weight_kg": "57",
    "height_cm": "176",
    "age": 19
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


response = requests.post(url=NUTRIX_ENDPOINT, json=NUTRIX_CONFIG, headers=HEADERS)
result = response.json()

DATA ={
    "workout": {
        "date": today_date,
        "time": now_time,
        "exercise": result['exercises'][0]['name'].title(),
        "duration": result['exercises'][0]['duration_min'],
        "calories": result['exercises'][0]['nf_calories']
}
}
print(DATA)

result = requests.post(url=GSHEET_ENDPOINT, json=DATA,headers=TOKEN)
print(result.text)
