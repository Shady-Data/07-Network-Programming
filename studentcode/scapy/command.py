#!/usr/bin/env python3

import subprocess
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--command', help='command tp be called and run')
    return parser.parse_args()

def parse_command(p_command):
    list_command = p_command.split(' ')
    return list_command

def run_command(p_command):
    command = parse_command(p_command)
    subprocess.call(command)

args = parse_args()

