import argparse
import yaml
import json
import paramiko
from paramiko import SSHConfig
import os

def parse_arguments():
    parser = argparse.ArgumentParser(description='Script to process inventory and todos')
    parser.add_argument('-i', '--inventory', help='Inventory file path')
    parser.add_argument('-f', '--todos', help='Todos file path')
    return parser.parse_args()

def read_yaml_file(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        return data

def write_json_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def establish_ssh_connection(host, port):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port=port)
        print(f'SSH connection established with {host}')
        # Effectuez ici les opérations nécessaires sur l'hôte distant
        # ...
    except paramiko.AuthenticationException:
        print(f'Authentication failed for {host}')
    except paramiko.SSHException as e:
        print(f'Error while establishing SSH connection with {host}: {str(e)}')
    finally:
        ssh.close()
        print(f'SSH connection closed with {host}')

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
    print('Contenu de l\'inventaire :')
    print(json.dumps(inventory_data, indent=4))

    # Conversion en JSON et écriture dans un fichier
    inventory_json_path = 'inventory.json'
    write_json_file(inventory_data, inventory_json_path)
    print(f'Inventaire converti en JSON et enregistré dans {inventory_json_path}')

    # Lecture du fichier de todos YAML
    todos_data = read_yaml_file(args.todos)
    print('Liste des todos :')
    print(json.dumps(todos_data, indent=4))

    # Conversion en JSON et écriture dans un fichier
    todos_json_path = 'todos.json'
    write_json_file(todos_data, todos_json_path)
    print(f'Liste de todos convertie en JSON et enregistrée dans {todos_json_path}')

    # Chargement de la configuration SSH par défaut
    ssh_config = SSHConfig()
    user_config_file = os.path.expanduser('~/.ssh/config')
    if os.path.exists(user_config_file):
        with open(user_config_file) as f:
            ssh_config.parse(f)

    # Établissement de la connexion SSH avec chaque hôte
    for host in inventory_data:
        # Récupération des paramètres de configuration SSH pour l'hôte
        ssh_config_host = ssh_config.lookup(host)
        if 'port' in ssh_config_host:
            port = int(ssh_config_host['port'])
        else:
            port = inventory_data[host].get('port', 22)

        establish_ssh_connection(host, port)
