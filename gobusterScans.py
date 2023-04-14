#!/usr/bin/env python3
# gobusterScans.py - Performs two separate gobuster scans when the program is run.
# The program takes two command-line arguments when run. The first argument is the target ip and the second argument is the port number.
# The first scan will use the 'big.txt' directory list and the output will be saved as 'gobuster-big.txt'.
# The second scan will use the 'directory-list-2.3-small.txt' directory list and the output will be saved as 'gobuster-small.txt'.
# A directory path can be appended to the scan target as an optional argument given through the command line.
# This program is designed for automatic directory enumeration for CTF challenges.


import os
import sys
import time


# Collect the command-line arguments and ensure that two arguments, target IP and port, and passed
if len(sys.argv) != 4:
    print('Usage: gobusterScans.py <target ip> <port> <directory path>')
    sys.exit()

targetIP = sys.argv[1]          # Save the target IP.
targetPort = sys.argv[2]        # Save the target port.
targetPath = sys.argv[3]        # Save the appended directory path.
bigScan = f'gobuster dir -o gobuster-big.txt -w /opt/big.txt -u http://{targetIP}:{targetPort}{targetPath}'                             # Command for big scan.
smallScan = f'gobuster dir -o gobuster-big.txt -w /opt/directory-list-2.3-small.txt -u http://{targetIP}:{targetPort}{targetPath}'      # Command for small scan.

print('\nStarting big scan...\n')
os.system(bigScan)                                                     # Run the big scan.
print('Scan finished. Output saved as \'gobuster-big.txt\'.\n')

print('Starting small scan in 10 seconds...')                           # Wait 10 seconds before running the next scan.
time.sleep(5)                                                           # This gives the user a chance to cancel the program before running the next scan.
print('Starting small scan in 5 seconds...')
time.sleep(5)

print('\nStarting small scan...\n')
os.system(smallScan)                                                   # Run the small scan.
print('Scan finished. Output saved as \'gobuster-small.txt\'.\n')
print('Directory scanning finished. Exiting...')
