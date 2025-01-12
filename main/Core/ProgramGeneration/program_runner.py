import subprocess
import os

class ProgramRunner:
    def __init__(self, language, file_path):
        self.language = language
        self.file_path = file_path

    def run_python(self):
        """
        Runs the generated Python code.
        """
        try:
            subprocess.run(["python3", self.file_path], check=True)
            print("Python program executed successfully.")
        except subprocess.CalledProcessError:
            print("Error executing Python program.")
    
    def run_java(self):
        """
        Compiles and runs the generated Java code.
        """
        try:
            subprocess.run(["javac", self.file_path], check=True)  # Compile
            class_name = os.path.splitext(os.path.basename(self.file_path))[0]
            subprocess.run(["java", class_name], check=True)  # Run
            print("Java program executed successfully.")
        except subprocess.CalledProcessError:
            print("Error executing Java program.")
    
    def run_javascript(self):
        """
        Runs the generated JavaScript code using Node.js.
        """
        try:
            subprocess.run(["node", self.file_path], check=True)
            print("JavaScript program executed successfully.")
        except subprocess.CalledProcessError:
            print("Error executing JavaScript program.")
    
    def run_code(self):
        """
        Runs language-specific code.
        """
        if self.language == "python":
            self.run_python()
        elif self.language == "java":
            self.run_java()
        elif self.language == "javascript":
            self.run_javascript()
        else:
            print(f"Unsupported language for running code: {self.language}")
