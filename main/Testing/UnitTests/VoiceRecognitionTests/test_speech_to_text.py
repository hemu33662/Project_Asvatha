import sys
import os
import unittest
from unittest.mock import Mock

# Add the Asvatha root directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from Core.VoiceRecognition.speech_to_text import ConvertSpeechToText

class TestSpeechToText(unittest.TestCase):
    def test_speech_to_text(self):
        mock_command_executor = Mock()
        stt = ConvertSpeechToText(command_executor=mock_command_executor)  # Pass the mock command executor
        result = stt.listen_and_recognize()  # Mock the microphone input for testing
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()
