from ncclient import manager

cisco = {
    "host": "192.168.253.233",
    "username": "crogne",
    "password": "Bowling300",
    "port": 830
}

with manager.connect(host=cisco["host"],port=cisco["port"],username=cisco["username"],password=cisco["password"],hostkey_verify =False) as m:
    for capabilitiy in m.server_capabilities:
        print(capabilitiy)