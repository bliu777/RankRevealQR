from gen_rank_def import genRankDef
from scipy.linalg import qr

def driver():
    mMin = 3
    mMax = 8

    nMin = 9
    nMax = 16

    minVal = -20
    maxVal = 20

    A = genRankDef(mMin, mMax, nMin, nMax, minVal, maxVal)

    print('A =', A)

    #print(qr(A, pivoting=True))

    Q,R,P = qr(A, pivoting=True)

    #print("TEST OUTPUT :)")

    print('P =', P)
    print('Q =', Q)
    print('R =', R)


#def gen_pivot():

driver()