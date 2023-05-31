from modules.copy import copy
from modules.apt import apt
from modules.service import service
from modules.template import template
from modules.command import command
from modules.sysctl import sysctl

def which_todos(client, todos_data, host_info):
    for todo in todos_data:
        module = todo.get('module')
        params = todo.get('params')

        if module == 'apt':
            apt(client, params)

        elif module == 'copy':
            copy(client, params, host_info)

        elif module == 'template':
            template(client, params)

        elif module == 'service':
            service(client, params)

        elif module == 'command':
            command(client, params)

        elif module == 'sysctl':
            sysctl(client, params)

        else:
            # Module inconnu
            print(f"Unknown module: {module}")
