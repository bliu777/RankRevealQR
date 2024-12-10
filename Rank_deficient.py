import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as linalg
from gen_rank_def import genRankDef 
import math

'''A=np.array(([1,4,1,5,7,8,9],
           [6,2,8,9,0,1,2],
           [2,6,4,7,3,8,0],
           [6,7,9,1,5,8,0],
           [2,6,2,2,4,6,1],
           [2,5,1,8,9,1,1]))'''



def Parker_Compression(A,e):
    Q,R,P=linalg.qr(A,pivoting=True)
    n=min(R.shape)
    i=0
    while i < n and abs(R[i,i]) > e:
        i+=1
    Rnew=R[0:i,:]
    Qnew=Q[:,0:i]
    return Qnew,Rnew,P

def reconstruct(Q,R,P):
    Atemp= Q @ R
    Itemp=np.identity(len(P))
    Pivot=np.zeros((len(P),len(P)))
    for i in range(len(P)):
        Pivot[:,i]=Itemp[P[i]]
    return Atemp @ linalg.inv(Pivot)


def rrqr_iteration(numSteps, numIts):

    e = np.zeros(numSteps)
    for i in range(numSteps):
        #print(-numSteps + i)
        e[i] = 10**(-numSteps + i + 5)
        #print(1**(-numSteps + i))
    #print(e)

    norms = np.zeros(numSteps)
    for it in range(numIts):
        for i in range(numSteps):
            A = genRankDef(50, 50, 50, 50, -20, 20, 45)
            Q,R,P=Parker_Compression(A,e[i])
            Anew=(reconstruct(Q,R,P))
            norms[i] += linalg.norm(Anew-A, 2)

    for i in range(numSteps):
        norms[i] = norms[i]/numIts

    plt.figure()
    plt.loglog(e,norms, "b.-")
    plt.xlabel("e values")
    plt.ylabel("norm values")
    plt.show()
    return (norms, e)

# rrqr_iteration(10, 10, 10)

