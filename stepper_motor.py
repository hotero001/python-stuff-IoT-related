#motor

import sys
import time
import RPi.GPIO as GPIO
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24
StepPins = [17,22,23,24]
 
# Set all pins as output
for pin in StepPins:
  print "Setup pins"
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)
 
# Define advanced sequence
# as shown in manufacturers datasheet
Seq = [[1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1],
       [1,0,0,1]]
        
StepCount = len(Seq)-1
StepDir = 2 # Set to 1 or 2 for clockwise
            # Set to -1 or -2 for anti-clockwise
 
# Read wait time from command line
if len(sys.argv)>1:
  WaitTime = int(sys.argv[1])/float(1000)
else:
  WaitTime = 10/float(1000)
 
# Initialise variables
StepCounter = 0
angles = [0, 30, 60, 90, 120, 150, 180]
 
# Start main loop
spin = input("Press and enter '7' to start spinning the motor clock-wise. Press and enter '8' to start spinning the motor counter-clock-wise. Press and enter any number from 0 to 6 to affix the motor to a certain angle")
print "press and enter '9' at any time to stop spinning the motor"
#this first option in the conditional statement keeps spinning the motor clock-wise indefinitely, until the user intervenes
if spin == 7:
	while spin == 7:
	 
	  for pin in range(0, 4):
	    xpin = StepPins[pin]
	    #print "press and enter '7' to stop spinning the motor"#StepCounter
	    #print "press and enter '7' to stop spinning the motor"#pin
	    if Seq[StepCounter][pin]!=0:
	      #print "press and enter '7' to stop spinning the motor"#" Step %i Enable %i" %(StepCounter,xpin)
	      GPIO.output(xpin, True)
	    else:
	      GPIO.output(xpin, False)

	  #line below will turn the motor clock-wise 
	  StepCounter += StepDir
	  #line below, which is commented out, will turn the motor counter-clock-wise
	  #StepCounter -= StepDir
	 
	  # If we reach the end of the sequence
	  # start again
	  if (StepCounter>=StepCount):
	    StepCounter = 0
	  if (StepCounter<0):
	    StepCounter = StepCount
	 
	  # Wait before moving on
	  time.sleep(WaitTime)
#this option in the conditional statement keeps spinning the motor counter-clock-wise indefinitely, until the user intervenes
elif spin == 8:
	while spin == 8:
		for pin in range(0, 4):
	    xpin = StepPins[pin]
	    #print "press and enter '7' to stop spinning the motor"#StepCounter
	    #print "press and enter '7' to stop spinning the motor"#pin
	    if Seq[StepCounter][pin]!=0:
	      #print "press and enter '7' to stop spinning the motor"#" Step %i Enable %i" %(StepCounter,xpin)
	      GPIO.output(xpin, True)
	    else:
	      GPIO.output(xpin, False)

	  #line below will turn the motor clock-wise 
	  StepCounter -= StepDir
	  #line below, which is commented out, will turn the motor counter-clock-wise
	  #StepCounter -= StepDir
	 
	  # If we reach the end of the sequence
	  # start again
	  if (StepCounter>=StepCount):
	    StepCounter = 0
	  if (StepCounter<0):
	    StepCounter = StepCount
	 
	  # Wait before moving on
	  time.sleep(WaitTime)
#this option will affix the motor to angle 0, regardless of its starting position
elif spin == 0:
	while spin == 0:
		for pin in range(0, 4):
	    xpin = StepPins[pin]
	    #print "press and enter '7' to stop spinning the motor"#StepCounter
	    #print "press and enter '7' to stop spinning the motor"#pin
	    if Seq[StepCounter][pin]!=0:
	      #print "press and enter '7' to stop spinning the motor"#" Step %i Enable %i" %(StepCounter,xpin)
	      GPIO.output(xpin, True)
	    else:
	      GPIO.output(xpin, False)

	  #line below will turn the motor clock-wise 
	  while StepCounter += StepDir
	 
	  # If we reach the end of the sequence
	  # start again
	  if (StepCounter>=StepCount):
	    StepCounter = 0
	  if (StepCounter<0):
	    StepCounter = StepCount
	 
	  # Wait before moving on
	  time.sleep(WaitTime)
#this option will affix the motor to angle 1, regardless of its starting position
elif spin == 1:
	while spin == 1:
		for pin in range(0, 4):
	    xpin = StepPins[pin]
	    #print "press and enter '7' to stop spinning the motor"#StepCounter
	    #print "press and enter '7' to stop spinning the motor"#pin
	    if Seq[StepCounter][pin]!=0:
	      #print "press and enter '7' to stop spinning the motor"#" Step %i Enable %i" %(StepCounter,xpin)
	      GPIO.output(xpin, True)
	    else:
	      GPIO.output(xpin, False)

	  #line below will turn the motor clock-wise 
	  while StepCounter += StepDir
	 
	  # If we reach the end of the sequence
	  # start again
	  if (StepCounter>=StepCount):
	    StepCounter = 0
	  if (StepCounter<0):
	    StepCounter = StepCount
	 
	  # Wait before moving on
	  time.sleep(WaitTime)
