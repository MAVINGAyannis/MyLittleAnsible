from modules.exec_command import execute_command
from datetime import datetime
from logging_config import configure_logging
import logging

def command(client, params, host_info):
    name = params.get('name')
    command = params.get('command')
    shell = "/bin/bash"

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    address = host_info.get('ssh_address')

    configure_logging()

    if 'shell' in params:
        shell = params['shell']

    logging.info(dt_string + " host=" + address + " op=command name=" + command)
    status = execute_command(client, command, "false", shell)
    if status == 1:
        logging.info(dt_string + " host=" + address + " op=command status=OK")
    if status == 401:
        logging.info(dt_string + " host=" + address + " op=command status=FAILED")
