import getpass
import telnetlib

HOST = "192.168.253.232"
user = input("Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf t\n")
tn.write(b"int lo2\n")
tn.write(b"ip add 10.200.200.1 255.255.255.255\n")
tn.write(b"no shut\n")
tn.write(b"end\n")
tn.write(b"wr\n")

print(tn.read_all().decode('ascii'))