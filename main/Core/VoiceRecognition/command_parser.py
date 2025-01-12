import re
from fuzzywuzzy import fuzz

class CommandParser:
    def __init__(self, threshold=0.5):
        self.command_handlers = {}
        self.synonym_map = {
            "open": ["open", "launch", "start"], 
            "shutdown": ["shutdown", "turn off", "power off"],
            "close": ["close", "exit", "quit"],
            "restart": ["restart", "reboot"],
            "navigate": ["navigate", "go to"],
            "move": ["move", "transfer"],
            "rename": ["rename", "change name"],
            "download": ["download"],
        }
        self.threshold = threshold

    def register_command(self, command_name, handler_function):
        """
        Register a new command handler for a specific command.
        """
        self.command_handlers[command_name.lower()] = handler_function
        
    def parse(self, command):
        """
        Parse and route the command to the appropriate handler.
        """
        # command = command.lower()
        command = re.sub(r'[^\w\s:/.]', '', command.lower())  # Remove non-alphanumeric characters except spaces and URL-related chars
        

        # Fuzzy matching to find the closest command
        best_match = None
        highest_ratio = 0

        # Check for synonyms and match commands dynamically
        for action, synonyms in self.synonym_map.items():
            for synonym in synonyms:
                # ratio = difflib.SequenceMatcher(None, command, synonym).ratio()
                ratio = fuzz.ratio(command, synonym) 
                if ratio > highest_ratio:
                    highest_ratio = ratio
                    best_match = action

        # If a good match is found, route to the appropriate handler
        if highest_ratio >= self.threshold:  # This threshold ensures a close enough match
            handler = self.command_handlers.get(best_match)
            if handler:
                remaining_text = self.extract_target(command, best_match)
                if remaining_text:
                    handler(remaining_text)  # Pass the extracted target
                else:
                    print(f"Missing target for command: '{best_match}'.")
            else:
                print(f"Handler for '{best_match}' not registered.")
        else:
            print(f"Unrecognized command: {command}")

    def extract_target(self, command, action):
        """
        Extract the target (e.g., app name, file path) from the command.
        """
        # Remove the action (e.g., "open") from the command to leave the target (e.g., "chrome")
        synonyms = self.synonym_map[action]
        action_regex = rf"\b({'|'.join(synonyms)})\b"
        target = re.sub(action_regex, "", command).strip()  # Remove the action word
        return target if target else None


# Define command handler functions
def open_application(target):
    print(f"Opening application: {target}")

def shutdown_system(target=None):
    print(f"Shutting down system...")


if __name__ == "__main__":
    parser = CommandParser()

    # Register command handlers
    parser.register_command("open", open_application)
    parser.register_command("shutdown", shutdown_system)
    parser.register_command("download", lambda target: print(f"downloaded application: {target}"))

    # Test cases
    parser.parse("start notepad")  # Expected: Opening application: notepad
    parser.parse("open chrome")   # Expected: Opening application: chrome
    parser.parse("shutdown")      # Expected: Shutting down system...
    parser.parse("download https://drive.google.com/drive/home/nasaramhemanth.pdf") # Expected: Unrecognized command: download
