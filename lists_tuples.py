# Lists and tuples

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, "three", "four", "five"]
list3 = [[1, "two", 3],["four", 5, 6, 7]]

# Getting individual values in a list with indexes:

list1[1] 		# 2
list2[3] 		# "four"

list3[0] 		# [1, "two", 3]
list3[0][1] 	# "two"
list3[1][3] 	# 7

# Negative indexes:

list1[-1] 		# 5
list1[-3] 		# 3
list3[-1][-2] 	# 6

# Getting a list's length with len():

len(list1) 		# 5
len(list2)		# 5
len(list3)		# 2 - counts the number of immediate entities/groups.

# Changing calues in a list with indexes:

animals = ["cat", "bat", "rat", "elephant"]
animals[1] = aardvark		# animals = ["cat", "aardvark", "rat", "elephant"]
animals[2] = animals[1]		# animals = ["cat", "aardvark", "aardvark", "elephant"]
animals[-1] = animals[2]	# animals = ["cat", "aardvark", "aardvark", "aardvark"]

# List concatenation and replication:

[1, 2, 3] + ["A", "B", "C"]	# [1, 2, 3, "A", "B", "C"]
['X', 'Y', 'Z'] * 3			# ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
test_list = [9, 8, 7]
test_list = test_list + ["C", "D", "E"]		# test_list = [9, 8, 7, "C", "D", "E"]

# Removing values from a list with del statement:

test_list = [9, 8, 7, "C", "D", "E"]
del test_list[2]			# test_list = [9, 8, "C", "D", "E"]
del test_list[-3]			# test_list = [9, 8, "D", "E"]

# Refer to cat_names_exercise.py

# Using for loops with lists:
	
for i in [1, 2, 3, 4]:
	print(i)				# 0
							# 1
							# 2 
							# 3

		# for i in range(len(list))
supplies = ["pens", "pencils", "staplers", "flame-throwers", "binders"]
for i in range(len(supplies)):
	print("Index " + str(i) + " in supplies is: " + supplies[i])
							# Index 0 in supplies is: pens
							# Index 1 in supplies is: pencils
							# Index 2 in supplies is: staplers
							# Index 3 in supplies is: flame-throwers
							# Index 4 in supplies is: binders

# The in and not in operators:

"howdy" in ["hello", "hi", "howdy", "heyas"]	# True
another_list = [1, 2, 3, "four", "five", "six"]
"four" in another_list		# True
7 in another_list			# False
"four" not in another_list	# False

# The multiple assignment trick:

cat = ["fat", "black", "loud"]
size = cat[0]
color = cat[1]
disposition = cat[2]

cat = ["fat", "black", "loud"]
size, color, disposition = cat

# Augmented assignment operators:

bacon = ["Zophie", "Chucky"]
bacon *= 3			# bacon = ["Zophie", "Chucky", "Zophie", "Chucky", "Zophie", "Chucky"]

# METHODS
# Finding a vlue in a list with index() method:

spam = ["hello", "hi", "howdy", "heyas"]
spam.index("hello")		# 0

spam = ["Zophie", "Fat-tail", "Pooka", "Ralph", "Pooka"]
spam.index("Pooka")		# 2

# Adding values to lists with the append() and insert() methods:

spam = ["cat", "dog", "cow"]
spam.append("moose")	# spam = ["cat", "dog", "cow", "mooose"]
spam.insert(1, "chicken")	# spam = ["cat", "chicken", "dog", "cow", "moose"]

# Removing values from lists with the remove() method:

spam = [1, 2, 3, 4]
spam.remove(4)			# spam = [1, 2, 3]

		#NOTE: The remove() method is good for when you know the value. Otherwise,
		# the del statement is best for index numbers.

