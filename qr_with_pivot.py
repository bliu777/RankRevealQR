from gen_rank_def import genRankDef
from scipy.linalg import qr

def driver():
    mMin = 50
    mMax = 50

    nMin = 50
    nMax = 50

    minVal = -20
    maxVal = 20

    numDepCols = 20

    A = genRankDef(mMin, mMax, nMin, nMax, minVal, maxVal, numDepCols)

    print('A =', A)

    #print(qr(A, pivoting=True))

    Q,R,P = qr(A, pivoting=True)

    #print("TEST OUTPUT :)")

    print('P =', P)
    print('Q =', Q)
    print('R =', R)

driver()