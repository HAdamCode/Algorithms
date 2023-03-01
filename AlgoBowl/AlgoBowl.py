input_file = open('input.txt')

num_targets = int(input_file.readline())

targets = [int(n) for n in input_file.readline().split(" ")]


prevUsed = [1]
finalArr = []

def recurseFunction(cur_num): 
    greatest = 0
    for j in prevUsed:
        if j <= cur_num and j > greatest:
            greatest = j
    if cur_num - greatest in prevUsed:
        finalArr.append([greatest, cur_num - greatest])
        prevUsed.append(cur_num)
        return
    else:
        recurseFunction(cur_num-greatest)
        finalArr.append([greatest, cur_num - greatest])
        prevUsed.append(cur_num)

def whileLoop(cur_num):
    while(True):
        if (cur_num in prevUsed):
            return
        for item in reversed(prevUsed):
            if (item + max(prevUsed) <= cur_num):
                finalArr.append([item, max(prevUsed)])
                prevUsed.append(item + max(prevUsed))
                break

        
for i in range(num_targets):
    try:
        if (max(prevUsed) < targets[i]/10):
            whileLoop(targets[i])
        elif (max(prevUsed) == 1):
            whileLoop(targets[i])
        else:
            recurseFunction(targets[i])
    except:
        whileLoop(targets[i])


f = open("myfile.txt", "w")
f.write(str(len(finalArr)) + '\n')
for final in finalArr:
    temp = str(final[0]) + ' ' + str(final[1]) + '\n'
    f.write(temp)
