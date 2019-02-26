class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age * 7


alf = Dog("Alf", 5)

print(alf.name)
print(alf.age)
