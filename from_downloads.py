'''
from_downloads.py - Searches the /home/{USER}/Downloads/ directory for files that
were added (downloaded) on the current date and adds them to the current working
directory. This will grab all files and subdirectories within the Downloads directory.
This program uses the date and time modules to get today's date, the last modified
date of a file, and then formats the last modified date to match the syntax of the
today() method provided by the date module.
'''


import os
import time
from datetime import date
import shutil


USER = os.getlogin()
DOWNLOADS = os.path.abspath(f'/home/{USER}/Downloads')
CWD = os.getcwd()
TODAY = date.today()
CWD_LIST = os.listdir(CWD)

# Keep track of the files that were moved and not moved.
files_moved = []
files_not_moved = []

print(f'\nToday\'s date: {TODAY}')


# Search through the Downloads directory to find any files that were modified
# (downloaded) today and move them to the current working directory.
downloads_list = os.listdir(DOWNLOADS)
for filename in downloads_list:
    # If the file already exists in the CWD, then do not move (overwrite).
    if filename in CWD_LIST:
        files_not_moved.append(filename)
        continue
    else:
        # Get the last modified time of file, convert it and then format it to
        # match the today() date syntax.
        modified_time = os.path.getmtime(os.path.join(DOWNLOADS, filename))
        convert_time = time.localtime(modified_time)
        format_time = time.strftime('%Y-%m-%d', convert_time)

        # Move the file to the CWD if it was modified today.
        if str(format_time) == str(TODAY):
            shutil.move(os.path.join(DOWNLOADS, filename), os.path.join(CWD, filename))
            files_moved.append(filename)

# Print the results such as any files moved/not moved.
print(f'\n{len(files_moved)} file(s) moved from Downloads.')
print(f'\n{len(files_not_moved)} file(s) not moved from Downloads.')
print('\nExiting...\n')
