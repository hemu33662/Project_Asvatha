import logging
import os
import sys
import subprocess
import pyautogui
import time
import psutil

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
# Import the SystemCommands class from the system_commands module

from Core.ScreenReading.screen_capture import capture_screenshot
from Core.ScreenReading.ocr_processing import extract_text_from_image
from Core.UserInteraction.voice_response import speak
from Core.CommandExecutor.system_commands import SystemCommands

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
        self.system_commands = SystemCommands()
        self.base_dir = os.path.expanduser("~")  # Instantiate SystemCommands
        self.screenshot_dir = os.path.join(self.base_dir, "screenshots")
        self.parser = CommandParser()  # Reference to CommandParser
        # Registering command handlers with the CommandParser
        self.parser.register_command("open", self.open_application)
        self.parser.register_command("shutdown", self.shutdown_system)
        self.parser.register_command("close", self.close_application)
        self.parser.register_command("restart", self.restart_system)

        # self.parser.register_command("lock", self.lock_system)
        # self.parser.register_command("logoff", self.logoff_system)
        self.parser.register_command("move", self.move_file)
        self.parser.register_command("rename", self.rename_file)
        self.parser.register_command("delete", self.delete_file)
        self.parser.register_command("change_volume", self.change_volume)
        self.parser.register_command("mute_volume", self.mute_volume)
        self.parser.register_command("change_brightness", self.change_brightness)
        self.parser.register_command("change_resolution", self.change_resolution)
        self.parser.register_command("take_screenshot", self.take_screenshot)
        self.parser.register_command("list_installed_apps", self.list_installed_apps)
        self.parser.register_command("run_custom_command", self.run_custom_command)
        self.parser.register_command("copy_to_clipboard", self.copy_to_clipboard)
        self.parser.register_command("get_clipboard_text", self.get_clipboard_text)
        self.parser.register_command("zip_files", self.zip_files)
        self.parser.register_command("download_file", self.download_file)
        self.parser.register_command("system_command", self.execute_system_command)

    def execute(self, command):
        """Main method to execute the command."""
        self.parser.parse(command)  # This will automatically route to the appropriate handler

    def execute_system_command(self, command):
        """ Executes system-level commands like shutdown or restart. """
        result = SystemCommands.execute_system_command(command)
        print(result) # This will automatically route to the appropriate handler

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

    def delete_file(self, command):
        """Deletes a file or folder."""
        path = command.strip()  # Extract the path from the command
        print(f"Attempting to delete: {path}")
        # Use the delete_command method from SystemCommands class
        SystemCommands.delete_command(path)

    # Adding methods that call the corresponding SystemCommands functions

    def change_volume(self, target):
        try:
            # Extract the volume level as an integer
            volume_level = int(target)
            print(f"Changing volume to {volume_level}%")
            # Call the appropriate system function to change the volume
            SystemCommands.change_volume(volume_level)
        except ValueError:
            print(f"Invalid volume level: {target}. Please provide a valid number.")


    def mute_volume(command):
        """Mute the system volume."""
        print("Muting the volume.")
        SystemCommands.mute_volume()

    def change_brightness(self, command):
        """Change screen brightness."""
        level = int(command.strip())
        print(f"Changing brightness to {level}%")
        SystemCommands.change_brightness(level)

    def change_resolution(self, command):
        """Change screen resolution."""
        resolution = command.strip()
        print(f"Changing resolution to {resolution}")
        SystemCommands.change_resolution(resolution)
    
    def take_screenshot(self):
        """Take a screenshot."""
        print("Taking screenshot.")
        SystemCommands.take_screenshot(self)

    def list_installed_apps(self):
        """List installed applications."""
        print("Listing installed applications.")
        apps = self.system_commands.list_installed_apps()
        print(apps)
        # SystemCommands.list_installed_apps(command)

    def run_custom_command(self, command):
        """Run a custom system command."""
        print(f"Running custom command: {command}")
        SystemCommands.run_custom_command(command)

    def copy_to_clipboard(self, command):
        """Copy text to clipboard."""
        text = command.strip()
        print(f"Copying text to clipboard: {text}")
        apps = self.system_commands.copy_to_clipboard(text)
        print(apps)

    def get_clipboard_text(self):
        """Get text from clipboard."""
        print("Getting clipboard text.")
        apps = self.system_commands.get_clipboard_text()
        print(apps)
        # SystemCommands.get_clipboard_text(command)

    def zip_files(self, command):
        """Zip files."""
        print(f"Zipping files: {command}")
        apps = self.system_commands.zip_files(command)
        print(apps)

    def download_file(self, command):
        """Download a file."""
        url = command.strip()
        print(f"Downloading file from: {url}")
        SystemCommands.download_file(url)

    def handle_screenshot_task():
        """
        Executes the screenshot task: captures a screenshot and processes it using OCR.
        """
        # Capture screenshot
        screenshot = capture_screenshot()
        screenshot_path = "screenshot.png"
        screenshot.save(screenshot_path)

        # Extract text from the screenshot using OCR
        extracted_text = extract_text_from_image(screenshot_path)

        # Provide feedback to the user via voice
        speak(f"Screenshot taken. Here's the extracted text: {extracted_text}")
        return extracted_text


    # execute_system_command(shutdown,lock,logoff,)
    # change_volume
    # mute_volume
    # change_brightness
    # change_resolution
    # take_screenshot
    # list_installed_apps
    # run_custom_command
    # copy_to_clipboard
    # get_clipboard_text
    # zip_files
    # delete_command
    # download_file

if __name__ == "__main__":
    executor = CommandExecutor()

    # executor.change_volume(30)
    # executor.execute("change volume 30")
    # executor.execute("change brightness 30")
    
    # executor.execute("mute volume")
    # executor.execute("change brightness 50")
    # executor.execute("open notepad")
    # executor.execute("take screenshot")
    # executor.execute("list installed apps")
    # executor.execute("copy to clipboard I'm Asvatha")
    # executor.execute("get clipboard text")
    # executor.execute("can you zip files  c:\\users\\heman\\downloads\\resume")
    # executor.execute(r"delete C:\Users\heman\Downloads\resume")
    # executor.execute("download file https://hemanthnasaram.netlify.app/NasaramHemanth_Resume.pdf")
    