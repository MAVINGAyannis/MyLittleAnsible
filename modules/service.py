from modules.exec_command import execute_command
from datetime import datetime
from logging_config import configure_logging
import logging

def service(client, params, host_info):
    name = params.get('name')
    state = params.get('state')

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    address = host_info.get('ssh_address')

    configure_logging()

    logging.info(dt_string + " host=" + address + " op=service name=" + name +  " state=" + state)

    if state == 'started':
        command = "systemctl start " + name + ".service"
    elif state == 'restarted':
        command = "systemctl restart " + name + ".service"
    elif state == 'stopped':
        command = "systemctl stop " + name + ".service"
    elif state == 'enabled':
        command = "systemctl enable " + name + ".service"
    elif state == 'disabled':
        command = "systemctl disable " + name + ".service"
    else:
        logging.info("WRONG STATE")
    execute_command(client, command, "false", "/bin/bash")
    logging.info(dt_string + " host=" + address + " op=service status=CHANGED")
