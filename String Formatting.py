# You can instert variables into strings using string modifiers
name = 'Kris Kringle'
print("Welcome back, %s!" % name)

#using two or more
age = 300
print("%s is %d years old" % (name, age))

myList = [1,2,3]
print("a list: %s" % myList)

#%s - String (or any object with a string representation, like numbers)
#%d - Integers
#%f - Floating point numbers
#%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
#%x/%X - Integers in hex representation (lowercase/uppercase)

#Exercise
data = ("John", "Doe", 53.44)
formatString= "Hello %s %s.Your current balance is %s." #data is  all seen as a string

print(formatString % data)
