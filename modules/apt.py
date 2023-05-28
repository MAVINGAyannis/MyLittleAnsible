from modules.exec_command import execute_command

def apt(client, params):
    name = params.get('name')
    state = params.get('state')
    print(f"Module: apt, Name: {name}, State: {state}")

    if state == 'present':
        # Faire quelque chose pour le module apt
        command = "apt-get --yes install " + name
        status = execute_command(client, command)
        if status == 1:
            print("APT INSTALL : COMMAND EXECUTED")

        if status == 401:
            print("APT INSTALL : WRONG COMMAND")
    elif state == 'absent':
        command = "apt-get --yes remove " + name
        status = execute_command(client, command)
        if status == 1:
            print("APT REMOVE : COMMAND EXECUTED")

        if status == 401:
            print("APT REMOVE : WRONG COMMAND")