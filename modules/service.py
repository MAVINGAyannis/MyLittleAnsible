from modules.exec_command import execute_command

def service(client, params):
    name = params.get('name')
    state = params.get('state')

    if state == 'started':
        print(f"Module: service, Name: {name}, State: {state}")
        command = "systemctl start " + name + ".service"
    elif state == 'restarted':
        print(f"Module: service, Name: {name}, State: {state}")
        command = "systemctl restart " + name + ".service"
    elif state == 'stopped':
        print(f"Module: service, Name: {name}, State: {state}")
        command = "systemctl stop " + name + ".service"
    elif state == 'enabled':
        print(f"Module: service, Name: {name}, State: {state}")
        command = "systemctl enable " + name + ".service"
    elif state == 'disabled':
        print(f"Module: service, Name: {name}, State: {state}")
        command = "systemctl disable " + name + ".service"
    else:
        print("WRONG STATE")
    print("SERVICE : " + state)
    execute_command(client, command, "false", "/bin/bash")
