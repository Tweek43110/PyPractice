# To check for True or False
x=5
print(x == 5)
print(x == 3)
print(x > 3)

#Complex boolean expressions using IF statements and AND OR conditions
user = "Peter"
age = 17
if user == "Peter" and age == 17:
    print("Welcome back %s" % user)\

if user == "Peter" or user == "Thomas":
    print("You have won a special gift")
    
#using the IN operator
if user in ['John', 'Peter', 'Joseph']:
    print('Your name is on the list')

#Python does not use terminator symbols like ;, it uses tabs
i = 4
if i <=5:
    print('The number is less than 5')
else:
    print('The number is greater than 5')

#Sometime the true and false needs to be checked another way, for example
x = [1,2,3]
y=[1,2,3]
print(x == y)
print(x is y)

# The NOT operator shows the opposite
print(not False)
