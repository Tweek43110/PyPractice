# Dictionaries use keys and values to store information

phonebook = {}
phonebook["Alex"] = 6145320125
phonebook["Tracey"] = 4324772025
print(phonebook)
#OR
spicyList = {
    "Jalepeno" : "Sorta spicy",
    "Habenero" : "Very spicy",
    "Bhut Jolokia" : "Ultra spicy"
    }
print(spicyList)

# Iterating items in a dictionary is a bit more difficult than lists
for pepper, spiceIndex in spicyList.items():
    print("The %s is considered %s" % (pepper, spiceIndex))
    
# Removing values
del spicyList["Jalepeno"]
#OR
spicyList.pop("Habenero")
print(spicyList)

#Exercise
phonebook2 = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# write your code here
phonebook2["Jake"] = 938273443 #Adding to a dictionary***************
phonebook2.update({"Peter" : 6148330960})# Antoher way to add to a dictionary***********
phonebook2.pop("Jill")
print(phonebook2)

# testing code
if "Jake" in phonebook2:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook2:
    print("Jill is not listed in the phonebook.")
