import os
import shutil
import requests

def download_file(url, destination_folder):
    try:
        # Send HTTP request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Extract filename from the URL
        filename = os.path.join(destination_folder, url.split('/')[-1])

        # Write the content of the file to disk
        with open(filename, 'wb') as file:
            file.write(response.content)
        
        print(f"File downloaded successfully: {filename}")
        return filename

    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
        return None


def move_file(source_path, destination_path):
    try:
        shutil.move(source_path, destination_path)
        print(f"File moved from {source_path} to {destination_path}")
    except Exception as e:
        print(f"Error moving file: {e}")


def rename_file(source_path, new_name):
    try:
        directory = os.path.dirname(source_path)
        new_path = os.path.join(directory, new_name)
        os.rename(source_path, new_path)
        print(f"File renamed from {source_path} to {new_path}")
        return new_path
    except Exception as e:
        print(f"Error renaming file: {e}")
        return None
