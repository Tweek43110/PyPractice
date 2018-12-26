# Functions help divide code into blocks so it is easier to read and reusable
def myName():
    print('Hi, my name is Alex')

myName() # Calling on the function later

# Functions can also pass arguments
def myPhrase(person, holiday):
    print("Hello %s, we wish you a %s!" % (person, holiday))

myPhrase("Todd", "Merry Christmas") #passes the arguments into the function

def sumOfTwoNumbers(a, b):
    return a + b

print(sumOfTwoNumbers(9, 245))

# Exercise
# Modify this function to return a list of strings as defined above
def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % (benefit)

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
