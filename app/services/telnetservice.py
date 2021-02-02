#import getpass
import telnetlib
from telnetlib import Telnet

HOST = "192.168.10.11" #"localhost"
tn = telnetlib.Telnet(HOST)
userauto = "auvit"
passauto = "1234"

#Conexion al username -------------------------------------
try:
	response = tn.read_until(b'login: ', timeout=100)
except EOFError as e:
	print ("Connection closed")

if b"login: " in response:
	print("[0.1]-> si encontro login")
	w1= userauto.encode("ascii") + b'\r\n'
	tn.write(w1)
	print("[1]--->"+str(w1))
else:
	print("1er ARG Esta perdido")


#Conexion al password ------------------------------------
try:
	response2 = tn.read_until(b"password: ", timeout=100)
except EOFError as e:
	print ("Connection closed")

if b'password: ' in response2:
	print("[0.1]-> si encontro password")
	w2=passauto.encode("ascii")+b'\r\n'
	tn.write(w2)
	print("[2]--->"+str(w2))
else:
	print("2o ARG Esta perdido")

#Conexion exitosa ------------------------------------
try:
	response3 = tn.read_until(b'QNET> ' , timeout=100)
except EOFError as e:
	print ("Connection closed")

if b'QNET> ' in response3:
	print("[0.1]-> Conexion exitosa")
	tn.write("#OUTPUT,288,1,1".encode('ascii')+ b'\r\n')
	print("[0.1]-> Comando enviado ")
else:
	print("Conexion fallida en metodo 3")

#-------------------------------------------------------

#tn.write(b"ls\n")
tn.write(b"exit\n") #forzozo
