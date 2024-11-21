# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.signal import spectrogram

# # Generate a sample audio signal (sine wave + noise)
# fs = 16000  # Sampling frequency (16 kHz)
# t = np.linspace(0, 2, fs * 2, endpoint=False)  # 2 seconds
# signal = np.sin(2 * np.pi * 440 * t) + 0.5 * np.random.normal(size=t.shape)

# # Compute the spectrogram
# f, t_spec, Sxx = spectrogram(signal, fs, nperseg=256, noverlap=128, scaling='density')

# # Convert to log scale (optional)
# Sxx_log = 10 * np.log10(Sxx + 1e-10)  # Add small value to avoid log(0)

# # Plot the spectrogram
# # plt.figure(figsize=(10, 6))
# # plt.pcolormesh(t_spec, f, Sxx_log, shading='gouraud', cmap='viridis')
# # plt.colorbar(label='Power (dB)')
# # plt.ylabel('Frequency [Hz]')
# # plt.xlabel('Time [s]')
# # plt.title('Spectrogram')
# # plt.show()

# print(Sxx_log)

import numpy as np
from scipy.signal import stft, istft
import matplotlib.pyplot as plt

# Generate a sample sine wave signal
fs = 16000  # Sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)  # Time vector
signal = np.sin(2 * np.pi * 440 * t)  # 440 Hz sine wave

# Compute the spectrogram
f, t_spec, Zxx = stft(signal, fs, nperseg=256)

# Reconstruct the audio signal from the spectrogram
_, reconstructed_signal = istft(Zxx, fs)

# Define the zoom interval (e.g., 0.1 to 0.12 seconds)
start_time = 0.1  # Start of zoom interval
end_time = 0.12  # End of zoom interval
start_idx = int(start_time * fs)
end_idx = int(end_time * fs)

# Plot original vs. reconstructed, zoomed in
plt.figure(figsize=(10, 6))

# Original signal zoomed in
plt.subplot(2, 1, 1)
plt.plot(t[start_idx:end_idx], signal[start_idx:end_idx], label="Original Signal")
plt.title(f"Original Signal (Zoomed: {start_time}s to {end_time}s)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

# Reconstructed signal zoomed in
plt.subplot(2, 1, 2)
plt.plot(t[start_idx:end_idx], reconstructed_signal[start_idx:end_idx], label="Reconstructed Signal", color='orange')
plt.title(f"Reconstructed Signal (Zoomed: {start_time}s to {end_time}s)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()
