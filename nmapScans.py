#!/usr/bin/env python3
# nmapScans.py - Performs two separate nmap scans on a target given through the command line when the program is run.
# The first scan is a basic 'quick' scan to get some common ports and run some basic NSE scripts.
# The second scan is a full port scan that searches for all open ports and runs some basic NSE scripts.
# The output of the scans are saved to initial.nmap and all-ports.nmap, respectively.
# This program is designed for automatic enumeration of ports for CTF challenges.


import os
import time
import sys


# Collect the first argument passed to to the program and ensure there is only one argument passed.
if len(sys.argv) != 2:
    print('Usage: nmapScans.py <target ip>')
    sys.exit()

targetIP = sys.argv[1]                                                      # Save the target IP.
basicScan = f'nmap -sV -sC -oN initial.nmap -vv {targetIP}'                 # Command for basic scan.
fullScan = f'nmap -sV -sC -oN all-ports.nmap -p- -vv {targetIP}'            # Command for full scan.

print('Starting basic scan...\n')
os.system(basicScan)                                                        # Run the basic scan.
print('Basic scan complete. Output file saved as \'initial.nmap\'.\n')

print('Starting full port scan in 10 seconds...')                           # Wait 10 seconds before running the next scan.
time.sleep(5)                                                               # This gives the user a chance to cancel the program before the next scan is run.
print('Starting full port scan in 5 seconds...')
time.sleep(5)

print('Starting full port scan...\n')
os.system(fullScan)                                                         # Run the full scan.
print('Full port scan complete...\n')
print('Basic port enumeration finished. Exiting...')
