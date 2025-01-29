import logging
import re
from fuzzywuzzy import fuzz

class CommandParser:
    def __init__(self, threshold=70):
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
            "change_volume": ["change volume", "adjust volume", "set volume", "volume up", "volume down"],
            "mute_volume": ["mute volume", "unmute volume", "toggle mute"],
            "change_brightness": ["change brightness", "adjust brightness", "increase brightness", "decrease brightness"],
            "change_resolution": ["change resolution", "adjust resolution", "set resolution"],
            "take_screenshot": ["take screenshot", "capture screen", "screenshot"],
            "list_installed_apps": ["list apps", "installed apps", "show apps", "installed programs"],
            "run_custom_command": ["run command", "execute command", "custom command"],
            "copy_to_clipboard": ["copy to clipboard", "copy", "clipboard copy"],
            "get_clipboard_text": ["get clipboard text", "clipboard text", "read clipboard"],
            "zip_files": ["zip files", "compress files", "archive files"],
            "delete_command": ["delete", "remove", "erase", "delete file"],
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
        # Normalize the command by removing unnecessary phrases
        command = re.sub(r'\b(can you|please|kindly|would you|could you|could|can)\b', '', command.lower()).strip()

        # Find the best matching action
        best_action = None
        highest_ratio = 0

        for action, synonyms in self.synonym_map.items():
            for synonym in synonyms:
                if synonym in command:
                    ratio = fuzz.partial_ratio(command, synonym)
                    if ratio > highest_ratio:
                        highest_ratio = ratio
                        best_action = action

        # Ensure the match meets the threshold
        if best_action and highest_ratio >= self.threshold:
            handler = self.command_handlers.get(best_action)
            if handler:
                # Extract the target (e.g., app name or URL) from the command, but handle special cases
                if best_action in ["take_screenshot", "shutdown", "list_installed_apps", "get_clipboard_text", "zip_files"]:
                    remaining_text = None  # No target needed
                else:
                    remaining_text = self.extract_target(command, best_action)

                if remaining_text is not None:
                    print(f"Detected intent: {best_action}")
                    print(f"Detected target: {remaining_text}")
                    handler(remaining_text)  # Invoke the handler with the target
                else:
                    print(f"Detected intent: {best_action}")
                    handler()  # Invoke the handler without a target
            else:
                print(f"Handler for '{best_action}' not registered.")
        else:
            print(f"Unrecognized command: {command}")

    def extract_target(self, command, action):
        """
        Extract the target (e.g., app name, file path) from the command.
        """
        print(f"Extracting target for action: {action}")
        print(f"Original command: {command}")
        synonyms = self.synonym_map[action]
        action_regex = rf"\b({'|'.join(synonyms)})\b"
        target = re.sub(action_regex, "", command).strip()  # Remove the action word
        return target if target else None


# Define command handler functions
def open_application(target):
    print(f"Opening application: {target}")

def close_application(target):
    print(f"Closing application: {target}")

def shutdown_system(target=None):
    print("Shutting down system...")

def change_volume(level):
    print(f"Changing volume to {level}%")

def mute_volume(mute_status):
    print(f"Muting volume: {mute_status}")

def change_brightness(level):
    print(f"Changing brightness to {level}%")

def change_resolution(resolution):
    print(f"Changing resolution to {resolution}")

def take_screenshot(target=None):
    print("Taking screenshot...")

def list_installed_apps(target=None):
    print("Listing installed applications...")

def run_custom_command(command):
    print(f"Running custom command: {command}")

def copy_to_clipboard(text):
    print(f"Copying to clipboard: {text}")

def get_clipboard_text(target=None):
    print("Getting clipboard text...")

def zip_files(files):
    print(f"Zipping files: {files}")

def delete_command(file_or_command):
    print(f"Deleting: {file_or_command}")

def download_file(url):
    print(f"Downloading file from: {url}")


if __name__ == "__main__":
    parser = CommandParser()

    # Register command handlers
    parser.register_command("open", open_application)
    parser.register_command("close", close_application)
    parser.register_command("shutdown", shutdown_system)
    parser.register_command("change_volume", change_volume)
    parser.register_command("mute_volume", mute_volume)
    parser.register_command("change_brightness", change_brightness)
    parser.register_command("change_resolution", change_resolution)
    parser.register_command("take_screenshot", take_screenshot)
    parser.register_command("list_installed_apps", list_installed_apps)
    parser.register_command("run_custom_command", run_custom_command)
    parser.register_command("copy_to_clipboard", copy_to_clipboard)
    parser.register_command("get_clipboard_text", get_clipboard_text)
    parser.register_command("zip_files", zip_files)
    parser.register_command("delete_command", delete_command)
    parser.register_command("download", download_file)

    # Test cases
    # parser.parse("start notepad")  # Expected: Opening application: notepad
    # parser.parse("open chrome")   # Expected: Opening application: chrome
    # parser.parse("shutdown")      # Expected: Shutting down system...
    parser.parse("change volume 30")  # Expected: Changing volume to 30%
    # parser.parse("mute volume")  # Expected: Muting volume: mute
    parser.parse("change brightness 80")  # Expected: Changing brightness to 80%
    parser.parse("take screenshot")  # Expected: Taking screenshot...
    parser.parse("list apps")  # Expected: Listing installed applications...
    parser.parse("copy to clipboard Hello World!")  # Expected: Copying to clipboard: Hello World!
    # parser.parse("zip files my_file.txt") 
    # parser.parse("can you zip files  c:\\users\\heman\\downloads\\resume") # Expected: Zipping files: my_file.txt
    # parser.parse("download https://example.com/file")  # Expected: Downloading file from: https://example.com/file
