from modules.exec_command import execute_command

def exec_apt(type, to_print, client, name):
    # Faire quelque chose pour le module apt
    command = "apt-get --yes " + type + " " + name
    status = execute_command(client, command)
    if status == 1:
        print("APT " + to_print + " : COMMAND EXECUTED")

    if status == 401:
        print("APT " + to_print + " : WRONG COMMAND")

def apt(client, params):
    name = params.get('name')
    state = params.get('state')
    print(f"Module: apt, Name: {name}, State: {state}")

    if state == 'present':
        exec_apt("install", "INSTALL", client, name)
    elif state == 'absent':
        exec_apt("remove", "REMOVE", client, name)