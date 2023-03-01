input_file = open('input.txt')

num_targets = int(input_file.readline())

targets = [int(n) for n in input_file.readline().split(" ")]


prev_used = [1]
counter = 0
finalArr = []

# def anything(cur_num): 
#     greatest = 0
#     for j in prev_used:
#         if j <= cur_num and j > greatest:
#             greatest = j
#     if cur_num - greatest in prev_used:
#         finalArr.append([greatest, cur_num - greatest])
#         prev_used.add(cur_num)
#         return
#     else:
#         anything(cur_num-greatest)
#         finalArr.append([greatest, cur_num - greatest])
#         prev_used.add(cur_num)

def whileLoop(cur_num):
    while(True):
        if (cur_num in prev_used):
            return
        for item in reversed(prev_used):
            if (item + max(prev_used) <= cur_num):
                finalArr.append([item, max(prev_used)])
                prev_used.append(item + max(prev_used))
                break

        

for i in range(num_targets):
    cur_num = targets[i]
    whileLoop(cur_num)
print(len(finalArr))
for item in finalArr:
    print(item[0], item[1])