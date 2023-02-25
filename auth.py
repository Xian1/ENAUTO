import requests
import json

api = "j_security_check"
base_url = "https://sandbox-sdwan-2.cisco.com/"
url = base_url + api
payload = {
    "j_username": "devnetuser",
    "j_password": "RG!_Yw919_83"
    }

response = requests.post(url=url, data=payload, verify=False)

cookies = response.headers["Set-Cookie"]
jsessionid = cookies.split(";")


headers = {'Cookie': jsessionid[0]}
api = "dataservice/client/token"
url = base_url + api      
response = requests.get(url=url, headers=headers, verify=False)
token = response.text

header = {'Content-Type': "application/json",'Cookie': jsessionid[0], 'X-XSRF-TOKEN': token}

api = "dataservice/device"
url = base_url + api      

response = requests.get(url=url, headers=headers, verify=False).json()
print (json.dumps(response, indent = 2))