# https://github.com/NLHEALTHCARE/PERSONAL/tree/master/Costiaan/Zandbak/AdventofCode2016
# http://adventofcode.com/2016/day/8

# OPGAVE DATA #

import os
data = []

with open(os.path.basename(__file__).replace('.py', '.txt'), 'r') as f:
    for line in list(f):
        data.append(line.strip())

# OPLOSSING #
instructions = data


class Display(object):
    def __init__(self):
        self.matrix = []

    def initiate(self, x, y):
        self.matrix = self.generate(x, y)

    @staticmethod
    def generate(x, y):
        new_matrix = []
        for i in range(y):
            row = []
            for j in range(x):
                row.extend(['.'])
            new_matrix.append(row)
        return new_matrix

    def show(self):
        count = 0
        for row in self.matrix:
            for column in row:
                print(column, end='')
                if column == '#':
                    count += 1
            print('\n', end='')
        print(count)

    def rect(self, x, y):
        for row in range(y):
            for column in range(x):
                self.matrix[row][column] = '#'

    def rotate_row(self, row, shift):
        new_row = ['.']*len(self.matrix[row])
        for pos in range(len(self.matrix[row])):
            new_pos = (pos+shift) % 50
            new_row[new_pos] = self.matrix[row][pos]
        self.matrix[row] = new_row

    def rotate_col(self, col, shift):
        new_matrix = self.generate(50, 6)
        for row in range(len(self.matrix)):
            new_pos = (row + shift) % 6
            new_matrix[new_pos][col] = self.matrix[row][col]
        for row in range(len(self.matrix)):
            self.matrix[row][col] = new_matrix[row][col]

    def process(self, instructions):
        for instruction in instructions:
            if instruction[0:4] == 'rect':
                x = int(instruction[5:].split('x')[0])
                y = int(instruction[5:].split('x')[1])
                display.rect(x, y)
            if instruction[0:13] == 'rotate row y=':
                row = int(instruction[13:].split(' by ')[0])
                shift = int(instruction[13:].split(' by ')[1])
                display.rotate_row(row, shift)
            if instruction[0:16] == 'rotate column x=':
                col = int(instruction[16:].split(' by ')[0])
                shift = int(instruction[16:].split(' by ')[1])
                display.rotate_col(col, shift)

display = Display()
display.initiate(50, 6)
display.process(instructions)
display.show()







