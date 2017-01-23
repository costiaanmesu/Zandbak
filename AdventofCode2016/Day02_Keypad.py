# https://github.com/NLHEALTHCARE/PERSONAL/tree/master/Costiaan/Zandbak/AdventofCode2016
# http://adventofcode.com/2016/day/2

# OPGAVE DATA #
import os
data = []

with open(os.path.basename(__file__).replace('.py', '.txt'), 'r') as f:
    for line in list(f):
        data.append(line.strip())

# OPLOSSING #
instructions = data
keypad1 = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
keypad2 = [['0', '0', '1', '0', '0'], ['0', '2', '3', '4', '0'], ['5', '6', '7', '8', '9'], ['0', 'A', 'B', 'C', '0'], ['0', '0', 'D', '0', '0']]

code1 = ''
code2 = ''


def move(keypad, x, y, moves):
    for move in moves.lower():
        if move == 'l' and x != 0 and digit(keypad, x-1, y) != '0':
            x += -1
        if move == 'r' and x != len(keypad[0][:-1]) and digit(keypad, x+1, y) != '0':
            x += 1
        if move == 'u' and y != 0 and digit(keypad, x, y-1) != '0':
            y += -1
        if move == 'd' and y != len(keypad[:-1]) and digit(keypad, x, y+1) != '0':
            y += 1
    return x, y


def digit(keypad, x, y):
    return keypad[y][x]

x, y = 1, 1
for instruction in instructions:
    x, y = move(keypad1, x, y, instruction)
    code1 += digit(keypad1, x, y)

x, y = 0, 2
for instruction in instructions:
    x, y = move(keypad2, x, y, instruction)
    code2 += digit(keypad2, x, y)


print('code 1 = %s' %code1)
print('code 2 = %s' %code2)


