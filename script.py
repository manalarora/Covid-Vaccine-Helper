import time
import datetime
import json
import requests


today = datetime.datetime.today()
DATE = f"{today.day}-{today.month}-{today.year}"
DISTRICT_IDS = [149,144]
PINCODES = [201301]
headers = {
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

def processData(data):
    for center in data["centers"]:
        for session in center["sessions"]:
            if session["min_age_limit"] == 18 and session["available_capacity"]>0:
                if session["vaccine"] == "COVAXIN":
                    print("-----------------------------")
                    print("PAY ATTENTION WE GOT COVAXIN")
                    print("-----------------------------")
                print("NAME OF CENTRE ", center["name"])
                print("DATE ", session["date"])
                print("AVAILABLE CAPACITY", session["available_capacity"])
                print("VACCINE ", session["vaccine"])
                print("STATE ", center["state_name"])
                print("DISTRICT NAME ", center["district_name"])
                print("\n")
                


def main():    
    while(True):
        print("Current Time Request ", datetime.datetime.today())
        # check in all the specified pincodes
        for pincode in PINCODES:
            url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={DATE}"
            response = requests.get(url, headers = headers)
            json_data = json.loads(response.text)
            processData(json_data)
        # check in all the specified districts
        for district_id in DISTRICT_IDS:
            url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={district_id}&date={DATE}"
            response = requests.get(url, headers = headers)
            json_data = json.loads(response.text)
            processData(json_data)
        # sleep for specified seconds
        time.sleep(30)

main()
