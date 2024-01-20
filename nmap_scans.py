'''
nmap_scans.py - Performs two separate nmap scans on a target given through the
command line when the program is run. The first scan is a basic 'quick' scan to
get some common ports and run some basic NSE scripts. The second scan is a full
port scan that searches for all open ports and runs some basic NSE scripts.The
output of the scans are saved to initial.nmap and all-ports.nmap, respectively.

This program is designed for automatic enumeration of ports for CTF challenges
on Kali Linux systems.
'''


import os
import time
import sys


# Collect the first argument passed to to the program and ensure there is only one argument passed.
if len(sys.argv) != 2:
    print('Usage: nmapScans.py <target ip>')
    sys.exit()

TARGET_IP = sys.argv[1]

basic_scan = f'nmap -sV -sC -oN initial.nmap -vv {TARGET_IP}'
full_scan = f'nmap -sV -sC -oN all-ports.nmap -p- -vv {TARGET_IP}'

print('Starting basic scan...\n')
os.system(basic_scan)
print('Basic scan complete. Output file saved as \'initial.nmap\'.\n')

print('Starting full port scan in 10 seconds...')
time.sleep(5)
print('Starting full port scan in 5 seconds...')
time.sleep(5)

print('Starting full port scan...\n')
os.system(full_scan)
print('Full port scan complete...\n')
print('Basic port enumeration finished. Exiting...')
