from ncclient import manager
import xmltodict
import json

with manager.connect(host="192.168.253.233",
                    port = 830,
                    username="crogne", 
                    password="Bowling300", 
                    hostkey_verify=False,
                    device_params={"name":"csr"}) as m:
    c = m.get_config(source='running').data_xml
    with open("%s.xml" % "192.168.253.233", 'w') as f:
        f.write(c)

test = (json.loads(c))
print (json.dumps(test), indent = 2)