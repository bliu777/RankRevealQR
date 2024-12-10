import numpy as np
import scipy.linalg as linalg
import numpy as np
import random

# A=np.array(([1,4,1,5,7,8,9],
#            [6,2,8,9,0,1,2],
#            [2,6,2,7,3,8,0],
#            [6,7,9,1,17,8,0],
#            [2,6,2,2,4,6,1],
#            [2,5,1,8,9,4,1]))


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

def ortho(Q,I):
    (_,b)=I.shape
    elist=[I[:,i] for i in range(b)]
    a=0
    for i in range(b):
        qhat=elist[i]-Q@Q[i,:]
        atemp=np.linalg.norm(qhat)
        if atemp >= a:
            a=atemp
            q=np.array(qhat/a)
            index=i
        Qhat=np.vstack((np.transpose(Q),q))
        I1=I[:,:index]
        I2=I[:,index+1:]
        If=np.hstack((I1,I2))
    return np.transpose(Qhat),If

def parkerQexpand(Q,It=0):
    m,n=Q.shape
    Qstar=Q
    if It==0:
        I=np.identity(max(Q.shape))
    else:
        I=It
    for i in range(m-n):
        Qstar,I=ortho(Qstar,I)
    return Qstar

def parkerRexpand(R,Q):
    mhat,nhat=Q.shape
    m,n=R.shape
    R22=np.zeros((n-mhat+1,n))
    Rstar=np.vstack((R,R22))

    for i in range(n-mhat+1,n-1):
        for j in range(i,n-1):
            a=Rstar[i-1,j-1]
            Rstar[i,j] =random.uniform(-a,a)
    return Rstar