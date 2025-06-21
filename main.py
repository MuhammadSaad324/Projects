import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 31.4273 # Your latitude
MY_LONG = 73.1166 # Your longitude
MY_USER = "saadhasssan47@gmail.com"
MY_PASSWORD = "mdmw hqvb iafm egbe"
RECEIVERS_EMAIL = "saadhasssan47@gmail.com"

def is_iss_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT-5 <=iss_latitude <=MY_LAT+5 and MY_LONG-5 <= iss_latitude <= MY_LONG+5:
        return True

def is_night_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[1])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[1])
    time_now = datetime.now()
    current_hour = time_now.hour
    if current_hour < sunrise or current_hour >= sunset:
        return True

while True:
    time.sleep(60)
    if is_iss_above() and is_night_time():
        with smtplib.SMTP("smtp.gmail.com") as server:
            server.starttls()
            server.login(user=MY_USER, password=MY_PASSWORD)
            server.sendmail(from_addr=MY_USER, to_addrs="mrusman4578@gmail.com",msg="Subject:ISS IS HERE\n\nHey Look Up ISS is Here.")


