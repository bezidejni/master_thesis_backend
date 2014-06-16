#!/usr/bin/sh
apt-get update
apt-get upgrade -y
apt-get install python-software-properties python python-setuptools -y
easy_install pip
pip install ansible
ansible-playbook -c local -i "[server]127.0.0.1," site.yml
