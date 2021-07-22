from bs4 import BeautifulSoup
import requests
import json


class User:
    def __init__(self, user_number):
        self.user_number = user_number

    def get_details(self):
        details_url = f"https://apps.sfc.hk/publicregWeb/indi/{self.user_number}/details"
        res = requests.get(details_url)
        soup = BeautifulSoup(res.text, "lxml")
        script = soup.find_all("script")[3]
        str_script = str(script)
        if 'var indData = ' in str_script:
            jsonStr = str_script.strip()
            jsonStr = jsonStr.split('var indData = ')[1].strip()
            jsonStr = jsonStr.split(';')[0].strip()
            if (jsonStr == ''):
                return ''
            else:
                r_dict = json.loads(jsonStr)
        return r_dict

    def get_address(self):
        details_url = f"https://apps.sfc.hk/publicregWeb/indi/{self.user_number}/addresses"
        res = requests.get(details_url)
        soup = BeautifulSoup(res.text, "lxml")
        script = soup.find_all("script")[3]
        str_script = str(script)
        if 'var indData = ' in str_script:
            jsonStr = str_script.strip()
            jsonStr = jsonStr.split('var indData = ')[1].strip()
            jsonStr = jsonStr.split(';')[0].strip()
            if (jsonStr == ''):
                return ''
            else:
                r_dict = json.loads(jsonStr)
        return r_dict

    def get_conditions(self):
        details_url = f"https://apps.sfc.hk/publicregWeb/indi/{self.user_number}/conditions"
        res = requests.get(details_url)
        soup = BeautifulSoup(res.text, "lxml")
        script = soup.find_all("script")[3]
        str_script = str(script)
        if 'var indData = ' in str_script:
            jsonStr = str_script.strip()
            jsonStr = jsonStr.split('var indData = ')[1].strip()
            jsonStr = jsonStr.split(';')[0].strip()
            if (jsonStr == ''):
                return ''
            else:
                r_dict = json.loads(jsonStr)
        return r_dict

    def get_disciplinaryAction(self):
        details_url = f"https://apps.sfc.hk/publicregWeb/indi/{self.user_number}/disciplinaryAction"
        res = requests.get(details_url)
        soup = BeautifulSoup(res.text, "lxml")
        script = soup.find_all("script")[4]
        str_script = str(script)
        if 'var disRemarkData = ' in str_script:
            jsonStr = str_script.strip()
            jsonStr = jsonStr.split('var disRemarkData = ')[1].strip()
            jsonStr = jsonStr.split(';')[0].strip()
            if (jsonStr == ''):
                return ''
            else:
                r_dict = json.loads(jsonStr)
        return r_dict

    def get_licenceRecord(self):
        details_url = f"https://apps.sfc.hk/publicregWeb/indi/{self.user_number}/licenceRecord"
        res = requests.get(details_url)
        soup = BeautifulSoup(res.text, "lxml")
        script = soup.find_all("script")[4]
        str_script = str(script)
        if 'var licRecordData = ' in str_script:
            jsonStr = str_script.strip()
            jsonStr = jsonStr.split('var licRecordData = ')[1].strip()
            jsonStr = jsonStr.split(';')[0].strip()
            if (jsonStr == ''):
                return ''
            else:
                r_dict = json.loads(jsonStr)
        return r_dict