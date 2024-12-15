import numpy as np
from scipy.io import wavfile

def normalize_audio_wavfile(input_path, output_path, target_peak=0.9):
    # Read the audio file
    sample_rate, data = wavfile.read(input_path)
    
    # Check if audio is stereo or mono
    if len(data.shape) == 2:
        # Stereo: Normalize each channel separately
        max_val = np.max(np.abs(data), axis=0)
        scaling_factor = target_peak / max_val
        normalized_data = (data * scaling_factor).astype(data.dtype)
    else:
        # Mono: Normalize
        max_val = np.max(np.abs(data))
        scaling_factor = target_peak / max_val
        normalized_data = (data * scaling_factor).astype(data.dtype)
    
    # Save the normalized audio
    wavfile.write(output_path, sample_rate, normalized_data)
    print(f"Normalized audio saved to {output_path}")

# Example usage
input_file = "Purple_Rain_Guitar.wav"
output_file = "Purple_Rain_Normalized.wav"
normalize_audio_wavfile(input_file, output_file)
