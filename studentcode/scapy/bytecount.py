#!/usr/bin/env python3

import os

def get_bytecount():
    process = os.popen('./ll.py -p '+ os.getcwd())
    # print(len('{!s}'.format(process.read())))
    print(len(process.read()))

get_bytecount()
