'''
gobusterScans.py - Performs two separate gobuster scans when the program is run.
The program takes two command-line arguments when run. The first argument is the
target ip and the second argument is the port number.The first scan output will
be saved as 'gobuster-big.txt'. The second scan output will be saved as
'gobuster-small.txt'. A directory path can be appended to the scan target as an
optional argument given through the command line.

This program is designed for automatic directory enumeration for CTF challenges
on Kali Linux systems..
'''



import os
import sys
import time


# Collect the command-line arguments and ensure that 3 arguments are passed.
if len(sys.argv) != 4:
    print('Usage: gobusterScans.py <target ip> <port> <directory path>')
    sys.exit()

TARGET_IP = sys.argv[1]          # Save the target IP.
TARGET_PORT = sys.argv[2]        # Save the target port.
TARGET_PATH = sys.argv[3]        # Save the appended directory path.

big_scan = f'gobuster dir -o gobuster-big.txt -w /opt/big.txt ' \
           f'-u http://{TARGET_IP}:{TARGET_PORT}{TARGET_PATH}'
small_scan = f'gobuster dir -o gobuster-big.txt -w /opt/directory-list-2.3-small.txt ' \
             f'-u http://{TARGET_IP}:{TARGET_PORT}{TARGET_PATH}'

# Run the big scan.
print('\nStarting big scan...\n')
os.system(big_scan)
print("Scan finished. Output saved as 'gobuster-big.txt'.\n")

print('Starting small scan in 10 seconds...')
time.sleep(5)
print('Starting small scan in 5 seconds...')
time.sleep(5)

# Run the small scan.
print('\nStarting small scan...\n')
os.system(small_scan)
print("Scan finished. Output saved as 'gobuster-small.txt'.\n")
print('Directory scanning finished. Exiting...')
