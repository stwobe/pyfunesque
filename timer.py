#!/usr/bin/env python

# author: Steve Roberts
# date: 12th June 2017
# time: 19:25 BST
# github - https://stwobe.github.com/pyfunesque

'''
timer app - with sounds! yay!! Fun!
See ReadMe file for which other programs you may need to run this
'''

import time # see below - this is used pause/count the seconds
import subprocess # this is for calling commands from Bash - see below

def timer(): # our main timer function
	timeleft = 600 #default is 10 minutes = 600 seconds - warm up oven
	while timeleft > 0: # set up while loop for timer
		print("timeleft = ", timeleft) #print how many seconds are left
		time.sleep(1) # halt the program for one second on each pass
		timeleft -= 1 # subtract one second each time around
		
def buzzer(): # the code for our buzzer
    while True: # the infinit loop!
        subprocess.call(["aplay", "/usr/lib/libreoffice/share/gallery/sounds/train.wav"])
        # the above command calls to Bash to play that sound file
        time.sleep(0.5) # the gap between playing the sound each time

timer() # jump top and run the timer() function shown above
buzzer() # then run the code in the buzzer function	

# this code needs lots of improving, such as..
# put the functions into separate files
# use a bash command or Python command that plays sound anywhere
