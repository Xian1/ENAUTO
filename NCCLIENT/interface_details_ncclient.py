from ncclient import manager
import xmltodict

#Connection details
cisco = {
    "host": "192.168.253.233",
    "username": "crogne",
    "password": "Bowling300",
    "port": 830
}

with manager.connect(host=cisco["host"],port=cisco["port"],username=cisco["username"],password=cisco["password"],hostkey_verify =False) as m:

#Get configuration and State Info for INterface

    netconf_reply = m.get(filter=("xpath", "/interface-state/interface[name='GigabitEthernet1']"))
    #intf_details = xmltodict.parse (netconf_)
    intf_info = netconf_reply["rpc-reply"]["data"]["interface-state"]["interface"]
    print (intf_info)

