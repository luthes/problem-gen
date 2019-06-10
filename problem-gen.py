#!/usr/bin/python3
import random
import sys


class Problem():
    def __init__(self, first_number, second_number, operator):
        self.largest_number = 0
        self.smallest_number = 0

        if first_number > second_number:
            largest_number = first_number
            smallest_number = second_number
        else:
            largest_number = second_number
            smallest_number = first_number

        self.a = largest_number
        self.b = smallest_number
        self.operator = operator


def generate_problem_array():
    problem_list = [[],[],[],[],[],[],[],[],[],[]]
    for j in range (0,10):
        for i in range(0,10):
            first_number = random.randint(0,10)
            second_number = random.randint(0,10)
            problem = Problem(first_number, second_number, "+")
            problem_list[j].append(problem)
    return problem_list


def main():
    with open('problems.txt', 'w+') as f:
        problems = generate_problem_array()
        f.write(f'\n\n\tName:_____________________   Grade:_____________________\n\n')
        f.write('\n\n')
        for row in problems:
            for col in row:
                f.write(f'\t{col.a:>5}')
            f.write('\n')
            for col in row:
                f.write(f'\t{col.operator}{col.b:>4}')
            f.write('\n')
            for col in row:
                f.write('\t______')
            for col in row:
                f.write('\n')
main()

