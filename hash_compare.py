'''
hash_compare.py - Take two command line arguments (hashes) and compare them
to determine if they are the same.
'''

import sys

if len(sys.argv) != 3:
    print('\nPlease provide the two hash values to compare.')
    sys.exit()
else:
    HASH_ONE = str(sys.argv[1])
    HASH_TWO = str(sys.argv[2])
    
    if HASH_ONE == HASH_TWO:
        print('\nHash values are the same.')
    else:
        print('\nHash values are different.')

print('Exiting...\n')
