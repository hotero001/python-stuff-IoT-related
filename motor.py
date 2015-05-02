import sys
import time
#import Rpi.GPIO as GPIO

class Motor_28BJY:
	MOTOR_PIN1 = 22
	MOTOR_PIN2 = 23
	MOTOR_PIN3 = 24
	MOTOR_PIN4 = 27
	#position counter
	position = 0

	def __init__(self):
		#Set the gpio-pins to output and set initial state
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)

		GPIO.setup(self.MOTOR_PIN1, GPIO.OUT)
		GPIO.setup(self.MOTOR_PIN2, GPIO.OUT)
		GPIO.setup(self.MOTOR_PIN3, GPIO.OUT)
		GPIO.setup(self.MOTOR_PIN4, GPIO.OUT)

	def move(self, steps, dir, delay=0.1):
		for _ in range(steps):
			if dir:
				position += 1
				#place your code for stepping up one step here
			else:
				position -= 1
				#place your code for stepping down one step here

			time.sleep(delay)

		def getPosition(self):
			return position

#let 'er buck
#motor = Motor_28BJY()
#motor.move(100, True)

#The line directly below should be the GUI of one button; both buttons should be displayed simultaneously, seperated by some pixels
user_input_one = input("Press 1 to open blinds clock-wise, or press 2 to open blinds counter-clock-wise: ")

#And the button should now display the following if it is actuated correctly from the above step
if user_input_one == 1 or user_input_one == 2:
	input("Press 5 to stop the blinds in place")

#The line directly below should be the GUI of the other button; both buttons should be displayed simultaneously, seperated by some pixels
user_input_two = input("Press any button from 4-9 to shift the blinds in the button's respective position: ")

#After a button from 4-9 is pressed, the RPi will be actuated in one of the following options
if user_input_two == 4:
	#code to shift the blinds in the 4 position
	print "t"
elif user_input_two == 5:
	#code to shift the blinds in the 5 position
	print "t"
elif user_input_two == 6:
	#code to shift the blinds in the 6 position
	print "t"
elif user_input_two == 7:
	#code to shift the blinds in the 7 position
	print "t"
elif user_input_two == 8:
	#code to shift the blinds in the 8 position
	print "t"
elif user_input_two == 9:
	#code to shift the blinds in the 9 position
	print "t"
else:
	#do nothing
	print "t"



