#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    '''iterate through each row'''
    for i in range(len(matrix)):
        '''iteratr through each column'''
        for j in range(len(matrix[i])):
            '''Print each integer'''
            print("{:d}".format(matrix[i][j]), end="")
            '''check if it is the last elemnet in the row'''
            if j != (len(matrix[i]) - 1):
                '''Print a space between elements'''
                print(" ", end="")

        '''Move to the next line after each row'''
        print()
