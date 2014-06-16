#!/usr/bin/sh
apt-get update
apt-get upgrade -y
apt-get install python-software-properties python python-setuptools -y
easy_install pip
pip install ansible
ansible-playbook -m local -i local site.yml
