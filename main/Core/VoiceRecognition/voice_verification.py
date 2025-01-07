import os
import numpy as np
from scipy.spatial.distance import cosine
import wave
import pyaudio

VOICE_PROFILE_DIR = "Core/VoiceRecognition/profiles"
PROFILE_FILENAME = "user_voice_profile.npy"
THRESHOLD = 0.3  # Adjust threshold based on testing

def load_voice_profile(filename=PROFILE_FILENAME):
    """Load the saved voice profile."""
    filepath = os.path.join(VOICE_PROFILE_DIR, filename)
    if not os.path.exists(filepath):
        raise FileNotFoundError("Voice profile not found. Please create one first.")
    return np.load(filepath)

def record_for_verification(duration=5):
    """Record a new voice sample for verification."""
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000

    audio = pyaudio.PyAudio()

    print(f"Recording for verification ({duration} seconds). Please speak clearly...")
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    frames = []
    for _ in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording complete.")
    stream.stop_stream()
    stream.close()
    audio.terminate()

    audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)
    return audio_data

def verify_voice():
    """Verify the new voice sample against the saved profile."""
    try:
        saved_profile = load_voice_profile()
        new_sample = record_for_verification()

        # Calculate cosine similarity
        similarity = 1 - cosine(saved_profile, new_sample)
        print(f"Similarity score: {similarity:.2f}")

        if similarity >= THRESHOLD:
            print("Voice verified successfully!")
            return True
        else:
            print("Voice verification failed.")
            return False
    except Exception as e:
        print(f"Error during verification: {e}")
        return False

if __name__ == "__main__":
    verify_voice()
