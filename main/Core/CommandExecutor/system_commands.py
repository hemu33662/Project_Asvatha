import os
import platform

def open_application(app_name):
    """
    Opens an application based on the OS and application name.
    """
    try:
        if platform.system() == "Windows":
            os.system(f"start {app_name}")
        elif platform.system() == "Darwin":  # macOS
            os.system(f"open -a {app_name}")
        elif platform.system() == "Linux":
            os.system(f"{app_name} &")
        else:
            print(f"Unsupported OS: {platform.system()}")
    except Exception as e:
        print(f"Error opening application: {e}")

def execute_system_command(command):
    """
    Executes system-level commands like shutdown or restart.
    """
    try:
        if platform.system() == "Windows":
            if command == "shutdown":
                os.system("shutdown /s /f /t 0")  # Shutdown immediately
            elif command == "restart":
                os.system("shutdown /r /f /t 0")  # Restart immediately
            else:
                print(f"Unknown system command: {command}")
        else:
            # For Linux or macOS
            if command == "shutdown":
                os.system("sudo shutdown now")  # Requires sudo for Linux/macOS
            elif command == "restart":
                os.system("sudo reboot")  # Requires sudo for Linux/macOS
            else:
                print(f"Unknown system command: {command}")
    except Exception as e:
        print(f"Error executing system command: {e}")
