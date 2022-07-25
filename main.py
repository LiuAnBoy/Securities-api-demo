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

    formData = {
        "licstatus": "active",
        "searchbyoption": "byname",
        "entityType": f"{type}",
        "searchtext": f"{user}",
    }

    # 需求params加上現在秒數
    base_url = "https://apps.sfc.hk/publicregWeb/searchByNameJson"
    today_ms = str(round(time.time() * 1000))

    payload = {
        "licstatus": formData['licstatus'],
        "searchbyoption": formData['searchbyoption'],
        "entityType": formData['entityType'],
        "searchtext": formData["searchtext"],
        "searchlang": "tc",
    }

    res = requests.post(base_url, params={"_dc": today_ms}, data=payload)
    user_number = json.loads(res.text)['items'][0]['ceref'] # 取回中央編號

    data_func = get_data.User(user_number)

    details = data_func.get_details() # 取回牌照詳情
    address = data_func.get_address() # 取回營業地址
    conditions = data_func.get_conditions() # 取回條件
    disciplinaryAction = data_func.get_disciplinaryAction() # 取回公開紀律紀錄
    licenceRecord = data_func.get_licenceRecord() # 取回牌照紀錄
    
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
