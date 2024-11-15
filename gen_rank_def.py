import matplotlib.pyplot as plt
import numpy as np
import math
import random
from numpy.linalg import inv 
from numpy.linalg import norm


def genRankDef(mMin, mMax, nMin, nMax, minVal, maxVal):
    m = random.randrange(mMin,mMax+1)
    n = random.randrange(nMin,nMax+1)
    print('m =', m, ', n =', n)

    A = np.zeros((m,n))
    for i in range(m):
        for j in range(n - 1):
            A[i,j] = random.randrange(minVal, maxVal)


    linDepCol = np.zeros(m)
    for i in range(n-1):
        for j in range(m):
            linDepCol[j] += random.randrange(-10,10) * A[j,i]

    for i in range(m):
        A[i,n-1] = linDepCol[i]

    print("A =", A)

    order = []
    for i in range(n):
        order.append(i)
    print(order)

    random.shuffle(order)
    print('Column order:', order)

    reorderA = np.zeros((m,n))
    for i in range(n):
        currCol = order[i]
        for j in range(m):
            reorderA[j,i] = A[j,currCol]

    return reorderA
