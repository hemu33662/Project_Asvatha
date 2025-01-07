import os
import wave
import pyaudio
import numpy as np

VOICE_PROFILE_DIR = "Core/VoiceRecognition/profiles"
PROFILE_FILENAME = "user_voice_profile.npy"

def record_voice(duration=5, filename=PROFILE_FILENAME):
    """Record the user's voice for a given duration and save it as a profile."""
    if not os.path.exists(VOICE_PROFILE_DIR):
        os.makedirs(VOICE_PROFILE_DIR)

    filepath = os.path.join(VOICE_PROFILE_DIR, filename)
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000

    audio = pyaudio.PyAudio()

    print(f"Recording for {duration} seconds. Please speak clearly...")
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    frames = []

    for _ in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording complete. Saving voice profile...")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save raw audio
    with wave.open(filepath.replace(".npy", ".wav"), 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    # Convert to numpy array for verification use
    audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)
    np.save(filepath, audio_data)
    print(f"Voice profile saved at {filepath}.")

if __name__ == "__main__":
    record_voice()
