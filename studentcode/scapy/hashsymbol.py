#!/usr/bin/env python3

import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('integer', metavar='X', nargs=1, type=int, help='Number of times to print the "#" symbol')
    return parser.parse_args()

def print_symbol(p_int):
    print(''.join("#" * p_int))

def out_symbol(p_int):
    sys.stdout.write('#' * p_int + '\n')

args = parse_args()
# print_symbol(args.integer[0])
out_symbol(args.integer[0])
