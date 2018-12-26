# Basic operators function as you expect, order of operations must be determined by parentheses
# % is the remainder operator, known as modulo
remainder = 111 % 5
print(remainder)

# raise a number to a power by using **
i = 2
square = i ** 2
cube = i ** 3
print(square)
print(cube)

# Operators can be used with strings in different ways

helloWorld = 'hello' + 'world'
print(helloWorld)

manyThanks = 'Thanks!' *10
print(manyThanks)

# Using operators with lists
evenNumbers = [2, 4, 6, 8]
oddNumbers = [1, 3, 5, 7]
someNumbers = oddNumbers + evenNumbers
print(someNumbers)
