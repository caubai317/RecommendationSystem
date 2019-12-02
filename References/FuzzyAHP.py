import numpy as np

TC = np.array([[1,5,4,7],[1/5,1,1/2,3],[1/4,2,1,3],[1/7,1/3,1/3,1]])
LIST_TC = ['PRICE','DISTANCE','LABOR','WAGE']
DECISION_MAKER1=np.array([[5,9,7,5],[7,9,5,7],[9,5,3,5],[5,7,7,5]])
DECISION_MAKER2=np.array([[7,9,5,7],[3,5,7,9],[5,7,7,9],[9,7,5,3]])
DECISION_MAKER3=np.array([[7,5,3,5],[5,9,7,3],[9,7,5,9],[5,7,9,5]])

def caculater_fuzzyGeometrix(matrix):
    a=[];
    for index_row in np.arange(0,matrix.shape[0]):
        temp = np.ones(matrix.shape[0]-1)
        for index_column in np.arange(0,matrix.shape[1]):
            temp = (temp * np.asarray(fill_evaluateNumber(matrix[index_row][index_column])))
            if index_column == matrix.shape[1] -1:
                a.append(np.around(temp**(1/4),decimals=2))           
    return a

def fill_evaluateNumber(num):
    if num >= 1:
       if num == 1:
           return [1,1,1]
       elif num == 9:
           return [9,9,9]
       else:
           return [num-1,num,num+1]
    else:
       num=1/num;
       if num == 9:
           return [1/9,1/9,1/9]
       else:
           return [1/(num+1),1/num,1/(num-1)] 
def calculate_meanValue(list_arr):
    # print(list_arr)
    item= np.zeros(3)
    for i in range(len(list_arr)):
        item = item + np.asarray(list_arr[i])
    item=np.flip(item,0)**(-1)
    
    return item 
def calculate_fuzzyWeight(list_arr,r):
    fuzzy_weight=[]
    for i in range(len(list_arr)):
        item =np.asarray(list_arr[i]) * r
        fuzzy_weight.append(np.round(item,decimals=3))
    return fuzzy_weight
def get_fuzzyNumber(num):
    if num == 1 :
        return [1,1,3]
    elif num == 9 :
        return [7,9,9]
    else :
        return [num-2,num,num+2]
def combineDecisionMatrix(matrix1,matrix2,matrix3):
    dictionary_result={}
    matrix_result =np.random.randint(0, 2, (matrix1.shape[0], matrix1.shape[1]))  
    idx=0
    for index_row in np.arange(0,matrix_result.shape[0]):    
        for index_column in np.arange(0,matrix_result.shape[1]):           
            matrix_result[index_row][index_column]= str(idx)
            dictionary_result[str(idx)]=caculate_valueCombine(get_fuzzyNumber(matrix1[index_row][index_column]),get_fuzzyNumber(matrix2[index_row][index_column]),get_fuzzyNumber(matrix3[index_row][index_column]))
            idx +=1
    return matrix_result,dictionary_result

def get_valueNormaliseMatrix(array,dictionary_main,dictionary_new):
    result= np.zeros(3)
    for i in range(len(array)):
         result = result + np.asarray(dictionary_main[str(array[i])])**2
    result=result**(1/2)
    for i in range(len(array)):
         dictionary_new[str(array[i])] = np.asarray(dictionary_main[str(array[i])])/result

def caculate_normaliseMatrix(matrix,dictionary):
    newDictionary=dictionary.copy()
    print(newDictionary)
    for index_column in np.arange(0,matrix.shape[1]):
        get_valueNormaliseMatrix(matrix[:,index_column],dictionary,newDictionary)
    print(newDictionary)
    return newDictionary
    
def caculate_valueCombine(arr1,arr2,arr3):
    result=[]
    value1 = min(arr1[0],arr2[0],arr3[0])
    value2 = (arr1[0]+arr2[1]+arr3[2])/3
    value3 =max(arr1[0],arr2[0],arr3[0])
    result.append(value1)
    result.append(value2)
    result.append(value3)
    return result
def combine_fuzzyWeightandNormaliseMatrix(list_array,matrix,dictionary):
    dictionary_sum=dictionary.copy()
    for index_row in np.arange(0,matrix.shape[0]):
        for index_column in np.arange(0,matrix.shape[1]):
            dictionary_sum[str(matrix[index_row][index_column])]=np.asarray(list_array[index_column])*np.asarray(dictionary[str(matrix[index_row][index_column])])
    # print(dictionary_sum)
    return dictionary_sum

def caculate_distanceAandcostB(array,a,b):
    left = array[0] +a*(array[1]-array[0]) 
    right =array[2] - a*(array[2]-array[1]) 
    result=b*left +(1-b)*right
    return result

def caculate_fuzzyMatrixAfter(matrix,dictionary):  
    matrix_re=np.random.rand(matrix.shape[0], matrix.shape[1]) 
    for index_row in np.arange(0,matrix.shape[0]):
        for index_column in np.arange(0,matrix.shape[1]):
            matrix_re[index_row][index_column]=round(caculate_distanceAandcostB(dictionary[str(matrix[index_row][index_column])],0.5,0.4),4)  
    return np.round(matrix_re,decimals=4)
def caculate_TOPSIS(matrix):
    topic=[]
    for index_column in np.arange(0,matrix.shape[1]):
        topic.append(get_valueVectorTopis(matrix[:,index_column]))
    print(topic)

def get_valueVectorTopis(array):
    maxValue=np.max(array)
    minValue=np.min(array)
    sum_val1=np.sum(((array-maxValue)**2)**(1/2))
    sum_val2=np.sum(((array-minValue)**2)**(1/2))
    PA=sum_val2/(sum_val1+sum_val2)
    # print(PA)
    return PA
def main():
  b=caculater_fuzzyGeometrix(TC)
  c=calculate_meanValue(b)
  d=calculate_fuzzyWeight(b,c)
  _matrix,_dictionary = combineDecisionMatrix(DECISION_MAKER1,DECISION_MAKER2,DECISION_MAKER3)
  nomalise_dic=caculate_normaliseMatrix(_matrix,_dictionary)
  sum_dic=combine_fuzzyWeightandNormaliseMatrix(d,_matrix,nomalise_dic)
  ketqua = caculate_fuzzyMatrixAfter(_matrix,sum_dic)
  print(ketqua)
  caculate_TOPSIS(ketqua)
if __name__ == "__main__":
    main()

