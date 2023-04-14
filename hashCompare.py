#!/usr/bin/env python3
# hashCompare.py - Take two command line arguments (hashes) and compare them
# to determine if they are the same.

import sys

if len(sys.argv) != 3:
    print('\nPlease provide the two hash values to compare.')
    sys.exit
else:
    hashOne = str(sys.argv[1])
    hashTwo = (sys.argv[2])
    if hashOne == hashTwo:
        print('\nHash values are the same.')
    else:
        print('\nHash values are different.')

print('Exiting...\n')
