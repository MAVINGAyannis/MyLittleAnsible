from modules.exec_command import execute_command
from datetime import datetime

def command(client, params, host_info):
    name = params.get('name')
    command = params.get('command')
    shell = "/bin/bash"

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    address = host_info.get('ssh_address')

    if 'shell' in params:
        shell = params['shell']

    print(dt_string + " - ROOT - INFO - host=" + address + " op=command name=" + command)
    status = execute_command(client, command, "false", shell)
    if status == 1:
        print(dt_string + " - ROOT - INFO - host=" + address + " op=command status=OK")
    if status == 401:
        print(dt_string + " - ROOT - INFO - host=" + address + " op=command status=FAILED")
