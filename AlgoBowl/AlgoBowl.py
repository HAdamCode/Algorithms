input_file = open('input.txt')

num_targets = int(input_file.readline())

targets = [int(n) for n in input_file.readline().split(" ")]


prev_usedWhile = [1]
counter = 0
finalArrWhile = []
prev_usedRecurse = {1}
finalArrRecurse = []

def anything(cur_num): 
    greatest = 0
    for j in prev_usedRecurse:
        if j <= cur_num and j > greatest:
            greatest = j
    if cur_num - greatest in prev_usedRecurse:
        finalArrRecurse.append([greatest, cur_num - greatest])
        prev_usedRecurse.add(cur_num)
        return
    else:
        anything(cur_num-greatest)
        finalArrRecurse.append([greatest, cur_num - greatest])
        prev_usedRecurse.add(cur_num)

def whileLoop(cur_num):
    while(True):
        if (cur_num in prev_usedWhile):
            return
        for item in reversed(prev_usedWhile):
            if (item + max(prev_usedWhile) <= cur_num):
                finalArrWhile.append([item, max(prev_usedWhile)])
                prev_usedWhile.append(item + max(prev_usedWhile))
                break

        

for i in range(num_targets):
    cur_num = targets[i]
    anything(cur_num)
    whileLoop(cur_num)

if (len(finalArrWhile) < len(finalArrRecurse)):
    print(len(finalArrWhile))
    for item in finalArrWhile:
        print(item[0], item[1])
else:
    print(len(finalArrRecurse))
    for item in finalArrRecurse:
        print(item[0], item[1])