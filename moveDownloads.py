#!/usr/bin/env python3
# moveDownloads.py - This program will search in the Downloads folder of the current user (/home/user/Downloads) and send specific file types to
# various standard directories of a typical user file system.
# These directories include Documents, Music, Pictures, and Videos.
# The file extension lists for the various documents can be modified to include additional file extensions for a specific directory or to have
# a current file extension moved to a different directory (e.g. adding '.txt' to the Pictures directory).

import os
import shutil

# Set username, directory, and file extension list variables
user = (os.getlogin())                                                                              # Get the current user.
downloads = os.path.abspath(f'/home/{user}/Downloads')                                              # Set the path of the Downloads folder.
documents = os.path.abspath(f'/home/{user}/Documents')                                              # Set the path of the Documents folder.
music = os.path.abspath(f'/home/{user}/Music')                                                      # Set the path of the Music folder.
pictures = os.path.abspath(f'/home/{user}/Pictures')                                                # Set the path of the Pictures folder.
videos = os.path.abspath(f'/home/{user}/Videos')                                                    # Set the path of the Videos folder.

documentsExtensions = ['.txt', '.doc', '.docx', '.pdf', '.html',
                       '.ppt', '.pptx', '.xlsx', '.odt', '.odf']                                    # List of file extensions to be moved to Documents.
musicExtensions = ['.mp3', '.wav', '.aiff', '.pcm', '.flac',
                   '.alac', '.wma', '.ogg', '.aac']                                                 # List of file extensions to be moved to Music.
picturesExtensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp',
                      '.raw', '.tiff', '.psd', '.cr2']                                              # List of file extensions to be moved to Pictures.
videosExtensions = ['.mp4', '.mov', '.avi', '.flv', '.mkv',
                    '.wmv', '.avchd', '.webm', '.mpeg-4']                                           # List of file extensions to be moved to Videos.

filesMoved = []                                                                                     # Store a list of moved files.
filesNotMoved = []                                                                                  # Store a list of files not moved.
subFolders = []                                                                                     # Store a list of subfolders that are in Downloads.

# Create a list of files in each folder
documentsFiles = []
musicFiles = []
picturesFiles = []
videosFiles = []

# Search for files that already exist in a specified folder.
def existing_files(fileList, folder):
    folderFiles = os.listdir(folder)        # List the files already in the folder.
    for filename in folderFiles:
        fileList.append(filename)           # Add existing files to a list.


# Search for files in Downloads and move them to the appropriate folder.
def move_files (destFolder, extList, fileList):
    downloadsFiles = os.listdir(downloads)                                                                  # List the downloads directory to get all files and subdirectories.
    for filename in downloadsFiles:
        if os.path.isdir(os.path.join(downloads, filename)) == True:                                        # If a subdirectory is found, then add it to the list of subdirectories
            if filename not in subFolders:                                                                  # and continue to the next file in the list.
                subFolders.append(filename)
            continue
        else:
            file = os.path.splitext(filename)
            if file[1] in extList:
                if filename in fileList:                                                                    # Check if the file already exists in the desination folder.
                    print(f'\nFile \'{filename}\' already in {destFolder}')
                    filesNotMoved.append(filename)
                else:
                    shutil.move(os.path.join(downloads, filename), os.path.join(destFolder, filename))      # Move the file to the destination folder.
                    filesMoved.append(filename)
            else:
                continue

# Start of program.
print(f'\nSearching through {downloads} for files...\n')

existing_files(documentsFiles, documents)
existing_files(musicFiles, music)
existing_files(picturesFiles, pictures)
existing_files(videosFiles, videos)

move_files(documents, documentsExtensions, documentsFiles)
move_files(music, musicExtensions, musicFiles)
move_files(pictures, picturesExtensions, picturesFiles)
move_files(videos, videosExtensions, videosFiles)

# Print results such as any subfolders, files moved, and files not moved.
print('\n' + str(len(subFolders)) + ' subfolder(s) in Downloads not moved:')                        # Print out the list of subfolders in Downloads.
for name in range(len(subFolders)):
    print(subFolders[name])

print('\n' + str(len(filesMoved)) + ' file(s) moved from Downloads:')                               # Print the number of moved files.

print('\n' + str(len(filesNotMoved)) + ' file(s) not moved from Downloads:')                        # Print the number of unmoved files.
    
print('\nExiting...\n')
