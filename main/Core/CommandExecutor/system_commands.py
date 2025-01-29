import os
import platform
import subprocess
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from PIL import ImageGrab
import pyperclip
import shutil
import requests
from datetime import datetime

class SystemCommands:
    def __init__(self):
        # Create directories for organizing files
        self.base_dir = os.path.expanduser("~")  # User's home directory
        self.download_dir = os.path.join(self.base_dir, "downloads")
        self.screenshot_dir = os.path.join(self.base_dir, "screenshots")
        self.docs_dir = os.path.join(self.base_dir, "docs")
        
        # Create directories if they don't exist
        os.makedirs(self.download_dir, exist_ok=True)
        os.makedirs(self.screenshot_dir, exist_ok=True)
        os.makedirs(self.docs_dir, exist_ok=True)

    # --- System Command Functions ---
    def execute_system_command(self, command):
        """ Executes system-level commands like shutdown or restart. """
        try:
            if platform.system() == "Windows":
                if command == "shutdown":
                    os.system("shutdown /s /f /t 0")
                    return "System shutting down."
                elif command == "restart":
                    os.system("shutdown /r /f /t 0")
                    return "System restarting."
                elif command == "lock":
                    os.system("rundll32.exe user32.dll,LockWorkStation")
                    return "System locked."
                elif command == "logoff":
                    os.system("shutdown /l")
                    return "User logged off."
                else:
                    return "Unknown system command."
            else:
                return "Unsupported operating system."
        except Exception as e:
            return f"Error executing system command: {e}"

    # --- System Settings Functions ---
    # def open_application(self, app_name):
    #     """ Opens an application based on the OS and application name. """
    #     try:
    #         if platform.system() == "Windows":
    #             os.system(f"start {app_name}")
    #         elif platform.system() == "Darwin":  # macOS
    #             os.system(f"open -a {app_name}")
    #         elif platform.system() == "Linux":
    #             os.system(f"{app_name} &")
    #         else:
    #             return f"Unsupported OS: {platform.system()}"
    #         return f"Application {app_name} opened."
    #     except Exception as e:
    #         return f"Error opening application: {e}"
    
    def change_volume(volume_level):
        """ Adjust the system volume using pycaw. Volume level should be between 0 and 100. """
        try:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = interface.QueryInterface(IAudioEndpointVolume)

            if not (0 <= volume_level <= 100):
                return "Volume level must be between 0 and 100."

            volume.SetMasterVolumeLevelScalar(volume_level / 100.0, None)
            return f"Volume set to {volume_level}%"
        except Exception as e:
            return f"Error adjusting volume: {e}"
   
    def mute_volume(mute=True):
        """ Mute or unmute the system volume. """
        try:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = interface.QueryInterface(IAudioEndpointVolume)

            volume.SetMute(mute, None)
            return "Volume muted." if mute else "Volume unmuted."
        except Exception as e:
            return f"Error adjusting mute state: {e}"
    
    def change_brightness(brightness_level):
        """ Adjust the system brightness using PowerShell. Brightness level should be between 0 and 100. """
        try:
            if not (0 <= brightness_level <= 100):
                return "Brightness level must be between 0 and 100."

            command = f"(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{brightness_level})"
            subprocess.run(["powershell", "-Command", command], check=True)
            return f"Brightness set to {brightness_level}%"
        except Exception as e:
            return f"Error adjusting brightness: {e}"
    
    def change_resolution(self, resolution):
        """ Change the screen resolution. """
        try:
            if platform.system() == "Windows":
                width, height = map(int, resolution.split('x'))
                subprocess.run(["QRes.exe", f"/x:{width}", f"/y:{height}"], check=True)
                return f"Resolution set to {width}x{height}"
            else:
                return "Resolution change is not supported on this platform."
        except Exception as e:
            return f"Error changing resolution: {e}"
    
    def take_screenshot(self):
        """Take a screenshot and save it to the screenshots directory."""
        try:
            screenshot_name = f"screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
            screenshot_path = os.path.join(self.screenshot_dir, screenshot_name)
            print(f"Saving screenshot to: {screenshot_path}")
            screenshot = ImageGrab.grab()
            screenshot.save(screenshot_path)
            print(f"Screenshot saved successfully to {screenshot_path}")
        except Exception as e:
            print(f"Error taking screenshot: {e}")

    
    def list_installed_apps(self):
        """ List installed applications (Windows only). """
        try:
            if platform.system() == "Windows":
                apps = subprocess.check_output(['powershell', '-Command', "Get-StartApps | Select-Object Name"]).decode()
                return apps
            else:
                return "Listing applications is not supported on this platform."
        except Exception as e:
            return f"Error listing installed applications: {e}"
   
    def run_custom_command(self, command):
        """ Execute a custom command. """
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout
            else:
                return f"Command error: {result.stderr}"
        except Exception as e:
            return f"Error executing command: {e}"
   
    def copy_to_clipboard(self, text):
        """ Copy text to the clipboard. """
        try:
            pyperclip.copy(text)
            return "Text copied to clipboard."
        except Exception as e:
            return f"Error copying to clipboard: {e}"
    
    def get_clipboard_text(self):
        """ Retrieve text from the clipboard. """
        try:
            return f"Clipboard content: {pyperclip.paste()}"
        except Exception as e:
            return f"Error retrieving clipboard content: {e}"
   
    def zip_files(self, file_paths):
        """Zip a directory into a single archive and save it in the same location."""
        try:
            # Get the directory and folder name from the provided file path
            dir_path = file_paths[0]
            dir_name = os.path.basename(dir_path)
            
            # Create the zip file in the same directory as the original folder
            zip_path = os.path.join(os.path.dirname(dir_path), dir_name)
            shutil.make_archive(zip_path, 'zip', root_dir=dir_path)
            
            return f"Directory zipped as {zip_path}.zip"
        except Exception as e:
            return f"Error zipping directory: {e}"

    def delete_command(path):
        """Delete a file or directory, prompting for admin access if needed."""

        
        def delete_file_or_directory(path):
            """Delete a file or directory."""
            try:
                os.remove(path)
                return f"File {path} deleted."
            except PermissionError:
                return "Access denied. You need administrator access to delete this file or folder."
            except OSError:
                return f"Error: Directory {path} is not empty or can't be deleted."
            except Exception as e:
                return f"Error deleting file/folder: {e}"

        def delete_with_admin(path):
            """Try to delete the file or directory with admin rights."""
            try:
                if os.path.isdir(path):
                    shutil.rmtree(path)  # Deletes folder and its contents
                    return f"Directory {path} deleted successfully with admin rights."
                elif os.path.isfile(path):
                    os.remove(path)  # Deletes file
                    return f"File {path} deleted successfully with admin rights."
                else:
                    return f"Path {path} does not exist."
            except Exception as e:
                return f"Error deleting file/folder with admin rights: {e}"

        # Try to delete the file/folder first
        result = delete_file_or_directory(path)
        print(result)

        # If access is denied or folder is not empty, prompt for admin rights
        if "Access denied" in result or "not empty" in result:
            print("Access denied or directory is not empty. You need administrator access to delete this file or folder.")
            user_response = input("Do you want to try deleting this file/folder with administrator rights? (yes/no): ").strip().lower()
            if user_response == "yes":
                # Attempt deletion with admin rights
                admin_result = delete_with_admin(path)
                print(admin_result)
            else:
                print("File/folder not deleted.")

    def download_file(self, url):
        """ Download a file from a URL and save it in the downloads directory. """
        try:
            file_name = url.split("/")[-1]
            save_path = os.path.join(self.download_dir, file_name)
            response = requests.get(url, stream=True)
            response.raise_for_status()  # Raise an exception for HTTP errors
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            return f"File downloaded successfully to {save_path}."
        except Exception as e:
            return f"Error downloading file: {e}"

# --- Example Usage ---
if __name__ == "__main__":
    system_commands = SystemCommands()

    # Execute some commands
    # print(system_commands.execute_system_command("lock"))
    # print(system_commands.open_application("notepad"))
    # print(system_commands.take_screenshot())
    # print(system_commands.download_file("https://hemanthnasaram.netlify.app/NasaramHemanth_Resume.pdf"))
    sc = SystemCommands()
    # print(sc.execute_system_command("lock"))
    # print(sc.change_volume(30))
    # print(sc.mute_volume(True))
    # print(sc.change_brightness(50))
    # print(sc.take_screenshot())
    # print(sc.copy_to_clipboard("Hello, Clipboard!"))
    # print(sc.get_clipboard_text())
    print(sc.zip_files([r"C:\Users\heman\Downloads\resume"]))
    # print(sc.delete_command(r"C:\Users\heman\Downloads\resume"))
    # print(sc.list_installed_apps())
