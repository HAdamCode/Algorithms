input_file = open('input.txt')

num_targets = int(input_file.readline())

targets = [int(n) for n in input_file.readline().split(" ")]


prev_used = {1}
counter = 0

def anything(cur_num): 
    greatest = 0
    for j in prev_used:
        if j <= cur_num and j > greatest:
            greatest = j
    if cur_num - greatest in prev_used:
        print(greatest, cur_num - greatest)
        prev_used.add(cur_num)
        return
    else:
        anything(cur_num-greatest)
        print(greatest, cur_num - greatest)
        prev_used.add(cur_num)

for i in range(num_targets):
    cur_num = targets[i]
    anything(cur_num)