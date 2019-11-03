import numpy as np 

#A = np.array([[1,0.5,3],[2,1,4],[1/3, 1/4, 1]])
A=np.array([
    [1, 1/5, 3, 4],
    [5, 1, 9, 7],
    [1/3, 1/9, 1, 2],
    [1/4, 1/7, 1/2, 1]
])
B=np.array([
    [1, 3, 2],
    [1/3, 1, 1/5],
    [1/2, 5, 1]
])

#Khởi tạo ma trận vuong bat ky
def create_matrix(dim):
    matrix = [[0 for x in range(dim)] for y in range(dim)]
    print('Moi nhap gia tri cho ma tran {}x{}'.format(dim, dim))
    # print(matrix[0,2]-1)
    for i in range(dim):
        for j in range(dim):
            matrix[i][j] = input("matrix[{},{}] = ".format(i, j))
    print(matrix)
    return matrix

#Khởi tạo ma trận phù hợp với cải tiến 1
def create_matrix_1(dim):
    matrix = np.eye(dim)
    print('Moi nhap {} gia tri cho hang 0'.format(dim-1))
    for i in range (1,dim):
        while matrix[0,i] < 1/9 or matrix[0,i] > 9:
            matrix[0,i]=input("matrix[0,{}] = ".format(i))
    print(matrix)
    return matrix

#Khởi tạo ma trận phù hợp với cải tiến 2
def create_matrix_2(dim):
    matrix = np.eye(dim)
    print('Moi nhap {} gia tri cho duong cheo'.format(dim-1))
    for i in range (dim - 1):
        while matrix[i,i+1] < 1/9 or matrix[i,i+1] > 9:
            matrix[i,i+1]=input("matrix[{},{}] = ".format(i, i+1))
    print(matrix)
    return matrix

# a = np.eye(6)
# a[0,1] = 2
# a[0,2] = 9
# a[0,3] = 8
# a[0,4] =12
# a[0,5] = 6

# b=np.eye(6)
# b[0,1]=2
# b[1,2]=4.5
# b[2,3]=8/9
# b[3,4]=1.5
# b[4,5]=0.5

def sol1(matrix):
    for  i in range(1,matrix.shape[0]-1):
        matrix[i,0]=1/matrix[0,i]

    for  i in range(0,matrix.shape[0]-1):
        for j in range (i+1, matrix.shape[0]):
            matrix[i,j]=matrix[i,0]*matrix[0,j]
            matrix[j,i]=1/matrix[i,j]
    print(matrix)
    return matrix

def sol2(matrix):
    for a in range(matrix.shape[0]-1):
        matrix[a+1, a] = 1/matrix[a, a+1]

    for i in range(matrix.shape[0]-1):
        for j in range(i+2, matrix.shape[0]):
            matrix[i, j] = matrix[i, j-1] * matrix[j-1, j]
            matrix[j, i] = 1/matrix[i, j]
    print(matrix)
    return matrix

a=create_matrix_1
sol1(a)

# sol2(b)

def chuan_hoa_matrix(matrix):
    matrix2 = matrix / np.sum(matrix, axis=0)
    matrix3 =np.sum(matrix2,axis=1) / np.sum(matrix2)
    return matrix3

print(chuan_hoa_matrix(A))
print(chuan_hoa_matrix(B))

def ti_so_nhat_quan(matrix):
    mat_trongso = chuan_hoa_matrix(matrix)
    vecto = np.dot(matrix, mat_trongso) / mat_trongso
    lamda_max = np.mean(vecto)
    print(lamda_max)
    n  = vecto.shape[0]
    CI = (lamda_max-n)/(n-1)
    CR = CI/0.52

    print('Ket qua',CR)

ti_so_nhat_quan(A)
    

# def vecto_rieng(matrix):
#     count = 0
#     target = 0.1
#     a=0
#     b=1
#     while True:  
#         #Binh phuong ma tran matrix
#         square = np.dot(matrix,matrix)

#         #Tong tat ca phan tu trong ma tran square
#         sum_all = np.sum(square)

#         #Tinh trong so
#         average = np.sum(square, axis=1)/sum_all

#         #Dam bao 2 lan lap
#         if count==0:
#             a = average
#             matrix = square
#             count+=1
#             continue

#         b=np.max(np.abs(a-average))

#         #So sanh do chenh lech voi muc tieu
#         if b<target:
#             print(b, count)
#             print ('Vecto rieng can tim: ', average)
#             return average
#         a = average
#         matrix = square

# vecto_rieng(A) 