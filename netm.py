from netmiko import ConnectHandler
import json

cisco = {
    "device_type": "cisco_ios",
    "host": "192.168.253.233",
    "username": "crogne",
    "password": "Bowling300"
}

net_connect = ConnectHandler(**cisco) as m:


output = net_connect.send_command("sh ip int bri")
print (output)