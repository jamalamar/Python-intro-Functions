
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



#Function that takes a list and sorts them in order

def small_to_large (list):
	return list.sort()
		

z = [3,5,7,1,2,4,6,8,9]
w = ['H', 'Y', 'E', 'P', 'M']

small_to_large(z)
small_to_large(w)
print(w)



