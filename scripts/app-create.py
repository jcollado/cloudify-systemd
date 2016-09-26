#!/usr/bin/env python

import subprocess

if __name__ == '__main__':
    try:
        subprocess.check_call(['yum', 'list', 'installed', 'python-flask'])
    except subprocess.CalledProcessError:
        subprocess.check_call([
            'yum',
            '-y',
            '-q',
            'install',
            'python-flask',
        ])
        print('Flask installed')
    else:
        print('Flask is already installed')
