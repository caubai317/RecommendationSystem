import numpy as np
import random
sw = 3
sh = 4
k = int((sw + sh)/2)
Dtrain = np.random.randint(5, size=(sw, sh))
beta = 0.2
# lr = 0.0008


def MatrixFactorization(D,k,beta):
    W = np.random.rand( sw, k)
    H = np.random.rand( k, sh)

    for s in range(4000000):
        sum_eui = 0
        for u in range(sw):
            for i in range(sh):
                r = D[u][i]
                if r <=0: continue
                r3 = 0
                for j in range(k):
                    r3 += W[u][j] * H[j][i]
                eui =  r - r3
                for j in range(k):
                    W[u][j] += beta * (eui * H[j][i])
                    H[j][i] += beta * (eui * W[u][j])
                sum_eui+=abs(eui)
        sum_eui/=(sw*sh)
        if abs(sum_eui) < 0.01: return W,H,sum_eui,'good'
    return W,H,sum_eui,'not good'

W,H,eui,result = MatrixFactorization(Dtrain,k,beta)

print('Dtrain: \n',Dtrain)
print('W: \n',W)
print('H: \n',H)
print('W*H: \n',np.dot(W,H))
print('eui: ',eui)
print('result: ',result)