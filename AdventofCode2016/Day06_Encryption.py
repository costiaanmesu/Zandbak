# https://github.com/NLHEALTHCARE/PERSONAL/tree/master/Costiaan/Zandbak/AdventofCode2016
# http://adventofcode.com/2016/day/6

# OPGAVE DATA #
import os
data = []
with open(os.path.basename(__file__).replace('.py', '.txt'), 'r') as f:
    for line in list(f):
        data.append(line.strip())

# OPLOSSING #
messages = data
modified_solution = ''
real_solution = ''

for i in range(len(messages[0])):
    decode_dict = {chr(key): 0 for key in range(0, 255+1)}
    for message in messages:
        decode_dict[message[i]] += 1
    modified_solution += max(decode_dict, key=decode_dict.get)

    for x in list(decode_dict.keys()):
        if decode_dict[x] == 0:
            del decode_dict[x]
    real_solution += min(decode_dict, key=decode_dict.get)

print('Modified solution: '+modified_solution)
print('Real solution: '+real_solution)



