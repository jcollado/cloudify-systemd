#!/usr/bin/env python

import os

SERVICE_TEMPLATE = """
[Unit]
Description={service_name}

[Service]
ExecStart={service_binary_path}
"""


def generate_service_file():
    """Generate service fie to be able to run application using systemctl."""
    service_name = os.environ['service_name']
    service_filename = (
        '/lib/systemd/system/{}.service'.format(service_name)
    )
    with open(service_filename, 'w') as service_file:
        service_file.write(
            SERVICE_TEMPLATE.format(
                service_name=service_name,
                service_binary_path=service_binary_path,
            )
        )
        print('Generated service file for: {}'.format(service_name))


if __name__ == '__main__':
    service_binary_path = os.environ['service_binary_path']

    if service_binary_path != 'None':
        generate_service_file()
