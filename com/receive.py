import serial
from xbee import XBee, ZigBee

serial_port = serial.Serial('/dev/ttyUSB0', 9600)
xbee = ZigBee(serial_port)

while True:
    try:
        print(xbee.wait_read_frame())
    except KeyboardInterrupt:
        break

serial_port.close()