from netmiko import ConnectHandler
import json

sw1 = {
    "device_type": "cisco_ios",
    "host": "192.168.253.231",
    "username": "crogne",
    "password": "Bowling300"
}

csr1000 = {
    "device_type": "cisco_ios",
    "host": "192.168.253.233",
    "username": "crogne",
    "password": "Bowling300"
}

all_switches = [sw1, csr1000]

for switches in all_switches:
    net_connect = ConnectHandler(**switches)
    output = net_connect.send_command("sh ip int bri")
    print ("**********")
    print (output)



##config_commands = ["interface loopback11", "ip address 10.29.22.1 255.255.255.255"]
#output = net_connect.send_config_set(config_commands)
#print (output)

#for vlan in range (40,50):
#    print ("create from vlan 40 to 50")
#    config_commands = ["vlan " + str(vlan), "name Myvlan" + str(vlan)]
#    output = net_connect.send_config_set(config_commands)
#    print (output)

