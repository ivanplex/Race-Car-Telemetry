import serial
from xbee import XBee, ZigBee

serial_port = serial.Serial('/dev/ttyUSB0', 9600)
xbee = ZigBee(serial_port)

while True:
    try:
        xbee.at(command='ab')
        xbee.at(command='bc')
        xbee.at(command='cd')
        xbee.at(command='c1')
        xbee.at(command='!$')
        xbee.at(command=' d')
        xbee.at(command='|d')
        xbee.at(command=bytes([0x13, 0x8F]))
        # xbee.send('at', frame_id='B', command='DL')

    except KeyboardInterrupt:
        break

serial_port.close()
