# import requests
# from datetime import datetime
#
# GENDER = "male"
# WEIGHT_KG = "57"
# HEIGHT_CM = "176"
# AGE = "19"
#
# API_KEY = "0c44f1bb2e89ddc60409c4dd6dc33880"
# APP_ID = "7cbe3133"
#
# exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
# sheet_endpoint = "https://api.sheety.co/f8124bfad201c0625b7ce04ebaa80c7b/myWorkout/workouts"
#
# exercise_text = input("Tell me which exercises you did: ")
#
# headers = {
#     "x-app-id": APP_ID,
#     "x-app-key": API_KEY,
# }
#
# parameters = {
#     "query": exercise_text,
#     "gender": GENDER,
#     "weight_kg": WEIGHT_KG,
#     "height_cm": HEIGHT_CM,
#     "age": AGE
# }
#
# response = requests.post(exercise_endpoint, json=parameters, headers=headers)
# result = response.json()
#
# ################### Start of Step 4 Solution ######################
#
# today_date = datetime.now().strftime("%d/%m/%Y")
# now_time = datetime.now().strftime("%X")
# for exercise in result["exercises"]:
#     sheet_inputs = {
#         "workout": {
#             "date": today_date,
#             "time": now_time,
#             "exercise": exercise["name"].title(),
#             "duration": exercise["duration_min"],
#             "calories": exercise["nf_calories"]
#         }
#     }
#     print(sheet_inputs)
#     sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
#
#     print(sheet_response.text)
#
# #{'workout': {'Date': '09:56:20', 'Time': 10, 'Exercise': 'General Workout', 'Duration': 10, 'Calories': 38}}
API_TEST ="EWIFJCJNONEWKNVCOJ"
import os
a = os.