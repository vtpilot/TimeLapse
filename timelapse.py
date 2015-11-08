#!/usr/bin/python

import time
import subprocess
import datetime

pics=10
wait=60

now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
OutputDir = "/home/pi/Photos/TimeLapse/" + now

### Configure Camera
# CaptureTarget=1 / Save to CF Card

subprocess.call("gphoto2 --set-config capturetarget=1 --set-config imageformat=0", shell=True)

print "Starting Time Lapse"

try:
	for i in range(1,pics):
		print "Taking Picture " + str(i) + "  of " + str(pics)		
			
		output = subprocess.call("gphoto2 --capture-image-and-download --filename " + OutputDir + "/" + str(i) + ".%C", shell=True)
		print(output)

		time.sleep(wait)

except KeyboardInterrupt:  
    print "Detected Keyboard Interrupt"
  
except:  
    print "Other error or exception occurred!"  
  
finally:  
    GPIO.cleanup()
		
