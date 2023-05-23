import argparse
from ssh_connect import connect_ssh_user, connect_ssh_key_file, connect_default
from yaml_to_json import read_yaml_file, write_json_file

def parse_arguments():
    parser = argparse.ArgumentParser(description='Script to process inventory and todos')
    parser.add_argument('-i', '--inventory', help='Inventory file path')
    parser.add_argument('-f', '--todos', help='Todos file path')
    return parser.parse_args()

# Point d'entrée du script
if __name__ == '__main__':
    args = parse_arguments()

    # Vérification des arguments
    if not args.inventory:
        print('Veuillez spécifier un fichier d\'inventaire avec le flag -i')
        exit(1)
    if not args.todos:
        print('Veuillez spécifier un fichier de todos avec le flag -f')
        exit(1)

    # Lecture du fichier d'inventaire YAML
    inventory_data = read_yaml_file(args.inventory)

    # Conversion en JSON et écriture dans un fichier
    inventory_json_path = 'inventory.json'
    write_json_file(inventory_data, inventory_json_path)

    # Lecture du fichier de todos YAML
    todos_data = read_yaml_file(args.todos)

    # Conversion en JSON et écriture dans un fichier
    todos_json_path = 'todos.json'
    write_json_file(todos_data, todos_json_path)

    # Lecture de chaque hôte
    for host, host_info in inventory_data['hosts'].items():
        print(f'Host: {host}')
        print(f'  ssh_address: {host_info["ssh_address"]}')
        print(f'  ssh_port: {host_info["ssh_port"]}')
        if 'ssh_user' in host_info and 'ssh_password' in host_info:
            connect_ssh_user(host_info['ssh_user'], host_info['ssh_password'], host_info["ssh_address"], host_info["ssh_port"])
        if 'ssh_key_file' in host_info:
            connect_ssh_key_file(host_info['ssh_key_file'], host_info["ssh_address"], host_info["ssh_port"])
        if 'ssh_user' not in host_info and 'ssh_key_file' not in host_info:
            connect_default(host_info["ssh_address"], host_info["ssh_port"])
