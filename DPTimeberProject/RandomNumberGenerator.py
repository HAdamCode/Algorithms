import random

output = ''
numOfRandNums = 1000
upperRange = 10000000
lowerRange = 0
with open('input.txt', 'w') as file:
    for i in range (0, numOfRandNums):
        output += str(random.randrange(lowerRange, upperRange)) + ' '
    file.write(str(numOfRandNums) + '\n')
    file.write(output)