import argparse
import yaml
import json
import paramiko
from paramiko import SSHConfig
import os
import socket

def connect_ssh_user(host_info):
    print('  ssh_type: login')
    print(f'  ssh_user: {host_info["ssh_user"]}')
    print(f'  ssh_password: {host_info["ssh_password"]}')

    client = paramiko.SSHClient()
    client.load_system_host_keys()
    try:
        client.connect(host_info["ssh_address"],
                       port=host_info["ssh_port"],
                       username=host_info["ssh_user"],
                       password=host_info["ssh_password"],
                       look_for_keys=False)
        print("Connected successfully!")
    except Exception:
        print("Failed to establish connection.")
    finally:
        client.close()

def connect_ssh_key_file(key_file, address, port):
    print('  ssh_type: key')
    print(f'  ssh_key_file: {key_file}')

def connect_default(address, port, host_info):
    print('  ssh_type: default')
