#!/usr/bin/env python

import subprocess

REPO_FILENAME = '/etc/yum.repos.d/mongodb.repo'
REPO_TEMPLATE = """
[mongodb]
name=MongoDB Repository
baseurl=http://downloads-distro.mongodb.org/repo/redhat/os/x86_64/
gpgcheck=0
enabled=1
"""


def generate_repo_file():
    """Generate repo file to be able to get mongodb."""
    with open(REPO_FILENAME, 'w') as repo_file:
        repo_file.write(REPO_TEMPLATE)


if __name__ == '__main__':
    try:
        subprocess.check_call(['yum', 'list', 'installed', 'mongodb-org'])
    except subprocess.CalledProcessError:
        generate_repo_file()
        subprocess.check_call(['yum', '-y', 'update'])
        subprocess.check_call([
            'yum',
            '-y',
            '-q',
            'install',
            'mongodb-org',
        ])

        # Listen to remote connections
        subprocess.check_call([
            'sed',
            '-i',
            's/bind_ip=127.0.0.1/#&/',
            '/etc/mongod.conf',
        ])

        print('MongoDB installed')
    else:
        print('MongoDB is already installed')
