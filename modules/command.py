from modules.exec_command import execute_command

def command(client, params):
    name = params.get('name')
    command = params.get('command')
    shell = "/bin/bash"

    if 'shell' in params:
        shell = params['shell']

    print(f"Module: command, Name: {name}, Command: {command}")
    status = execute_command(client, command, "false", shell)
    if status == 1:
        print("COMMAND : EXECUTED")
    if status == 401:
        print("COMMAND : WRONG COMMAND")
