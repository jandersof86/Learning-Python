# this program will take the names of all the user's cats and list them at the end.

cat_names = []

while True:
	print("Enter the name of cat " + str(len(cat_names) +1) + " (Or simply press enter to stop.): ")
	name = input()
	if name == "":
		break
	cat_names = cat_names + [name] # list concatenation
print("The cat names are:")
for name in cat_names:
	print("	" + name)