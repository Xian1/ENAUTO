import requests
import json

iface = "Loopback3"

server= {
    "host": "192.168.253.233",
    "port": 443,
    "user": "crogne", 
    "password": "Bowling300"
}

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
    }

data = {
    "ietf-interfaces:interface": {
    "name": iface,
    "description": "Added with requests library",
    "type": "iana-if-type:softwareLoopback",
    "enabled": True,
    "ietf-ip:ipv4": {
        "address": [
                {
                    "ip": "172.16.2.1",
                    "netmask": "255.255.255.0"
                }
            ]
        }
    }
}  

#Creating loopback 
#url = f"https://{server['host']}:{server['port']}/restconf/data/ietf-interfaces:interfaces/"
#response = requests.put(url=url, headers=headers, auth=(server['user'], server['password']), data=json.dumps(data), verify=False)

#Update loopback
url = f"https://{server['host']}:{server['port']}/restconf/data/ietf-interfaces:interfaces/interface=" + iface
#response = requests.put(url=url, headers=headers, auth=(server['user'], server['password']), data=json.dumps(data), verify=False)

#delete loopback
url = f"https://{server['host']}:{server['port']}/restconf/data/ietf-interfaces:interfaces/interface=" + iface
response = requests.delete(url=url, headers=headers, auth=(server['user'], server['password']), verify=False)

print (response.status_code)
if response.status_code == 204:
    if iface:

        #Read the new loopback
        url = f"https://{server['host']}:{server['port']}/restconf/data/ietf-interfaces:interfaces/interface=" + iface
        response = requests.get(url=url, headers=headers, auth=(server['user'], server['password']), verify=False).json()

        #print the result of 

        intname = (response['ietf-interfaces:interface']['name'])
        ip =  (response['ietf-interfaces:interface']['ietf-ip:ipv4']['address'][0]['ip'])
        netmask = (response['ietf-interfaces:interface']['ietf-ip:ipv4']['address'][0]['netmask'])
        print (intname + " has been created and its IP " + ip + " and netmask " + netmask)
    else:
        print(iface + " is deleted !!")

if response.status_code == 201:
    url = f"https://{server['host']}:{server['port']}/restconf/data/ietf-interfaces:interfaces/interface=" + iface
    response = requests.get(url=url, headers=headers, auth=(server['user'], server['password']), verify=False).json()

    #print the result of 

    intname = (response['ietf-interfaces:interface']['name'])
    ip =  (response['ietf-interfaces:interface']['ietf-ip:ipv4']['address'][0]['ip'])
    netmask = (response['ietf-interfaces:interface']['ietf-ip:ipv4']['address'][0]['netmask'])
    print (intname + " has been created and its IP " + ip + " and netmask " + netmask)
else:
    print("Failed")

