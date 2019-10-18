
# (Data type categories)
# Text Type: str
# Numeric Types: int, float, complex
# Sequence Types: list, tuple, range
# Mapping Type: dict
# Boolean Types: bool
# Binary Types: bytes, bytearray, memoryview

# Getting the data type:

x = 5
print(type(x))

# Setting the data type:

x = str("Hello")
x = int(20)
x = float(2.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name="John", age=36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(5)