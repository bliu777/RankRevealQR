import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as linalg
from gen_rank_def import genRankDef
from Rank_deficient import *
from wav_to_spectrogram import *


spect, phase, samples = wav_to_spectrogram("test_file.wav")

ranks = []

for eps in range(1, 2000, 20):
    Qnew, Rnew, P = Parker_Compression(spect, e=eps)
    rank = Qnew.shape[1]
    print(rank)
    ranks.append(rank)

plt.plot(range(1, 2000, 20), ranks)
plt.show()

# Anew = reconstruct(Qnew, Rnew, P)

# print(f"Reconstruction shape: {Anew.shape}")

# diff = spect - Anew
# norm = linalg.norm(diff)
# print(f"Norm of diff: {norm}")

# spectrogram_to_wav(Anew, phase, samples)