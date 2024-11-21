import matplotlib.pyplot as plt
import numpy as np
import math
import random
from numpy.linalg import inv 
from numpy.linalg import norm


def genRankDef(mMin, mMax, nMin, nMax, minVal, maxVal, numDepCols):
    m = random.randrange(mMin,mMax+1)
    n = random.randrange(nMin,nMax+1)
    #print('m =', m, ', n =', n)

    A = np.zeros((m,n))
    for i in range(m):
        for j in range(n - numDepCols):
            A[i,j] = random.randrange(minVal, maxVal)

    linDepCols = np.zeros((m,numDepCols))
    for colNum in range(numDepCols):
        for i in range(m):
            for j in range(n-1):
                linDepCols[i, colNum] += random.randrange(-10,11) * A[i,j]
            e = random.randrange(1, 10)**random.randrange(-14, 0)
            #print(e)
            linDepCols[i,colNum] += e

    for colNum in range(numDepCols):
        for i in range(m):
            A[i,n-1 - colNum] = linDepCols[i, colNum]

    #print("A =", A)

    order = []
    for i in range(n):
        order.append(i)
    #print(order)

    random.shuffle(order)
    #print('Column order:', order)

    reorderA = np.zeros((m,n))
    for i in range(n):
        currCol = order[i]
        for j in range(m):
            reorderA[j,i] = A[j,currCol]

    return reorderA
