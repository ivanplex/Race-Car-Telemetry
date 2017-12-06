# Import a library of functions called 'pygame'
import pygame
import time
import random
import math
 
# Initialize the game engine
pygame.init()
 
# Set the height and width of the screen
size = [2048, 800]
screen = pygame.display.set_mode(size)

PIXEL_SIZE = 8

lineScanBuffer = []
 
pygame.display.set_caption("Camera Feed")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

def camerafeed(shift):

	line = []

	for x in range(int(2048/PIXEL_SIZE)):
		val = (x-shift-50)*(x-shift-100)*(x-shift-200)*(x-shift-238) / -60000
		if val > 255:
			val = 255
		elif val < 0:
			val = 0
		#print val
		line.append(val)

	lineScanBuffer.append(line)
    
 


while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
	clock.tick(10)
     
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			done=True # Flag that we are done so we exit this loop
 
	screen.fill((0,0,0)) # Paint Canvas Black

	for y in range(int(800/PIXEL_SIZE)):

		if(len(lineScanBuffer) > int(800/PIXEL_SIZE)):
			lineScanBuffer.pop(0)
		if(len(lineScanBuffer) <= int(800/PIXEL_SIZE)):
			shift = int(3*math.sin(y/50)*random.randint(0, 2))
			camerafeed(shift)
			print("shift:  "+ str(y) + "  " + str(shift))

		for x in range(int(2048/PIXEL_SIZE)):
			# cr = random.randint(0, 255)
			# cg = random.randint(0, 255)
			# cb = random.randint(0, 255)

			b = lineScanBuffer[y]
			pygame.draw.rect(screen, (b[x],b[x],b[x]), [x*PIXEL_SIZE, y*PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE])
        	
			# Centre line
			pygame.draw.rect(screen, (255,0,0), [1016, y*PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE])
		#time.sleep(0.02)
		# Go ahead and update the screen with what we've drawn.
		# This MUST happen after all the other drawing commands.
		pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()