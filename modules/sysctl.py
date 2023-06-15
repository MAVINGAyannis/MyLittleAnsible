from modules.exec_command import execute_command
from datetime import datetime
from logging_config import configure_logging
import logging

def sysctl(client, params, host_info):
    attribute = params.get('attribute')
    value = params.get('value')
    permanent = params.get('permanent')
    shell = "/bin/bash"

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    address = host_info.get('ssh_address')

    configure_logging()

    logging.info(dt_string + " host=" + address + " op=sysctl attribute=" + attribute + " value=" + str(value) + " permanent=" + str(permanent))
    if permanent:
        command = f'sudo grep -q "{attribute}" /etc/sysctl.conf && sudo sed -i "s/{attribute}.*/{attribute} = {value}/" /etc/sysctl.conf || echo "{attribute} = {value}" | sudo tee -a /etc/sysctl.conf > /dev/null'
    else:
        command = "sysctl " + attribute + "=" + str(value)

    if execute_command(client, command, "false", shell) == 1:
        logging.info(dt_string + " host=" + address + " op=sysctl status=CHANGED")
        execute_command(client, "sysctl -p", "false", shell)
    else:
        logging.info(dt_string + " host=" + address + " op=sysctl status=FAILED")
