#!/usr/bin/sh -e
systemctl stop ${service_name}
echo "${service_name} stopped"
