import numpy as np
from scipy.io import wavfile
from scipy.signal import spectrogram
from scipy.signal import istft
from scipy.io.wavfile import write
from librosa import griffinlim
import os


def wav_to_spectrogram(filename):
    
    samples, data = wavfile.read(filename)

    if data.ndim == 2:
        data = np.mean(data, axis=1)

        frequencies, times, Sxx = spectrogram(data, samples, nperseg=1024, noverlap=512)

        Sxx_log = 10 * np.log10(Sxx + 1e-10)

        Sxx_log -= np.max(Sxx_log) # normalization component

    return Sxx, Sxx_log, samples


def spectrogram_to_wav_griffinlim(spect, samples):

    spect_mag = np.sqrt(spect)

    reconstructed_signal = griffinlim(spect_mag, n_iter=32, hop_length=512, win_length=1024)
    
    reconstructed_signal = np.int16(reconstructed_signal / np.max(np.abs(reconstructed_signal)) * 32767)
    
    if os.path.exists("griffinlim_reconstruction.wav"): 
        os.remove("griffinlim_reconstruction.wav")

    write("griffinlim_reconstruction.wav", samples, reconstructed_signal)