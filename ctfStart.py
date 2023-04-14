#!/usr/bin/env python3
# ctfStart.py - Creates a new directory for a Capture the Flag (CTF) challenge.
# The program will take a single argument via the command line which will be the name of the directory to create.
# The program will then move the user into the newly created directory and spawn a bash shell for working in the new directory.


import os
import sys

if len(sys.argv) != 2:
    print('Usage: ctfStart.py <directory>')
    sys.exit()

user = (os.getlogin())                                  # Get the logged in user.
ctfDirectory = f'/home/{user}/tryhackme'                      # Path to the directory of stored CTF challenges.
newCTF = os.path.join(ctfDirectory, sys.argv[1])        # Create the absolute path to the CTF directory.

print(f'Creating new directory {newCTF}...')

try:
    os.makedirs(newCTF)                                 # Create new CTF directory and any parent directories in the path.
except FileExistsError:
    print('Specified directory already exists!')        # Catch the error if the directory already exists.
    sys.exit()
    
print(f'Created directory {newCTF}')
os.chdir(newCTF)                            # Change the current working directory to the newly created directory.
os.system('/bin/bash')                      # Spawn a bash shell in the newly created directory.
                                            # This allows the user to work in the new directory without changing to it manually.
