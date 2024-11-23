import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as linalg
from gen_rank_def import genRankDef
from Rank_deficient import *
from wav_to_spectrogram import *


spect, phase, samples = wav_to_spectrogram("test_file.wav")
print(spect.shape)

Q, R, P = Parker_Compression(spect, 1000)

Anew = reconstruct(Q, R, P)

spectrogram_to_wav(Anew, phase, samples)
