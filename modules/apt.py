from modules.exec_command import execute_command
from datetime import datetime
from logging_config import configure_logging
import logging

def exec_apt(type, to_print, client, name):
    # Faire quelque chose pour le module apt
    command = "apt-get --yes " + type + " " + name
    status = execute_command(client, command, "false", "/bin/bash")

    if status == 401:
        logging.info("APT " + to_print + " : wrong command")

def apt(client, params, host_info):
    name = params.get('name')
    state = params.get('state', 'present')
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    address = host_info.get('ssh_address')

    configure_logging()

    logging.info(dt_string + " host=" + address + " op=apt name=" + name +  " state=" + state)

    if state == 'present':
        exec_apt("install", "INSTALL", client, name)
        logging.info(dt_string + " host=" + address + " op=apt status=OK")
    elif state == 'absent':
        exec_apt("remove", "REMOVE", client, name)
        logging.info(dt_string + " host=" + address + " op=apt status=CHANGED")