
arr = []
x = []
y = []
with open("test.txt", "r") as inputFile:
    for line in inputFile:
        temp = line.split("\n")
        arr.append(temp[0])

n = arr[0]
for i in range(1, len(arr)):
    temp = arr[i].split(" ")
    x.append(temp[0])
    y.append(temp[1])

