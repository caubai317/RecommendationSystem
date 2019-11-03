import numpy as np

def create_matrix_2(dim):
    matrix = np.eye(dim)
    print('Moi nhap {} gia tri cho duong cheo'.format(dim-1))
    for i in range(dim - 1):
        while matrix[i, i+1] < 1/9 or matrix[i, i+1] > 9:
            matrix[i, i+1] = input("matrix[{},{}] = ".format(i, i+1))
    print(matrix)
    return matrix


def sol2(matrix):
    for a in range(matrix.shape[0]-1):
        matrix[a+1, a] = 1/matrix[a, a+1]

    for i in range(matrix.shape[0]-1):
        for j in range(i+2, matrix.shape[0]):
            matrix[i, j]= matrix[i, j-1]* matrix[j-1,j]
            matrix[j, i] = 1/matrix[i, j]
    print(matrix)

    #Khởi tạo ma trận Vuong bat ky


def create_matrix(dim):
    matrix = [[0 for x in range(dim)] for y in range(dim)]
    print('Moi nhap gia tri cho ma tran {}x{}'.format(dim, dim))
    # print(matrix[0,2]-1)
    for i in range(dim):
        for j in range(dim):
            matrix[i][j] = input("matrix[{},{}] = ".format(i, j))
    print(matrix)
    return matrix

create_matrix(4)
