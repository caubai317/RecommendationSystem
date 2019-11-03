import numpy as np 
from numpy.linalg import norm

nan = float('nan')
a = np.array([
    [5, 5, 2, 0, 1, nan, nan],
    [4, nan, nan, 0, nan, 2, nan],
    [nan, 4, 1, nan, nan, 1, 1],
    [2, 2, 3, 4, 4, nan, 4],  
    [2, 0, 4, nan, nan, nan, 5] 
])

b = np.array([
    [1, 5, 4, nan],
    [4, 1, 1, 3],
    [5, nan, 2, 4],
    [nan, 5, 5, nan],
    [3, 2, nan, 4]
])

#Tiền xử lý
def pre_processing(array):
    #Trung bình cộng rating của mỗi user
    mean_column = np.nanmean(array, axis=0)
    #Trừ rating mỗi user cho TBC
    array2 = np.round(array - mean_column, 2)
    #Chuyển tất cả NaN về giá trị 0
    array2[np.isnan(array2)] = 0
    return array2

#Hàm tính độ tương tự giữa các user
def cosine_similarity(array):
    array_cosine = np.eye(array.shape[1])
    for i in range(array.shape[1]):
        for j in range(i+1, array.shape[1]):
            u = array[:,i]
            w = array[:,j]
            array_cosine[i,j] = u.T.dot(w)/(norm(u)*norm(w))
            array_cosine[j,i] = array_cosine[i,j]
    return array_cosine

def predict_rating(i, u, k, norm_array, similar_table):
    #Tìm vị trí tất cả user đã rate item i
    user_rated_col = np.where(norm_array[i,:] != 0)[0].astype(np.int32)
    #Sim giữa user u với các user vừa tìm được
    sim_user_rated = similar_table[u, user_rated_col]
    #Rating của các user vừa tìm được cho item i
    arr_user_rated = norm_array[i, user_rated_col]
    #Tìm vị trí k user giống nhất với user u
    k_similarest_user = np.argsort(sim_user_rated)[-k:]
    
    a = arr_user_rated[k_similarest_user]
    b = sim_user_rated[k_similarest_user]
    predict = np.sum(a * b) / np.sum(abs(b))
    print (predict)

norm_array = pre_processing(a)
similar_table = np.round(cosine_similarity(norm_array),2)
predict_rating(4,5,2,norm_array, similar_table)

print(pre_processing(b))
print(cosine_similarity(pre_processing(b)))