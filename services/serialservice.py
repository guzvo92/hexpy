
import serial
from serial import Serial


def escritura(string):
	ser = serial.Serial('/dev/ttyAMA0')  # open serial port
	print(ser.name)         # check which port was really used
	ser.write(b+ str(string))
	ser.close()             # close port


