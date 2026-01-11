# File Organizer / Rearranger

This is a Python project to organize files in a folder automatically.

## What it does
The project rearranges all files in a folder into subfolders based on their type.  
Images, Documents, Videos, Music files are moved into separate folders.  
Unknown file types are moved into an "Others" folder.  
It also displays the list of moved files.

## How it is built
- Python: For handling files and folders  
- shutil: To move files from one folder to another  
- os: To list files and create folders  
- Gradio: For a simple user interface to run the organizer

## Usage
1. Run `file_organizer.py` in Google Colab or local environment  
2. Enter the folder path containing files  
3. Click "Organize Files" to automatically rearrange the files
