import unittest
from unittest.mock import patch
from Core.ProgramGeneration.program_runner import ProgramRunner

class TestProgramRunner(unittest.TestCase):

    @patch('subprocess.run')
    def test_run_python(self, mock_run):
        mock_run.return_value = None
        runner = ProgramRunner(language="python", file_path="test.py")
        runner.run_python()
        mock_run.assert_called_with(["python3", "test.py"], check=True)

    @patch('subprocess.run')
    def test_run_java(self, mock_run):
        mock_run.return_value = None
        runner = ProgramRunner(language="java", file_path="TestClass.java")
        runner.run_java()
        mock_run.assert_called_with(["javac", "TestClass.java"], check=True)
        mock_run.assert_any_call(["java", "TestClass"], check=True)

    @patch('subprocess.run')
    def test_run_javascript(self, mock_run):
        mock_run.return_value = None
        runner = ProgramRunner(language="javascript", file_path="TestClass.js")
        runner.run_javascript()
        mock_run.assert_called_with(["node", "TestClass.js"], check=True)

if __name__ == "__main__":
    unittest.main()
