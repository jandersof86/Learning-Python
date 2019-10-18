# String literals:

"hello"
'hello'

# Assign string to variable:

a = "hello"
print(a)

# Multiline strings:

a = """Lorem ipsum dolor sit blah
blah blah blah blah blah blah blah
blah"""
print(a)

# Strings are arrays:

a = "Say hello to the End."
print(a[1])

# Slicing:

b = "Hello, World"
print(b[2:5])

# Negative indexing:

b = "Hello, World"
print(b[-5:-2])

# String length:

a = "Hello, World"
print(len(a))

# String Methods: https://www.w3schools.com/python/python_ref_string.asp

a = " Hello, World "
print(a.strip())						# removes any whitespace from the beginning or end
print(a.lower())						# returns the string in lower case
print(a.upper())						# returns the string in upper case
print(a.replace("Hello", "Goodbye"))	# replaces a string with another string
print(a.split(","))						# splits string into substring if it finds instances of the given separator	

# Check string (boolean):

txt = "The rain in spain stays mainly in the plain"
x = "ain" in txt
print(x)

y = "ain" not in txt
print(y)

# String concatenation:

a = "hello"
b = "world"
c = a + b
c = "hello " + b
c = a + " " + b

# String format:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
my_order = "I want {} pieces of item number {} for {} dollars each."
print(my_order.format(quantity, itemno, price))

my_order = "I want to pay {2} dollars for {0} pieces of item {1}."
print(my_order.format(quantity, itemno, price))