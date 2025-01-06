import logging

class ErrorDetection:
    def __init__(self):
        logging.basicConfig(filename='errors.log', level=logging.ERROR)

    def detect_error(self, task):
        """
        Detects if a task is invalid.
        """
        if not task:
            self.log_error("No task to execute.")
            return True
        elif "action" not in task or "target" not in task:
            self.log_error(f"Invalid task format: {task}")
            return True
        return False

    def log_error(self, error_message):
        """
        Logs errors to a file.
        """
        logging.error(error_message)
        print(f"Error logged: {error_message}")
