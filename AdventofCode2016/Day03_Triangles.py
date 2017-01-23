# https://github.com/NLHEALTHCARE/PERSONAL/tree/master/Costiaan/Zandbak/AdventofCode2016
# http://adventofcode.com/2016/day/3

# OPGAVE DATA #
import os
data = []

with open(os.path.basename(__file__).replace('.py', '.txt'), 'r') as f:
    for line in list(f):
        data.append(line.strip())

# OPLOSSING #
shapes = data


def possible(sides):
    longest = max(sides)
    sides.remove(longest)
    return int(sides[0]+sides[1] > longest)


horizontal = 0
for sides in shapes:
    sides = [int(i) for i in sides.split()]
    horizontal += possible(sides)


sides = []
vertical = 0
for pos in range(len(shapes[0].split())):
    for rows in shapes:
        columns = [int(i) for i in rows.split()]
        sides.append(columns[pos])
        if len(sides) == 3:
            vertical += possible(sides)
            sides = []

print('horizontaal = %s' %horizontal)
print('verticaal = %s' %vertical)