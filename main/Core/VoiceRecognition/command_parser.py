import re

class CommandParser:
    def __init__(self):
        self.command_handlers = {}

    def register_command(self, command_name, handler_function):
        """
        Register a new command handler for a specific command.
        """
        self.command_handlers[command_name.lower()] = handler_function

    def parse(self, command):
        """
        Parse and route the command to the appropriate handler.
        """
        command = command.lower()
        for keyword, handler in self.command_handlers.items():
            if re.search(r"\b" + re.escape(keyword) + r"\b", command, re.I):
                # Extract the relevant part of the command
                remaining_text = command.split(keyword, 1)[1].strip()
                if remaining_text:  # Ensure there's something after the command
                    handler(remaining_text)
                else:
                    print(f"Missing target for command: '{keyword}'.")
                return
        print(f"Unrecognized command: {command}")

# Command handlers
def open_application(command):
    app_name = command.strip()
    print(f"Opening application: {app_name}")

def close_application(command):
    app_name = command.strip()
    print(f"Closing application: {app_name}")

def shutdown_application(command):
    app_name = command.strip()
    print(f"Shutting down system.")

def restart_application(command):
    app_name = command.strip()
    print(f"Restarting system.")

# Register handlers
if __name__ == "__main__":
    parser = CommandParser()
    parser.register_command("open", open_application)
    parser.register_command("close", close_application)
    parser.register_command("shutdown", shutdown_application)
    parser.register_command("restart", restart_application)
    
    # Test cases
    parser.parse("open Chrome")  # Expected output: Opening application: Chrome
    parser.parse("close Notepad")  # Expected output: Closing application: Notepad
    parser.parse("open")  # Expected output: Missing target for command: 'open'.
    parser.parse("search Google")  # Expected output: Unrecognized command: search google
    parser.parse("restart system")



