import speech_recognition as sr
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))  

from Core.VoiceRecognition.voice_auth_integration import authenticate_and_process


class ConvertSpeechToText:
    def __init__(self, command_executor):
        self.command_executor = command_executor
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen_and_recognize(self):
        try:
            with self.microphone as source:
                print("Listening...")
                authenticate_and_process()
                audio = self.recognizer.listen(source, timeout=20)
            return self.recognizer.recognize_google(audio)
        except sr.WaitTimeoutError:
            print("Timeout occurred while listening.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None
        # except KeyboardInterrupt:
        #     print("Listening interrupted.")
        #     return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    