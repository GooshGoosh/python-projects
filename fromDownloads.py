#!/usr/bin/env python3
# fromDownloads.py - Searches the /home/{user}/Downloads/ directory for files that were added (downloaded) on the current date and adds them to
# the current working directory. This will grab all files and subdirectories within the Downloads directory.
# This program uses the date and time modules to get today's date, the last modified date of a file, and then formats the last modified date to match the
# syntax of the today() method provided by the date module. 

import os
import time
from datetime import date
import shutil


user = (os.getlogin())                                      # Get the current logged in user.
downloads = os.path.abspath(f'/home/{user}/Downloads')      # Set the path of the Downloads folder.
currentDirectory = os.getcwd()                              # Set the path of the current working directory.
today = date.today()                                        # Get today's date.
currentDirectoryList = os.listdir(currentDirectory)         # Search through the current directory and make a list of files already present in the directory.
filesMoved = []                                             # Keep track of files that were moved.
filesNotMoved = []                                          # Keep track of files that were not moved (likely due to overwrite to already existing files).

print(f'\nToday\'s date: {today}')


# Search through the Downloads directory to find any files that were modified (downloaded) today and move them to the current working directory.
downloadsList = os.listdir(downloads)
for filename in downloadsList:
    if filename in currentDirectoryList:
        filesNotMoved.append(filename)
        continue
    else:
        modifiedTime = os.path.getmtime(os.path.join(downloads, filename))                                  # Get the last modified time of a file.
        convertTime = time.localtime(modifiedTime)                                                          # Convert the last modified time to struct_time.
        formatTime = time.strftime('%Y-%m-%d', convertTime)                                                 # Format the struct_time to match the date syntax returned via the today() method.
        if str(formatTime) == str(today):                                                                   # If the file was modified today,
            shutil.move(os.path.join(downloads, filename), os.path.join(currentDirectory, filename))        # then move the file to the current working directory.
            filesMoved.append(filename)                                                                     # Add the file to the list of moved files.

# Print the results such as any files moved/not moved.
print('\n' + str(len(filesMoved)) + ' file(s) moved from Downloads:')               # Print the number of moved files.

print('\n' + str(len(filesNotMoved)) + ' file(s) not moved from Downloads:')        # Print the number of unmoved files.
    
print('\nExiting...\n')
        
