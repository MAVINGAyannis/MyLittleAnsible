import argparse
import yaml
import json
import paramiko
from paramiko import SSHConfig
import os
import socket
from modules.exec_command import execute_command
from modules.copy import copy
from modules.apt import apt
from modules.service import service
from modules.template import template

def which_todos(client, todos_data):
    for todo in todos_data:
        module = todo.get('module')
        params = todo.get('params')

        if module == 'apt':
            apt(client, params)

        elif module == 'copy':
            copy(client, params)

        elif module == 'template':
            template(client, params)

        elif module == 'service':
            service(client, params)
        else:
            # Module inconnu
            print(f"Unknown module: {module}")


def connect_ssh_user(host_info, todos_data):
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
        output = execute_command(client, "ls -l")
        which_todos(client, todos_data)
    except Exception:
        print("Failed to establish connection.")
    finally:
        client.close()

def connect_ssh_key_file(key_file, address, port):
    print('  ssh_type: key')
    print(f'  ssh_key_file: {key_file}')

def connect_default(address, port, host_info):
    print('  ssh_type: default')
