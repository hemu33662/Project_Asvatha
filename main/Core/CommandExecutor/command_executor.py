import os
import sys
import subprocess
import pyautogui
import time
import psutil

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from Core.VoiceRecognition.command_parser import CommandParser

# Predefined application mappings (for some common apps)
app_mappings = {
    "notepad": "notepad.exe",
    "paint": "mspaint.exe",
    "chrome": "chrome.exe",
    "firefox": "firefox.exe",
    "edge": "msedge.exe",
    "opera": "opera.exe",
    "brave": "brave.exe",
    "word": "winword.exe",
    "excel": "excel.exe",
    "powerpoint": "powerpnt.exe",
    "outlook": "outlook.exe",
    "teams": "teams.exe",
    "skype": "skype.exe",
    "vscode": "Code.exe",
    "intellij": "idea64.exe",
    "notepad++": "notepad++.exe",
    "vlc": "vlc.exe",
    "winrar": "winrar.exe",
    "discord": "discord.exe",
    "zoom": "zoom.exe",
    "steam": "steam.exe",
    "git bash": "git-bash.exe",
    "docker": "Docker Desktop.exe",
    "mspaint": "mspaint.exe",
    "task manager": "taskmgr.exe",
    "control panel": "control.exe",
}

class CommandExecutor:
    def __init__(self):
        self.parser = CommandParser()  # Reference to CommandParser
        # Registering command handlers with the CommandParser
        self.parser.register_command("open", self.open_application)
        self.parser.register_command("shutdown", self.shutdown_system)
        self.parser.register_command("close", self.close_application)
        self.parser.register_command("restart", self.restart_system)
        self.parser.register_command("move", self.move_file)
        self.parser.register_command("rename", self.rename_file)
        
    def execute(self, command):
        """Main method to execute the command."""
        self.parser.parse(command)  # This will automatically route to the appropriate handler

    def open_application(self, target):
        """Opens an application based on the given parameters."""
        app_name = target.strip().lower()  # Normalize the input to lowercase
        print(f"Opening application: {app_name}")

        # Try to open directly first from predefined mappings
        if app_name in app_mappings:
            app_path = app_mappings[app_name]
            try:
                subprocess.run([app_path], check=True)
                print(f"Successfully opened {app_name}")
            except Exception as e:
                print(f"Failed to open {app_name}: {e}")
                self.open_with_search(target)
        else:
            # If not found in predefined mappings, try searching via taskbar search
            self.open_with_search(target)

    def open_with_search(self, query):
        """Simulate opening the taskbar search and typing the query."""
        pyautogui.hotkey('win', 's')
        time.sleep(0.5)
        pyautogui.write(query)
        time.sleep(0.5)
        pyautogui.press('enter')
        print(f"Opening {query} via taskbar search.")

    def close_application(self, target):
        """Closes the specified application."""
        app_name = target.strip().lower()

        # Print out the target being closed
        print(f"Attempting to close application: {app_name}")

        # Try to find and kill the process (using psutil to find the process)
        try:
            # Loop through all running processes
            for proc in psutil.process_iter(['pid', 'name']):
                # Check if the process name matches the app name
                if app_name in proc.info['name'].lower():
                    print(f"Closing {proc.info['name']} (PID: {proc.info['pid']})")
                    proc.terminate()  # Attempt to terminate the process
                    proc.wait()  # Wait for process to terminate
                    print(f"Successfully closed application: {proc.info['name']}")
                    return

            print(f"Application '{app_name}' not found or could not be closed.")
        
        except psutil.NoSuchProcess:
            print(f"Error: Process not found.")
        except psutil.AccessDenied:
            print(f"Error: Access denied when trying to close '{app_name}'.")
        except Exception as e:
            print(f"Error: {str(e)}")

    def shutdown_system(self, target):
        """Shuts down the system."""
        print("Shutting down system...")
        os.system("shutdown /s /f /t 0")

    def restart_system(self, target):
        """Restarts the system."""
        print("Restarting system...")
        os.system("shutdown /r /f /t 0")

    def move_file(self, command):
        """Moves a file from one location to another."""
        parameters = command.split(" to ")
        if len(parameters) == 2:
            source_path, destination_path = parameters
            print(f"Moving file from {source_path} to {destination_path}")
            try:
                os.rename(source_path, os.path.join(destination_path, os.path.basename(source_path)))
                print(f"Successfully moved the file to {destination_path}")
            except Exception as e:
                print(f"Failed to move file: {e}")
        else:
            print("Invalid file move command format.")

    def rename_file(self, command):
        """Renames a file."""
        parameters = command.split(" to ")
        if len(parameters) == 2:
            source_path, new_name = parameters
            print(f"Renaming file: {source_path} to {new_name}")
            try:
                os.rename(source_path, os.path.join(os.path.dirname(source_path), new_name))
                print(f"Successfully renamed file to {new_name}")
            except Exception as e:
                print(f"Failed to rename file: {e}")
        else:
            print("Invalid file rename command format.")


if __name__ == "__main__":
    executor = CommandExecutor()

    # Test cases
    executor.execute("start notepad")  # Should open Chrome directly if it's in app_mappings
    executor.execute("close notepad")
    # executor.execute("open Chrome")  # Same for "open" command
    # executor.execute("shutdown")  # Should trigger system shutdown
