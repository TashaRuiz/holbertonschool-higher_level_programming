#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for num in matrix:
        for idx in range(len(num)):
            if idx == len(num) - 1:
                print("{:d}".format(num[idx]), end="")
            else:
                print("{:d}".format(num[idx]), end=" ")
        print()
