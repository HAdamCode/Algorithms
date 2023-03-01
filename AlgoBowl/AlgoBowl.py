input_file = open('input.txt')

num_targets = int(input_file.readline())

targets = [int(n) for n in input_file.readline().split(" ")]


prev_usedWhile = [1]
counter = 0
finalArrWhile = []

def anything(cur_num): 
    greatest = 0
    for j in prev_usedWhile:
        if j <= cur_num and j > greatest:
            greatest = j
    if cur_num - greatest in prev_usedWhile:
        finalArrWhile.append([greatest, cur_num - greatest])
        prev_usedWhile.append(cur_num)
        return
    else:
        anything(cur_num-greatest)
        finalArrWhile.append([greatest, cur_num - greatest])
        prev_usedWhile.append(cur_num)

def whileLoop(cur_num):
    while(True):
        if (cur_num in prev_usedWhile):
            return
        for item in reversed(prev_usedWhile):
            if (item + max(prev_usedWhile) <= cur_num):
                finalArrWhile.append([item, max(prev_usedWhile)])
                prev_usedWhile.append(item + max(prev_usedWhile))
                # prev_usedWhile.sort(reverse=True)
                break

        
for i in range(num_targets):
    try:
        if (max(prev_usedWhile) < targets[i]/10):
            whileLoop(targets[i])
        else:
            anything(targets[i])
    except:
        whileLoop(targets[i])

f = open("myfile.txt", "w")
print(len(finalArrWhile))
for item in finalArrWhile:
    temp = str(item[0]) + ' ' + str(item[1]) + '\n'
    f.write(temp)
