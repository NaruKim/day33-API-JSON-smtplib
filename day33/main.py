import requests
from datetime import datetime

MY_LAT = 37.566536
MY_LNG = 126.977966

# response = requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# # if response.status_code == 404:
# #     raise Exception("That resource does not exist")
# # elif response.status_code == 401:
# #     raise Exception("You are not authorised to access")
#
# data = response.json()
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
# timestamp = data['timestamp']
# message = data['message']
#
# iss_position = (latitude,longitude)
# print(iss_position)

parameters = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)