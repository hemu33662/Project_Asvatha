import unittest
from unittest.mock import patch
from Core.ProgramGeneration.code_debugger import CodeDebugger

class TestCodeDebugger(unittest.TestCase):

    @patch('subprocess.run')
    def test_debug_python(self, mock_run):
        mock_run.return_value = None  # Simulate successful debugging
        debugger = CodeDebugger(language="python", file_path="test.py")
        debugger.debug_python()
        mock_run.assert_called_with(["python3", "-m", "py_compile", "test.py"], check=True)

    @patch('subprocess.run')
    def test_debug_java(self, mock_run):
        mock_run.return_value = None
        debugger = CodeDebugger(language="java", file_path="TestClass.java")
        debugger.debug_java()
        mock_run.assert_called_with(["javac", "TestClass.java"], check=True)

    @patch('subprocess.run')
    def test_debug_javascript(self, mock_run):
        mock_run.return_value = None
        debugger = CodeDebugger(language="javascript", file_path="TestClass.js")
        debugger.debug_javascript()
        mock_run.assert_called_with(["eslint", "TestClass.js"], check=True)

if __name__ == "__main__":
    unittest.main()
