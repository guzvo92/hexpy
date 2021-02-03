#import getpass
import telnetlib
from telnetlib import Telnet

class lutronmaster:

	def __init__(self,host,userman,passman):
		self.host = host
		self.tnco = telnetlib.Telnet(host)
		self.userman = userman
		self.passman = passman

	def conexion(self):
		self.conexion = False
		#Conexion al username -------------------------------------
		try:
			response = self.tnco.read_until(b'login: ', timeout=100)
		except EOFError as e:
			print ("Connection closed: " + str(e))

		if b"login: " in response:
			print("[Sys]-> Encontro Login Buffer")
			self.tnco.write(self.userman.encode("ascii") + b'\r\n')
		else:
			print("1er ARG Esta perdido")

		#Conexion al password ------------------------------------
		try:
			response2 = self.tnco.read_until(b"password: ", timeout=100)
		except EOFError as e:
			print ("Connection closed: " + str(e))

		if b'password: ' in response2:
			print("[Sys]-> Encontro password en Buffer")
			self.tnco.write(self.passman.encode("ascii")+b'\r\n')
		else:
			print("2o ARG Esta perdido")

		#Conexion exitosa ------------------------------------
		try:
			response3 = self.tnco.read_until(b'QNET> ' , timeout=100)
		except EOFError as e:
			print ("Connection closed")

		if b'QNET> ' in response3:
			print("[Sys]-> Conexion exitosa")
			self.conexion = True			
		else:
			self.conexion = False
			print("Conexion fallida en metodo 3")

		return self.conexion

	def send(self,parametro):
		if self.conexion == True:
			print ("[Sys]-> Status: Online")
			self.tnco.write(parametro.encode('ascii')+ b'\r\n')
			print("[Send]-> Comando enviado ")
		else:
			print ("[Sys]-> Status: Offline")
		#tnco.write(b"ls\n")

	def endconexion(self):
		self.tnco.write(b"exit\n") #forzozo
		print("[Sys]-> Conexion terminada ")


'''
import time 
test = lutronmaster("192.168.10.11","auvit","1234")
test.conexion()
test.send("#OUTPUT,288,1,0")
time.sleep(2)
test.send("#OUTPUT,288,1,1")
time.sleep(2)
test.endconexion()
'''

