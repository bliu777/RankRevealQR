import numpy as np
import matplotlib.pyplot as plt
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

    return spect, phase, samples, frequencies, times

def spectrogram_to_wav(spect, phase, samples):

    Sxx_reconstructed = spect * np.exp(1j * phase)

    _, reconstruction = istft(Sxx_reconstructed, fs=samples, nperseg=1024, noverlap=512)

    reconstruction = reconstruction / np.max(np.abs(reconstruction))  

    reconstruction = np.int16(reconstruction * 32767)

    if os.path.exists("reconstruction.wav"): 
        os.remove("reconstruction.wav")

    write("Purple_Rain_Compressed.wav", samples, reconstruction)

def plot_spectrogram(filename):
    spect, phase, samples, frequencies, times = wav_to_spectrogram(filename)

    plt.figure(figsize=(10, 6))
    plt.imshow(np.log(spect), aspect='auto', cmap='inferno', origin='lower', 
               extent=[times.min(), times.max(), frequencies.min(), frequencies.max()])
    plt.colorbar(label='Log Magnitude')
    plt.title(f"Spectrogram Heatmap of {filename}")
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.show()