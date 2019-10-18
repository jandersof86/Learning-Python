# Variables

x = 5;
y = "John";
print(x);
print(y);

x = 4; # x is an integer.
x = "Sally"; # x is now a string.

x = "John"
x = 'John'

# Assign value to multiple variables:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

# Output variables:

x = "awesome"
print("Python is " + x)

x = "Python is "
y = "awesome"
z = x + y
print(z)

x = 5
y = 10
print(x + y)

# Global variables:

x = "awesome"

def my_function():
	print("Python is " + x)

my_function()

def my_other_function():
	global x
	x = "fantastic"

my_other_function()
print("Python is " + x)

# Casting - Specify a variable type:

x = float(1)		# will be 1.0
y = float(2.8)		# will be 2.8
z = float("3")		# will be 3.0
w = float("4.2")	# will be 4.2

x = str("s1")		# will be "s1"
y = str(2)			# will be "2"
z = str(3.0)		# will be "3.0"