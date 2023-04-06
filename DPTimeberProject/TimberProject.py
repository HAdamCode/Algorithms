l = [33, 28, 35, 25, 29, 34, 28, 32]
numberOfCalls = 0

def T(i, j):
    global numberOfCalls
    numberOfCalls += 1
    if (j == i):
        return l[i]
    if (j == i + 1):
        return max(l[i], l[j])
    return max(l[i] + min(T(i + 2, j), T(i + 1, j - 1)), l[j] + min(T(i + 1, j - 1), T(i, j - 2)))

with open("input.txt", 'r') as file:
    file.read
print('Max value:', T(0, 7))
print('The number function calls:', numberOfCalls)