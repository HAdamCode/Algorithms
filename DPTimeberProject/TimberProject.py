import sys

numberOfCalls = 0

def T(i, j):
    global numberOfCalls
    numberOfCalls += 1
    if (j == i):
        return l[i]
    if (j == i + 1):
        return max(l[i], l[j])
    return max(l[i] + min(T(i + 2, j), T(i + 1, j - 1)), l[j] + min(T(i + 1, j - 1), T(i, j - 2)))

numberOfValues= 0
segmentNumbers = []
l = []
with open(sys.argv[1], 'r') as file:
    i = 0
    for line in file:
        if i == 0:
            numberOfValues = int(line)
        elif i == 1:
            lineString = line
        i += 1

lineStringList = lineString.split(' ')
for line in lineStringList:
    if line == '':
        continue
    l.append(int(line))
print(numberOfValues)
print('Max value:', T(0, numberOfValues-2))
print('The number function calls:', numberOfCalls)
print(segmentNumbers)