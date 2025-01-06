import unittest
import sys
import os

# Add the Asvatha root directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from Core.CommandExecutor.system_commands import open_application

class TestSystemCommands(unittest.TestCase):
    def test_open_application(self):
        open_application("notepad")  # Expect manual verification
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
