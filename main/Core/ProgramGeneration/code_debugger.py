import subprocess

class CodeDebugger:
    def __init__(self, language, file_path):
        self.language = language
        self.file_path = file_path

    def debug_python(self):
        """
        Runs Python syntax check on the generated Python code.
        """
        try:
            subprocess.run(["python3", "-m", "py_compile", self.file_path], check=True)
            print("Python code is free of syntax errors.")
        except subprocess.CalledProcessError:
            print("Syntax errors detected in Python code.")
    
    def debug_java(self):
        """
        Runs Java syntax check on the generated Java code.
        """
        try:
            subprocess.run(["javac", self.file_path], check=True)
            print("Java code is free of syntax errors.")
        except subprocess.CalledProcessError:
            print("Syntax errors detected in Java code.")
    
    def debug_javascript(self):
        """
        Runs JavaScript linting (using `eslint`) on the generated code.
        """
        try:
            subprocess.run(["eslint", self.file_path], check=True)
            print("JavaScript code is free of linting issues.")
        except subprocess.CalledProcessError:
            print("Linting issues detected in JavaScript code.")
    
    def debug_code(self):
        """
        Runs language-specific syntax checking and debugging.
        """
        if self.language == "python":
            self.debug_python()
        elif self.language == "java":
            self.debug_java()
        elif self.language == "javascript":
            self.debug_javascript()
        else:
            print(f"Unsupported language for debugging: {self.language}")
