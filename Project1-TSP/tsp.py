import sys
import math

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
    print(f"{total:.3f}")



arr = []
with open(sys.argv[1], "r") as inputFile:
    for line in inputFile:
        temp = line.split("\n")
        arr.append(temp[0])

n = arr[0]
point = []
for i in range(1, len(arr)):
    temp = arr[i].split(" ")
    p = [int(temp[0]), int(temp[1]), 0]
    point.append(p)

NearestNeighbor(point)
