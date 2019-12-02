import numpy as np

PRICE = np.array([[1,3,2],[1/3,1,1/5],[1/2,5,1]])
DISTANCE = np.array([[1,6,1/3],[1/6,1,1/9],[3,9,1]])
LABOR = np.array([[1,1/3,1],[3,1,7],[1,1/7,1]])
WAGE = np.array([[1,1/3,1/2],[3,1,4],[2,1/4,1]])
TC = np.array([[1,1/5,3,4],[5,1,9,7],[1/3,1/9,1,2],[1/4,1/7,1/2,1]])
LIST_TC = ['PRICE','DISTANCE','LABOR','WAGE']
LIST_JOB = ['A','B','C']

def caculater_Vector(matrix,e=0.02):
    mat1=np.dot(matrix,matrix)
    sum_mat1=np.sum(mat1,axis=1)
    vecto=np.around(np.divide(sum_mat1,np.sum(sum_mat1)),decimals=4)
    
    next_matrix = mat1
    while(True):
        matrix_temp = np.dot(next_matrix,next_matrix)
        sum_matrixTemp=np.sum(matrix_temp,axis=1)
        vecto_temp=np.around(np.divide(sum_matrixTemp,np.sum(sum_matrixTemp)),decimals=4)
        next_matrix=matrix_temp
        loss_vector=np.subtract(vecto,vecto_temp)
        print("loss_vector len",len(loss_vector))
        if np.sum(loss_vector) / len(loss_vector) < e:
            break
    return vecto_temp

def caculater_CR(matrix, vector):
    RI = {'1':0,'2':0,'3':0.52,'4':0.89,'5':1.11,'6':1.25,'7':1.35,'8':1.4,'9':1.45,'10':1.49,'11':1.52,'12':1.54,'13':1.56,'14':1.58,'15':1.59}
    vector_tongtrongso=np.dot(matrix,vector)
    vector_nhatquan=np.divide(vector_tongtrongso,vector)
    lambda_max = np.sum(vector_nhatquan)/len(vector_nhatquan)
    CI=(lambda_max- matrix.shape[0] ) / (matrix.shape[0] - 1)
    CR = CI / RI[str(matrix.shape[0])]
    return CR
   
def text_valueCR(matrixTC):
    vecto = caculater_Vector(matrixTC)
    CR = caculater_CR(matrixTC,vecto)
    if CR > 0.1:
        print('Nhập lại ',CR,vecto)
   
class Tree:
    def __init__(self,name,value,children):
        self.name = name
        self.value = value
        self.children = children

    def addNode(self,node_name, node_value):
        for i,n in enumerate(node_name):
            self.children.append(Tree(n, node_value[i], []))

def caculater_eachNode(node,result_cacul):
    r = []
    if len(node.children) == 0:
        return node.value 
    for child in node.children:
        r.append(caculater_eachNode(child,result_cacul) * node.value)
    result_cacul.append(r)
    return r
    
def main(): 
    result_cacul = []
    text_valueCR(PRICE)
    text_valueCR(DISTANCE)
    text_valueCR(LABOR)
    text_valueCR(WAGE)
    root_tree = Tree('JOB',1,[])
    root_tree.addNode(LIST_TC,caculater_Vector(TC))
    TC_CON = [caculater_Vector(PRICE),caculater_Vector(DISTANCE),caculater_Vector(LABOR),caculater_Vector(WAGE)]
    for i,child in enumerate(root_tree.children):
        child.addNode(LIST_JOB,TC_CON[i])
    caculater_eachNode(root_tree,result_cacul)
    result_cacul = result_cacul[:-1]
    result_cacul = np.array(result_cacul).T
    print(result_cacul)
    job = LIST_JOB[result_cacul.sum(axis=1).argmax()]
    print('chosse job:',job)
    for i,r in enumerate(result_cacul):
        print(LIST_JOB[i],np.sum(r))

if __name__ == "__main__":
    main()
