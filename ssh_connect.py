import argparse
import yaml
import json
import paramiko
from paramiko import SSHConfig
import os
import socket
from modules.copy import copy
from modules.apt import apt
from modules.service import service
from modules.template import template
from which_todos import which_todos
from logging_config import configure_logging
import logging
from datetime import datetime

def connect_ssh_user(host_info, todos_data):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    configure_logging()

    try:
        client.connect(host_info["ssh_address"],
                       port=host_info["ssh_port"],
                       username=host_info["ssh_user"],
                       password=host_info["ssh_password"],
                       look_for_keys=False)
        which_todos(client, todos_data, host_info)
    except Exception:
        logging.info(dt_string + " Failed to establish connection.")
    finally:
        client.close()

def connect_ssh_key_file(key_file, address, port):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    configure_logging()

    logging.info('  ssh_type: key')
    logging.info('  ssh_key_file: {key_file}')

def connect_default(address, port, host_info):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    configure_logging()

    logging.info('  ssh_type: default')
