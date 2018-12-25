# Lists
groceryList = ['kiwi', 'chicken breast', 'bread']
print(groceryList)
groceryList.append('lunch meat')
print(groceryList)

numbers = []
strings = []

strings = ['Alex', 'Steve', 'Chuck']
print(strings)
numbers = [3, 4, 5]
print(numbers)

strings.append('John')
strings.append('Jane')
print(strings)

strings.append(numbers)
print(strings)
#creates nested list accessible with this notation
print(strings[5][1])
