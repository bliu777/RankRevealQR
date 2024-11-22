import numpy as np
from scipy.io import wavfile
from scipy.signal import spectrogram
import matplotlib.pyplot as plt


def wav_to_spectrogram(filename):
    
    samples, data = wavfile.read(filename)

    if data.ndim == 2:
        data = np.mean(data, axis=1)

        frequencies, times, Sxx = spectrogram(data, samples, nperseg=1024)

        Sxx_log = 10 * np.log10(Sxx + 1e-10)

        Sxx_log -= np.max(Sxx_log) # normalization component

    return Sxx, Sxx_log