import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as linalg
from gen_rank_def import genRankDef
from Rank_deficient import *
from wav_to_spectrogram import wav_to_spectrogram

no_log, A = wav_to_spectrogram("test_file.wav")

# print(A[:5, :5])

Qnew, Rnew, P = Parker_Compression(no_log, e=0.1)

print(Qnew.shape)
print(Rnew.shape)

Anew = reconstruct(Qnew, Rnew, P)

# print(Anew[:5, :5])

diff = A - Anew

norm = linalg.norm(diff)

# print(norm)
