

def decode(hexdata):
	if(hexdata == b'\x21'):
		print('Command: ')
	else:
		print()



def parseInteger(barray):
	for i in range(0,len(barray)):
		print(int(barray[i]))
	

parseInteger(b'\xcf')

parseInteger(b'\xcf\x55\x37')