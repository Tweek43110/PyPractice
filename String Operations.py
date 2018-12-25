#Finding string length
string = 'Hello there'
print(len(string))

#Finding an index number for a string letter, remeber it uses 0 indexing
print(string.index("h"))

#printing only aselection of text
print(string[2:7])
#prints starting at a certain number and goes to the end
print(string[3:])
#prints at start number to end number btu skips every 2(again zero index) characters
print(string[3:11:3])
#reversing a string
print(string[::-1])

#creating all caps or lowercase
print(string.upper())
print(string.lower())

#A way to check if a string starts or ends with something
print(string.startswith('Hello'))#returns true
print(string.endswith('cheese'))#returns false

#to split the string aa certain character into a list, use this
twoWords = string.split(" ")
print(twoWords)
