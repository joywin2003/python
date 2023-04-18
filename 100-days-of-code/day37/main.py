import requests
import datetime

today = datetime.datetime.now().strftime("%Y%m%d")

API_URL = "https://pixe.la/v1/users"
USERNAME = "joywin123"
GRAPH_ENDPOINT = f"{API_URL}/{USERNAME}/graphs"
TOKEN = "ewfwvgrgreg"
PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/graph1"
print(PIXEL_ENDPOINT)
# parameter = {
#     "token":"ewfwvgrgreg",
#     "username":"joywin123",
#     "agreeTermsOfService":"yes",
#     "notMinor":"yes",

graph_config ={
    "id":"graph1",
    "name":"workout",
    "unit": "min",
    "type":"int",
    "color":"shibafu"
}


pixel_config ={
    "date": "20221027",
    "quantity":"9",

}
pixel_out={
    "quantity": "1",
}

HEADERS = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=PIXEL_ENDPOINT,json=pixel_config,headers=HEADERS)
# response = requests.put(url=PIXEL_ENDPOINT,json=pixel_out,headers=HEADERS)
print(response.text)

