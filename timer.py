import time
import subprocess

def timer():
	timeleft = 600
	while timeleft > 0:
		print("timeleft = ", timeleft)
		time.sleep(1)
		timeleft -= 1
		
def buzzer():
    while True:
        subprocess.call(["aplay", "/usr/lib/libreoffice/share/gallery/sounds/train.wav"])
        time.sleep(0.5)

timer()
buzzer()	
