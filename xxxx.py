from bs4 import BeautifulSoup
import requests
import os
import time
import json
import get_data

formData = {
    "licstatus": "active",
    "searchbyoption": "byname",
    "searchlang": "tc",
    "entityType": "individual",
    "searchtext": "陳文徽",
    "page": "1",
    "start": "0",
    "limit": "20"
}


def get_User_Number(formData):
    base_url = "https://apps.sfc.hk/publicregWeb/searchByNameJson"
    today_ms = str(round(time.time() * 1000))

    payload = {
        "licstatus": formData['licstatus'],
        "searchbyoption": formData['searchbyoption'],
        "searchlang": formData['searchlang'],
        "entityType": formData['entityType'],
        "searchtext": formData["searchtext"],
    }

    res = requests.post(base_url, params={"_dc": today_ms}, data=payload)
    soup = BeautifulSoup(res.content, "lxml")
    result = soup.find("p")
    r_dict = json.loads(result.text)
    user_number = r_dict['items'][0]['ceref']

    return str(user_number)


user = get_data.User(get_User_Number(formData))


def get_User_data():
    details = user.get_details()
    address = user.get_address()
    conditions = user.get_conditions()
    disciplinaryAction = user.get_disciplinaryAction()
    licenceRecord = user.get_licenceRecord()
    data = {
        "data": {
            "details": details,
            "address": address,
            "conditions": conditions,
            "disciplinaryAction": [disciplinaryAction],
            "licenceRecord": licenceRecord
        }
    }
    print(data)


get_User_data()