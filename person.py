class Person:
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex

	def printPerson(self):
		print("{}: Age: {}, Sex: {}".format(self.name, self.age, self.sex))