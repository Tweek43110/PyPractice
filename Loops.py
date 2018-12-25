# There are two type of loops available FOR and WHILE
# FOR examples
simpleTest = [1,2,3,4]
for number in simpleTest:
    print(number)

# another useful example
for i in range(12, 20):
    print(i)

for evenNumbers in range(0,20,2):
    print(evenNumbers)

# WHILE examples
x = 0
while x < 5:
    print(x)
    x += 1

# BREAKs can help end a loop
answer = 46
while True:
    print(answer)
    answer +=1
    if answer >= 50:
        break # stops the loop from going on forever until crash

# CONTINUE is used as an answer check
for top in range(10):
    if x % 2 == 0: #checks that the answer does not have a remainder
        continue
    print(top)

#Using ELSE statements
count = 1
while(count < 9):
    print(count)
    count +=1
else:
    print('The counting loop has ended!')

#Practice
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]
for i in numbers:
    if i % 2 == 0:
        print(i)
        i +=i
    if i == 237:
        break

    # Or the soultion could be:
    #for i in numbers:
        #if number == 237: STOPS FOR THE REQUESTED NUMBER
            #break
        #if number %2 == 1; IF THE NUMBER IS NOT EVEN IT WILL NOT BE PRINTED
            #continue
    #print(number)

