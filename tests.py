import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as linalg
from gen_rank_def import genRankDef
from Rank_deficient import *
from wav_to_spectrogram import *
from QR_expand import *


spect, phase, samples, _, _ = wav_to_spectrogram("Purple_Rain_Guitar.wav")

Q, R, P = Parker_Compression(spect, 100)

# Arand = reconstruct(Qexpand, Rexpand, P)

Anew = reconstruct(Q, R, P)

spectrogram_to_wav(Anew, phase, samples)