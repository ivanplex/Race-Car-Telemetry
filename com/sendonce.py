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
		print(ser.write(b'\xff\xaa\x13\x98\x3d'))
	except Exception:
		print("error")
else:
	print("cannot open serial port")