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


"""
Thực tế thì số user lớn hơn item rất nhiều 
-> Nên dựa vào item-item kết quả tốt hơn, ít chỉnh sửa hơn 
"""
#Item-item Collaborative Filtering
class CF(object):
    def __init__(self, array, i, u, k, uuCF = 1):
        self.uuCF = uuCF
        self.array = array if uuCF else array[:, [1, 0, 2]]
        self.k = k
        self.i = i
        self.u = u 
    
    #Tiền xử lý
    def pre_processing(self):
        #Trung bình cộng rating của mỗi user (không chứa NaN)
        self.mean_column = np.nanmean(self.array, axis=0)
        #Trừ rating mỗi user cho TBC
        self.array = np.round(self.array - self.mean_column, 2)
        #Chuyển tất cả NaN về giá trị 0
        self.array[np.isnan(self.array)] = 0 

    #Hàm tính độ tương tự giữa các user
    def cosine_similarity(self):
        self.array_cosine = np.eye(self.array.shape[1])
        #cosine_similarity(a,b) = cos(a,b) = (a.T * b)/(norm(a)*norm(b))
        #Tính cosine của 2 vector a và b => Độ tương tự (similar) của a và b
        for i in range(self.array.shape[1]):
            for j in range(i+1, self.array.shape[1]):
                u = self.array[:,i]
                w = self.array[:,j]
                self.array_cosine[i,j] = u.T.dot(w)/(norm(u)*norm(w))
                self.array_cosine[j,i] = self.array_cosine[i,j]
        self.similar_table = np.round(self.array_cosine,2)
        
    #Hàm dự đoán cho đánh giá item i của user u dựa trên k user gần giống nhất
    def predict_rating(self): #i, u, k, norm_array, similar_table):
        #Tìm vị trí tất cả user đã rate item i
        user_rated_col = np.where(self.array[self.i,:] != 0)[0].astype(np.int32)
        #Sim giữa user u với các user vừa tìm được
        sim_user_rated = self.similar_table[self.u, user_rated_col]
        #Rating của các user vừa tìm được cho item i
        arr_user_rated = self.array[self.i, user_rated_col]
        #Tìm vị trí k user giống nhất với user u
        k_similarest_user = np.argsort(sim_user_rated)[-self.k:]
        
        a = arr_user_rated[k_similarest_user]
        b = sim_user_rated[k_similarest_user]
        self.predict = np.sum(a * b) / np.sum(abs(b))
        print (np.round(self.predict + self.mean_column[self.u], 2))

    def refresh(self):
        self.pre_processing()
        self.cosine_similarity()
        self.predict_rating()

predict = CF(a, i=1, u=4, k=2)
predict.refresh()

def predict_all(array):
    for i in range(array.shape[0]):
        arr = np.where(np.isnan(array[i,:]))[0]
        if arr.size > 0:
            for j in arr:
                print(i, j)
                predict = CF(a, i=i, u=j, k=2)
                predict.refresh()
    
predict_all(a)