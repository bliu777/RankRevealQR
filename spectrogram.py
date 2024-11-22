import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

# Generate a sample audio signal (sine wave + noise)
fs = 16000  # Sampling frequency (16 kHz)
t = np.linspace(0, 2, fs * 2, endpoint=False)  # 2 seconds
signal = np.sin(2 * np.pi * 440 * t) + 0.5 * np.random.normal(size=t.shape)

# Compute the spectrogram
f, t_spec, Sxx = spectrogram(signal, fs, nperseg=256, noverlap=128, scaling='density')

# Convert to log scale (optional)
Sxx_log = 10 * np.log10(Sxx + 1e-10)  # Add small value to avoid log(0)

# Plot the spectrogram
# plt.figure(figsize=(10, 6))
# plt.pcolormesh(t_spec, f, Sxx_log, shading='gouraud', cmap='viridis')
# plt.colorbar(label='Power (dB)')
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [s]')
# plt.title('Spectrogram')
# plt.show()

print(len(Sxx_log))
