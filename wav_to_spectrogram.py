import numpy as np
from scipy.io import wavfile
from scipy.signal import stft
from scipy.signal import istft
from scipy.io.wavfile import write
import os


def wav_to_spectrogram(filename):
    
    samples, data = wavfile.read(filename)

    if data.ndim == 2:
        data = np.mean(data, axis=1)

    frequencies, times, Sxx = stft(data, fs=samples, nperseg=1024, noverlap=512)

    spect = np.abs(Sxx)
    phase = np.angle(Sxx)

    return spect, phase, samples

def spectrogram_to_wav(spect, phase, samples):

    Sxx_reconstructed = spect * np.exp(1j * phase)

    _, reconstruction = istft(Sxx_reconstructed, fs=samples, nperseg=1024, noverlap=512)

    reconstruction = reconstruction / np.max(np.abs(reconstruction))  

    reconstruction = np.int16(reconstruction * 32767)

    if os.path.exists("reconstruction.wav"): 
        os.remove("reconstruction.wav")

    write("reconstruction_ε=1000.wav", samples, reconstruction)