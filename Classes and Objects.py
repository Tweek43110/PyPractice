# Objects are encapsuled variables and functions in one entity. The classes are templates to create objects
class firstClass:
    exampleVar = "Some text"

    def someFunction(self):
        print("This message will self destruct if opened.")

myFirstObject = firstClass() #saves class attributes to the object

print(myFirstObject.exampleVar) # use dot notations to access information inside

# You can make multiple objects from the classes
mySecondObject = firstClass()
mySecondObject.exampleVar = "Different words"

print(myFirstObject.exampleVar)
print(mySecondObject.exampleVar)

myFirstObject.someFunction() # access internal functions using dot notation as well

#Exercise
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car2 = Vehicle()

car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000.00

car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())
