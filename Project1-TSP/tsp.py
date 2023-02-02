import sys
import math
from itertools import permutations

def NearestNeighbor(arr):
    p = arr[0]
    position = 0
    total = 0
    smallestDistance = 0
    smallestPosition = []
    startX = arr[position][0]
    startY = arr[position][1]
    while True:
        smallestDistance = 0
        for i in range(1, len(arr)):
            if arr[i][2] == 1:
                continue
            if smallestDistance == 0:
                smallestPosition = arr[i]
                smallestDistance = math.sqrt(pow(arr[i][0] - startX, 2) + pow(arr[i][1] - startY, 2))
                continue
            if math.sqrt(pow(arr[i][0] - startX, 2) + pow(arr[i][1] - startY, 2)) < smallestDistance:
                smallestDistance = math.sqrt(pow(arr[i][0] - startX, 2) + pow(arr[i][1] - startY, 2))
                smallestPosition = arr[i]
        startX = smallestPosition[0]
        startY = smallestPosition[1]
        if len(smallestPosition) == 0 or smallestPosition[2] == 1:
            total += math.sqrt(pow(smallestPosition[0] - p[0], 2) + pow(smallestPosition[1] - p[1], 2))
            break
        else:
            smallestPosition[2] = 1
            total += smallestDistance
    return total

def OptimalTSP(arr):
    d = math.inf
    first = True
    for perm in permutations(arr):
        if first:
            first = False
            xInit = perm[0][0]
            yInit = perm[0][1]
        distance = 0
        x = perm[0][0]
        y = perm[0][1]
        if x != xInit and y != yInit:
            break
        for i in range(1, len(perm)):
           distance += math.sqrt(math.pow(perm[i][0]-x, 2) + pow(perm[i][1] - y, 2))
           x = perm[i][0]
           y = perm[i][1]
        distance += math.sqrt(math.pow(perm[0][0]-perm[-1][0], 2) + pow(perm[0][1] - perm[-1][1], 2))
        if distance < d:
            d = distance
    print(f"{d:.3f}")




arr = []
with open(sys.argv[1], "r") as inputFile:
    for line in inputFile:
        temp = line.split("\n")
        arr.append(temp[0])

n = arr[0]
point = []
for i in range(1, int(n)+1):
    temp = arr[i].split(" ")
    p = [int(temp[0]), int(temp[1]), 0]
    point.append(p)


OptimalTSP(point)
