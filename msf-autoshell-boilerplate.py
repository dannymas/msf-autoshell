#!/usr/bin/env python3

import re
import sys
import argparse
import netifaces
from IPython import embed
from lib.msfrpc import Msfrpc
from libnessus.parser import NessusParser
from netaddr import IPNetwork, AddrFormatError

def parse_args():
    '''
    Parse arguments
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--nessus", help="Nessus .nessus file")
    return parser.parse_args()

def check_for_args():
    '''
    Check for necessary arguments
    '''
    if not args.nessus:
        print('[-] Missing .nessus file')
        sys.exit('[-] Example: python autopwn.py -n /path/here/example_nessus_scan.nessus')

def main():
    print('[*] Entered main function')
    embed()

if __name__ == '__main__':
    args = parse_args() # This makes the 'args' variable global
    main()
