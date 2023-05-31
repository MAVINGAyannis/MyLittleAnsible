from modules.exec_command import execute_command

def service(client, params):
    name = params.get('name')
    state = params.get('state')

    if state == 'started':
        # Faire quelque chose pour le module service (state: started)
        print(f"Module: service, Name: {name}, State: {state}")
        command = "systemctl start " + name + ".service"
        print(command)
    elif state == 'restarted':
        # Faire quelque chose pour le module service (state: enabled)
        print(f"Module: service, Name: {name}, State: {state}")
        command = "systemctl restart " + name + ".service"
    elif state == 'stopped':
        # Faire quelque chose pour le module service (state: enabled)
        print(f"Module: service, Name: {name}, State: {state}")
        command = "systemctl stop " + name + ".service"
    elif state == 'enabled':
        # Faire quelque chose pour le module service (state: enabled)
        print(f"Module: service, Name: {name}, State: {state}")
        command = "systemctl enable " + name + ".service"
    elif state == 'disabled':
        # Faire quelque chose pour le module service (state: enabled)
        print(f"Module: service, Name: {name}, State: {state}")
        command = "systemctl disable " + name + ".service"
    else:
        print("WRONG STATE")
    print("SERVICE : " + state)
    execute_command(client, command, "false", "/bin/bash")
