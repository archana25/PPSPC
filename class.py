class Practice:
	def __init__(self,filename,speed,signal):
		self.filename = filename
		self.speed=speed
		self.signal = signal



object1 = Practice('name','23','1')
print object1.filename
print object1.speed
print object1.signal

object2 = Practice('frido',None,'45654')
print object2.filename
print object2.speed
print object2.signal

