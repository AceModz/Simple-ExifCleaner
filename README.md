# Simple-ExifCleaner

This Python script utilizes the Pillow and MoviePy libraries to remove Exif data from images and videos. It provides a user-friendly interface using the tkinter library to select the file for processing. The script automatically detects the file type (image or video) and creates a copy of the file without Exif data in a specified folder.

# Dependencies
• Pillow: Python image processing library.

•MoviePy: Python library for video editing.


# Windows :

    $ pip install Pillow moviepy

# Kali Linux :

    $ sudo apt-get update
    $ sudo apt-get install python3-pip python3-dev
    $ pip3 install Pillow moviepy



    

    


# Usage
1. Run the Python script.

# Windows :
    $ python main.py

# Kali Linux : 
    $ python3 main_kali.py

    

2. A dialog box will open to select the file for processing.
3. The script will create a copy of the file without Exif data in the specified folder.


# Script Functions
`remove_exif(file_path, output_folder)`
• Accepts the file path and an output folder as input.
• Removes Exif data from the image or video.
• Saves the new file in the specified folder.
`select_file()`
Uses the tkinter library to display a dialog box allowing the user to select a file.
Calls the remove_exif function based on the selected file type.
Notes
Ensure the required dependencies are installed before executing the script.
Files without Exif data will be saved in separate folders ("Removed Exif Image" or "Removed Exif Video").
    
