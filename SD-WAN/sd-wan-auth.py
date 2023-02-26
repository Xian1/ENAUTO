import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#Log in to sandbox to get sessionid
api = "j_security_check"
base_url = "https://10.10.20.90/"
url = base_url + api
payload = {
    "j_username": "admin",
    "j_password": "C1sco12345"
    }

response = requests.post(url=url, data=payload, verify=False)

cookies = response.headers["Set-Cookie"]
jsessionid = cookies.split(";")

#Log in with sessionid to get token

headers = {'Cookie': jsessionid[0]}
api = "dataservice/client/token"
url = base_url + api      
response = requests.get(url=url, headers=headers, verify=False)
token = response.text

headers = {
    'Content-Type': "application/json",
    "Accept": "application/json",
    'Cookie': jsessionid[0], 
    'X-XSRF-TOKEN': token}


admin_endpoint = "dataservice/admin/user"

payload = {
    "group" : ["netadmin"],
    "description": "Christia Rogne",
    "userName": "crogne",
    "password": "Password123"
}

#user_create = requests.post(url=f"{base_url}{admin_endpoint}", headers=headers, data=json.dumps(payload), verify = False)
#print (user_create.text)

pw_endpoint = "dataservice/damin/user/password/crogne"

payload = {
    "userName": "crogne",
    "Password": "Somehingsuperscure123!"
}

user_chpwd = requests.put(url=f"{base_url}{pw_endpoint}", headers=headers, data=json.dumps(payload), verify = False)
#print (user_chpwd.text)

#Log in with token and sessionid to get devices   
#device_endpoint = "dataservice/template/feature/types"
#url = base_url + device_endpoint

#response = requests.get(url=url, headers=headers, verify=False).json()
#print (json.dumps(response, indent = 2))


#monitor_endpoint = "dataservice/device/monitor"
#url = base_url + monitor_endpoint

#monitor_response = requests.get(url=url, headers=headers, verify=False).json()
#vedges = monitor_response["data"]
#print (vedges)

#for vedge in vedges:
#    if vedges[x]["status"] == "normal":
#        print ("Status for " +  vedges[x]["host-name"] + " is " + vedges[x]["status"])

#for vedge in monitor_response:

#    if 

#print (json.dumps(monitor_response, indent = 2))

cert_endpoint = "dataservice/certificate/vsmart/list"

cert_response = requests.get(url=f"{base_url}{cert_endpoint}", headers=headers, verify = False).json()
#print (json.dumps(cert_response, indent = 2))

root_endpoint = "dataservice/certificate/rootcertificate"

root_response = requests.get(url=f"{base_url}{root_endpoint}", headers=headers, verify = False).json()
print (json.dumps(root_response, indent = 2))