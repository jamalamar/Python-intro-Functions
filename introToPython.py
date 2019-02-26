
#Function that return the sum of two numbers

def sum (x, y):
	return x + y

print(sum(4,6))




#Function that prints in reverse whatever you input

def rev (list):
	return list[::-1]

x = [1,2,3,4,5,6,7,8,9]
y = "Hello"

print(rev(y))



# def reverse (word):
# 	if (word == ''):
# 	 return ''
# 	else:
# 		return reverse(word[1::] + word[0:1:])

# print(reverse("Hello"))




#Function that takes a list and sorts them in order

def small_to_large (list):
	return list.sort()
		

z = [3,5,7,1,2,4,6,8,9]
w = ['H', 'Y', 'E', 'P', 'M']

small_to_large(z)
small_to_large(w)
print(w)




#Pass for empty code blocks

namee = "Jamal"
	
if namee != '':
	pass
else:
	namee = 'Default'




# print(dir(__name__))




def doSomenthing():
	def sayHello():
		message = "Hello HEllo Hello"
		print(locals())
	sayHello()

doSomenthing()





#nonlocal name ---> "Tristan" & "Christopher"

name = "Christopher"

def first():
	name = "AJ"
	def second():
		def third():
			nonlocal name
			name = "Tristan"
		third()
	second()
	print(name)
first()
print(name)










#SQUARE LIST (take a list of numbers, raise by power of 2, and return the sum of the new list)



#UNIQUE CHARACTERS (function that detetermines if a string contains all unique characters)



#FIZZBUZZ (thirds: FIZZ, fifths: BUZZ, divisible by 3 and 5: FIZZBUZZ)





