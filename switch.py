import telnetlib
import time

#Defining variables
HOST="192.168.1.1"
username="admin"
password='cisco'

#Telnet into the device
tn=telnetlib.Telnet(HOST)      #creting session with device

time.sleep(3)
tn.read_until(b"Username: ")  # b is used for coverting into bytes
tn.write(username.encode(ascii())+ b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode(ascii())+b"\n")
time.sleep(5)

#write the commands on the device
tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"config t\n")
tn.write(b"vlan 10")
tn.write(b"end\n")
tn.write(b"exit\n")

#To print on the console
print(tn.read_all().decode())