#this option will affix the motor to angle 2, regardless of its starting position
elif spin == 2:
	while spin == 2:
		for pin in range(0, 4):
	    xpin = StepPins[pin]
	    #print "press and enter '7' to stop spinning the motor"#StepCounter
	    #print "press and enter '7' to stop spinning the motor"#pin
	    if Seq[StepCounter][pin]!=0:
	      #print "press and enter '7' to stop spinning the motor"#" Step %i Enable %i" %(StepCounter,xpin)
	      GPIO.output(xpin, True)
	    else:
	      GPIO.output(xpin, False)

	  #line below will turn the motor clock-wise 
	  StepCounter += StepDir

	  #line below, which is commented out, will turn the motor counter-clock-wise
	  #StepCounter -= StepDir
	 
	  # If we reach the end of the sequence
	  # start again
	  if (StepCounter>=StepCount):
	    StepCounter = 0
	  if (StepCounter<0):
	    StepCounter = StepCount
	 
	  # Wait before moving on
	  time.sleep(WaitTime)
#this option will affix the motor to angle 3, regardless of its starting position
elif spin == 3:
	while spin == 3:
		for pin in range(0, 4):
	    xpin = StepPins[pin]
	    #print "press and enter '7' to stop spinning the motor"#StepCounter
	    #print "press and enter '7' to stop spinning the motor"#pin
	    if Seq[StepCounter][pin]!=0:
	      #print "press and enter '7' to stop spinning the motor"#" Step %i Enable %i" %(StepCounter,xpin)
	      GPIO.output(xpin, True)
	    else:
	      GPIO.output(xpin, False)

	  #line below will turn the motor clock-wise 
	  StepCounter += StepDir
	  #line below, which is commented out, will turn the motor counter-clock-wise
	  #StepCounter -= StepDir
	 
	  # If we reach the end of the sequence
	  # start again
	  if (StepCounter>=StepCount):
	    StepCounter = 0
	  if (StepCounter<0):
	    StepCounter = StepCount
	 
	  # Wait before moving on
	  time.sleep(WaitTime)
#this option will affix the motor to angle 4, regardless of its starting position
elif spin == 4:
	while spin == 4:
		for pin in range(0, 4):
	    xpin = StepPins[pin]
	    #print "press and enter '7' to stop spinning the motor"#StepCounter
	    #print "press and enter '7' to stop spinning the motor"#pin
	    if Seq[StepCounter][pin]!=0:
	      #print "press and enter '7' to stop spinning the motor"#" Step %i Enable %i" %(StepCounter,xpin)
	      GPIO.output(xpin, True)
	    else:
	      GPIO.output(xpin, False)

	  #line below will turn the motor clock-wise 
	  StepCounter += StepDir
	  #line below, which is commented out, will turn the motor counter-clock-wise
	  #StepCounter -= StepDir
	 
	  # If we reach the end of the sequence
	  # start again
	  if (StepCounter>=StepCount):
	    StepCounter = 0
	  if (StepCounter<0):
	    StepCounter = StepCount
	 
	  # Wait before moving on
	  time.sleep(WaitTime)
#this option will affix the motor to angle 5, regardless of its starting positon
elif spin == 5:
	while spin == 5:
		for pin in range(0, 4):
	    xpin = StepPins[pin]
	    #print "press and enter '7' to stop spinning the motor"#StepCounter
	    #print "press and enter '7' to stop spinning the motor"#pin
	    if Seq[StepCounter][pin]!=0:
	      #print "press and enter '7' to stop spinning the motor"#" Step %i Enable %i" %(StepCounter,xpin)
	      GPIO.output(xpin, True)
	    else:
	      GPIO.output(xpin, False)

	  #line below will turn the motor clock-wise 
	  StepCounter += StepDir
	  #line below, which is commented out, will turn the motor counter-clock-wise
	  #StepCounter -= StepDir
	 
	  # If we reach the end of the sequence
	  # start again
	  if (StepCounter>=StepCount):
	    StepCounter = 0
	  if (StepCounter<0):
	    StepCounter = StepCount
	 
	  # Wait before moving on
	  time.sleep(WaitTime)
#this option will affix the motor to angle 6, regardless of its starting position
elif spin == 6:
	while spin == 6:
		for pin in range(0, 4):
	    xpin = StepPins[pin]
	    #print "press and enter '7' to stop spinning the motor"#StepCounter
	    #print "press and enter '7' to stop spinning the motor"#pin
	    if Seq[StepCounter][pin]!=0:
	      #print "press and enter '7' to stop spinning the motor"#" Step %i Enable %i" %(StepCounter,xpin)
	      GPIO.output(xpin, True)
	    else:
	      GPIO.output(xpin, False)

	  #line below will turn the motor clock-wise 
	  StepCounter += StepDir
	  #line below, which is commented out, will turn the motor counter-clock-wise
	  #StepCounter -= StepDir
	 
	  # If we reach the end of the sequence
	  # start again
	  if (StepCounter>=StepCount):
	    StepCounter = 0
	  if (StepCounter<0):
	    StepCounter = StepCount
	 
	  # Wait before moving on
	  time.sleep(WaitTime)


