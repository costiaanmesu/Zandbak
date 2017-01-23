# https://github.com/NLHEALTHCARE/PERSONAL/tree/master/Costiaan/Zandbak/AdventofCode2016
# http://adventofcode.com/2016/day/1
import os
with open(os.path.basename(__file__).replace('.py', '.txt'), 'r') as f:
        route = f.readline().split(', ')

x, y = 0, 0
direction = 0
visited = []
hq = None

def change_direction(step, direction):
    if step[0] == 'R':
        if direction < 3:
            direction += 1
        else:
            direction = 0
    if step[0] == 'L':
        if direction > 0:
            direction += -1
        else:
            direction = 3
    return direction


def move(x, y, direction, step, visited):
    if direction == 0:
        for add in range(y, y+int(step[1:])):
            visited.append([x, add])
        y += int(step[1:])
    if direction == 2:
        for add in reversed(range(y, y-int(step[1:]))):
            visited.append([x, add])
        y -= int(step[1:])
    if direction == 1:
        for add in range(x, x+int(step[1:])):
            visited.append([add, y])
        x += int(step[1:])
    if direction == 3:
        for add in reversed(range(x, x-int(step[1:]))):
            visited.append([add, y])
        x -= int(step[1:])
    return x, y, visited


def twice(visited):
    for visit in visited:
        if visited.count(visit) > 1:
            twice = visit
            return twice
            break


for step in route:
    direction = change_direction(step, direction)
    x, y, visited = move(x, y, direction, step, visited)
    if not hq:
        hq = twice(visited)
        if hq:
            print('HQ postion (x, y) = %s'%hq)
            print('HQ distance in blocks = %s' %(abs(hq[0])+abs(hq[1])))
print('Final destination in blocks = %s' %(abs(x)+abs(y)))

