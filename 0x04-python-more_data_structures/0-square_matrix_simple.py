#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared =[]
    for x in matrix:
        matrix_2 = map(lambda i: i**2, x)
        squared.append(list(matrix_2))
    return squared
    
