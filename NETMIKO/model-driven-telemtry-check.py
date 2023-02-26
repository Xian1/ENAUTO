from netmiko import ConnectHandler

R1 = {  "device_type":"cisco_ios",
        "ip":"192.168.253.232",
        "username":"crogne",
        "password":"Bowling300"
    }

net_connect = ConnectHandler (**R1)

output = net_connect.send_command("sh run | sec tel")

net_connect.disconnect()

print(output)
