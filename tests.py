import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as linalg
from gen_rank_def import genRankDef
from Rank_deficient import *
from wav_to_spectrogram import *


spect, phase, samples = wav_to_spectrogram("test_file.wav")

Q, R, P = Parker_Compression(spect, 1000)

# Anew = reconstruct(Q, R, P)


ranks = []
xvals = [i for i in range(1, 2000, 20)]

for eps in range(1, 2000, 20):
    Qnew, Rnew, P = Parker_Compression(spect, e=eps)
    rank = Qnew.shape[1]
    ranks.append(rank)

plt.semilogx(xvals, ranks)
plt.title("Rank of Q for different ε")
plt.xlabel("ε")
plt.ylabel("Rank of Q")
plt.show()

# print(f"Reconstruction shape: {Anew.shape}")

# diff = spect - Anew
# norm = linalg.norm(diff)
# print(f"Norm of diff: {norm}")

# spectrogram_to_wav(Anew, phase, samples)

# print(norm)

rrqr_iteration(8, 50)
