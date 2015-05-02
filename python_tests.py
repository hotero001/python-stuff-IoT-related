#python tests
#sadly, have not used python in a while, and needed to run tests

class FirstClass:
	def setstuff(self, value):
		print self
		self.data = value

	def display(self, valx):
		print self.data
		print valx

x = FirstClass()
x.setstuff("King Arthur")

x.display("dog")

stepPin = [1,2,3,4]
print stepPin[0:4]