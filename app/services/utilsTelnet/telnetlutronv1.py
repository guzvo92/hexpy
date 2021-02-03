#import getpass
import telnetlib
from telnetlib import Telnet

HOST = "192.168.15.12" #"localhost"
tn = telnetlib.Telnet(HOST)

'''
#conexion1
userman = input ("Enter your account :")
passwman = getpass.getpass()

tn.read_until(b"login: ")
tn.write(userman.encode('ascii') + b"\n")
if passwman:
	tn.read_until(b"Password: ")
	tn.write(passwman.encode('ascii')+ b"\n")


'''
#conexion2
userauto = "Auvit"
passauto = "1234"


try:
	response = tn.read_until(b"login: ", timeout=10)
except EOFError as e:
	print ("Connection closed")

if b"login: " in response:
	print("[0.1]-> si encontro login")
	w1= userauto.encode("ascii")+b'\r\n'
	tn.write(w1)
	print("[1]--->"+str(w1))
else:
	print("1er ARG Esta perdido")

try:
	response2 = tn.read_until(b"password: ", timeout=10)
except EOFError as e:
	print ("Connection closed")

if b'password: ' in response2:
	print("[0.1]-> si encontro password")
	w2=passauto.encode("ascii")+b'\r\n'
	tn.write(w2)
	print("[2]--->"+str(w2))
else:
	print("2o ARG Esta perdido")


#//tn.write(b"#OUTPUT,288,1,0"+b"<CR>"+b"<LF>")
m1 = "#OUTPUT,10,1,0.00".encode("ascii")+b'\r\n'
print("[3]--->"+str(m1))
tn.write(m1)

#print(tn.read_all().decode('ascii'))

#tn.write(b"ls\n")
tn.write(b"exit\n") #forzozo
