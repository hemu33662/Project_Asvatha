import os
import shutil
import requests

class FileManager:
    def __init__(self, destination_folder):
        self.destination_folder = destination_folder
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

    def download_file(self, url):
        try:
            # Send HTTP request to the URL
            response = requests.get(url)
            response.raise_for_status()  # Check if the request was successful

            # Extract filename from the URL using os.path.basename
            filename = os.path.join(self.destination_folder, os.path.basename(url.split("/")[-1]))

            # Write the content of the file to disk
            with open(filename, 'wb') as file:
                file.write(response.content)

            print(f"File downloaded successfully: {filename}")
            return filename

        except requests.exceptions.RequestException as e:
            print(f"Error downloading file: {e}")
            return None

    def move_file(self, source_path, destination_path):
        try:
            # Preserve the file extension when moving
            file_extension = os.path.splitext(source_path)[1]
            if not destination_path.endswith(file_extension):
                destination_path += file_extension  # Append the original file extension
            shutil.move(source_path, destination_path)
            print(f"File moved from {source_path} to {destination_path}")
        except Exception as e:
            print(f"Error moving file: {e}")

    def rename_file(self, source_path, new_name):
        try:
            # Get the original file extension
            file_extension = os.path.splitext(source_path)[1]
            directory = os.path.dirname(source_path)

            # Ensure the new name includes the original file extension
            new_name_with_extension = new_name + file_extension if not new_name.endswith(file_extension) else new_name
            new_path = os.path.join(directory, new_name_with_extension)

            os.rename(source_path, new_path)
            print(f"File renamed from {source_path} to {new_path}")
            return new_path
        except Exception as e:
            print(f"Error renaming file: {e}")
            return None

    def create_file(self, file_path, content=""):
        try:
            with open(file_path, 'w') as file:
                file.write(content)
            print(f"File created successfully: {file_path}")
            return file_path
        except Exception as e:
            print(f"Error creating file: {e}")
            return None


    def execute(self, action, *args, **kwargs):
        """
        Dynamically execute the corresponding file operation based on the action.
        """
        action_map = {
            "download": self.download_file,
            "move": self.move_file,
            "rename": self.rename_file,
            "create": self.create_file,
        }

        if action in action_map:
            return action_map[action](*args, **kwargs)  # Pass both positional and keyword arguments
        else:
            print(f"Unknown action: {action}")
            return None


# Example Usage
def main():
    # Initialize FileManager with a destination folder
    file_manager = FileManager(destination_folder="downloads")

    # Example dynamic file operations
    # file_manager.execute("download", "https://hemanthnasaram.netlify.app/NasaramHemanth_Resume.pdf")
    # file_manager.execute("move", "Downloads/NasaramHemanth_Resume.pdf", "downloads/moved_resume.pdf")
    # file_manager.execute("rename", "downloads/moved_resume.pdf", "my_resume")
    file_manager.execute("create", "downloads/test_file.txt", content="Hello, this is a test file.")

if __name__ == "__main__":
    main()
