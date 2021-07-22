from re import search
from flask import Flask, request
from bs4 import BeautifulSoup
import requests
import os
import time
import json
import get_data

app = Flask(__name__)


@app.route('/api/userdata', methods=['GET'])
def index():
    user = request.args.get('user')
    type = request.args.get('type')
    lang = request.args.get('lang')

    formData = {
        "licstatus": "active",
        "searchbyoption": "byname",
        "searchlang": f"{lang}",
        "entityType": f"{type}",
        "searchtext": f"{user}",
        # "page": "1",
        # "start": "0",
        # "limit": "20"
    }

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

    x = get_data.User(user_number)

    details = x.get_details()
    address = x.get_address()
    conditions = x.get_conditions()
    disciplinaryAction = x.get_disciplinaryAction()
    licenceRecord = x.get_licenceRecord()
    data = {
        "data": {
            "details": details,
            "address": address,
            "conditions": conditions,
            "disciplinaryAction": disciplinaryAction,
            "licenceRecord": licenceRecord
        }
    }

    return data


if __name__ == '__main__':
    app.run(debug=True)
