#!/usr/bin/env python3

'''
This program is meant to emulate the effects of the linux command `ls -l`
'''

import os, stat
import datetime
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help='File path of the directory/file to be listed')
    return parser.parse_args()

def list_directory(p_path='.'):
    users = get_users()
    groups = get_groups()
    directory_list = os.scandir(p_path)
    for f in directory_list:
        stats = f.stat()
        print('{:10} {} {} {:5} {} {}'.format(stat.filemode(stats.st_mode), users[str(stats.st_uid)], groups[str(stats.st_gid)], stats.st_size, datetime.datetime.fromtimestamp(stats.st_mtime).strftime('%h %d %H:%M'), f.name))

def get_users():
    users = {}
    with open('/etc/passwd', 'r') as infile:
        for line in infile.readlines():
            users[line.split(':')[2]] = line.split(':')[0]
    return users

def get_groups():
    groups = {}
    with open('/etc/group', 'r') as infile:
        for line in infile.readlines():
            groups[line.split(':')[2]] = line.split(':')[0]
    return groups

args = parse_args()
if args.path:
    list_directory(args.path)
else:
    list_directory()
