from modules.exec_command import execute_command
from datetime import datetime

def exec_apt(type, to_print, client, name):
    # Faire quelque chose pour le module apt
    command = "apt-get --yes " + type + " " + name
    status = execute_command(client, command, "false", "/bin/bash")

    if status == 401:
        print("APT " + to_print + " : wrong command")

def apt(client, params, host_info):
    name = params.get('name')
    state = params.get('state', 'present')
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    address = host_info.get('ssh_address')

    print(dt_string + " - ROOT - INFO - host=" + address + " op=apt name=" + name +  " state=" + state)

    if state == 'present':
        exec_apt("install", "INSTALL", client, name)
        print(dt_string + " - ROOT - INFO - host=" + address + " op=apt status=OK")
    elif state == 'absent':
        exec_apt("remove", "REMOVE", client, name)
        print(dt_string + " - ROOT - INFO - host=" + address + " op=apt status=CHANGED")