
import sys
import time

numberOfCalls = 0

def T(i, j):
    if (j == i):
        return table[i][j]
    if (j == i + 1):
        return table[i][j]

    first = 0
    second = 0
    third = 0

    if table[i+2][j] != -1:
        first = table[i+2][j]
    else:
        first = T(i + 2, j)
    if table[i+1][j-1] != -1:
        second = table[i+1][j-1]
    else:
        second = T(i+1, j-1)
    if table[i][j-2] != -1:
        third = table[i][j-2]
    else:
        third = T(i, j - 2)

    if l[i] + min(first, second) >= l[j] + min(second, third):
        if first > second:
            traceBack[i][j].append(i+1)
            traceBack[i][j].append(j+1)
            table[i][j] = l[i] + second
            return l[i] + second
        else:
            traceBack[i][j].append(i+1)
            traceBack[i][j].append(i+2)
            table[i][j] = l[i] + first
            return l[i] + first
    else:
        if second > third:
            traceBack[i][j].append(j+1)
            traceBack[i][j].append(j)
            table[i][j] = l[j] + third
            return l[j] + third
        else:
            traceBack[i][j].append(j+1)
            traceBack[i][j].append(i+1)
            table[i][j] = l[j] + second
            return l[j] + second

def Traceback(i, j):
    if i == j:
        print("My turn:", traceBack[i][j][0])
        return
    
    print("My turn:", traceBack[i][j][0])
    print("Neighbors turn:", traceBack[i][j][1])

    if i + 2 > j:
        return
    if traceBack[i][j][0] != i+1:
        if (traceBack[i][j][1] == j):
            Traceback(i, j-2)
        else:
            Traceback(i+1, j-1)
    else:
        if traceBack[i][j][1] == i+2:
            Traceback(i+2, j)
        else:
            Traceback(i+1, j-1)


start = time.time()
numberOfValues= 0
l = []
table = []
traceBack = []
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

for i in range(0, numberOfValues):
    table.append([])
    traceBack.append([])
    for j in range(0, numberOfValues):
        traceBack[i].append([])
        if i == j:
            table[i].append(l[i])
        else:
            table[i].append(-1)
            
        
for i in range(0, numberOfValues):
    traceBack[i][i].append(i+1)
    
for i in range(0, numberOfValues-1):
    if l[i] >= l[i+1]:
        table[i][i+1] = l[i]
        traceBack[i][i+1].append(i+1)
        traceBack[i][i+1].append(i+2)
    else:
        table[i][i+1] = l[i+1]
        traceBack[i][i+1].append(i+2)
        traceBack[i][i+1].append(i+1)


print(T(0, numberOfValues-1))
Traceback(0, numberOfValues-1)