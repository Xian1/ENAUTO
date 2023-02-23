import json
import requests


base_url ="https://131.226.217.159"
auth_endpoint = "j_security_check"

login_body={
    "j_username": "devnetuser",
    "J_password": "RG!_Yw919_83"
}

sesh = requests.session()
login_response = sesh.post(url=f"{base_url}{auth_endpoint}", data=login_body, verify=False)
print (login_response.status_code)

device_endpoint = "dataservice/system/device/vedges"


device_response = sesh.get(url=f"{base_url}{device_endpoint}", verify=False).json()
print (device_response.text)
