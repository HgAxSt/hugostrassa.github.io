import numpy as np
"""RANGE SINTAX: RANGE(START, STOP, STEP)

list(range(0, 5))
 output: [0, 1, 2, 3, 4]

list(range(0,8,2))
 output: [0, 2, 4, 6]
#####################################################################################################################################
lista_1 = [1,2,3,4,5]
lista_2 = [6,7,8,9,10]
new_list = []

for i in range(0, len(lista_1)):
    x = lista_1[i] * lista_2[i]
    new_list.append(x)
print(new_list)
 outuput: [6, 14, 24, 36, 50]
#########################################################################################################################################

lista_1 = np.array([1,2,3,4,5])
lista_2 = np.array([6,7,8,9,10])
new_list = lista_1 * lista_2
print(new_list)
outuput: [6, 14, 24, 36, 50]
matriz_zeros = np.zeros((3,5), dtype = "int") nós podemos fazer também "np.ones" para um´s.
print(matriz_zeros)
output: 
 [
[0 0 0 0 0]
[0 0 0 0 0]
[0 0 0 0 0]
]
------------------------------------------------------------------------------------------------------------------------------------------
eye_element = np.eye(3,3)
print(" ", eye_element) 
OUTPUT:
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
------------------------------------------------------------------------------------------------------------------------------------------

matrix = np.random.randint(10, 50, (5,4))
print("", matrix)
OUTPUT:
 [[22 16 37 38]
 [29 46 38 40]
 [32 22 24 31]
 [29 28 30 16]
 [47 18 29 24]]
 
matrix_dimension = matrix.ndim
print("", matrix_dimension)
OUTPUT:
     2
 
matrix_shape = matrix.shape
print("", matrix_shape)
OUTPUT:
    (5, 4)
"""
 