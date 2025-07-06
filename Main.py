# testing python file
import copy
import matplotlib.pyplot as plt

matrix = [[i**2] for i in range(5)]
ref = matrix
matrixCopy = copy.deepcopy(matrix)
print(f"matrix {matrix} matrix ref {ref} matrix copy {matrixCopy}")
