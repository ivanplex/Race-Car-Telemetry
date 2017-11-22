#! /usr/bin/python

import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)
try:
	ser.isOpen()
	print("Serial is open")
except:
	print("Serial is closed")
	exit()

if(ser.isOpen()):
	try:
		while(1):
			print(ser.read())
	except Exception:
		print("error")
else:
	print("cannot open serial port")