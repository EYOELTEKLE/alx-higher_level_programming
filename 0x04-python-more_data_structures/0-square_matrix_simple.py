#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    size = len(matrix[0])
    answer = [[matrix[j][i] ** 2 for i in range(size)] for j in range(size)]
    return answer
