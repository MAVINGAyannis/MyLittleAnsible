from modules.exec_command import execute_command

def apt(client, params):
    name = params.get('name')
    state = params.get('state')

    if state == 'present':
        # Faire quelque chose pour le module apt
        command = "apt-get --yes install " + name
        execute_command(client, command)
    elif state == 'absent':
        command = "apt-get --yes remove " + name
        execute_command(client, command)