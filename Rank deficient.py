import numpy as np
import scipy.linalg as linalg

A=np.array(([1,4,1,5,7,8,9],
           [6,2,8,9,0,1,2],
           [2,6,4,7,3,8,0],
           [6,7,9,1,5,8,0],
           [2,6,2,2,4,6,1],
           [2,5,1,8,9,1,1]))


def Parker_Compression(A,e):
    Q,R,P=linalg.qr(A,pivoting=True)
    n=min(R.shape)
    i=0
    while abs(R[i,i]) > e and i <= n:
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


Q,R,P=Parker_Compression(A,2)
Anew=(reconstruct(Q,R,P))
print(Anew-A)