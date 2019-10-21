# Exception handling

def error_func(divide_by):
	return 42 // divide_by

#print(error_func(0)) # Results in ZeroDivisionError

########################################

def try_func(divide_by):
	try:
		return 42 // divide_by
	except ZeroDivisionError:
		print("Error: Invalid argument.")

#print(try_func(0))

def try_func2(divide_by):
	return 42 // divide_by

try:
	print(try_func2(1))
	print(try_func2(0))
except ZeroDivisionError:
	print("Error: Invalid argument.")