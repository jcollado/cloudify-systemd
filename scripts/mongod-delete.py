#!/usr/bin/env python

import subprocess

if __name__ == '__main__':
    subprocess.check_call([
        'yum',
        '-y',
        '-q',
        'erase',
        'mongodb-org',
    ])
    print('MongoDB uninstalled')
