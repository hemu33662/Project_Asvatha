import os

# Define the root directory of your project
project_root = r"D:\newProject\voiceAssistant\asvatha"

# Walk through the directory structure and add __init__.py where necessary
for root, dirs, files in os.walk(project_root):
    # Check if the directory already contains __init__.py
    if "__init__.py" not in files:
        # Create an empty __init__.py file
        open(os.path.join(root, "__init__.py"), 'w').close()
        print(f"Added __init__.py to {root}")
