import random

output = ''
numOfRandNums = 20
upperRange = 1000
lowerRange = 0
with open('input.txt', 'w') as file:
    for i in range (0, numOfRandNums - 1):
        output += str(random.randrange(lowerRange, upperRange)) + ' '
    file.write(str(numOfRandNums) + '\n')
    file.write(output)