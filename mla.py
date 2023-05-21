import argparse
import yaml
import json
import paramiko
from paramiko import SSHConfig
import os
import socket

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
        ssh.connect(hostname=host, port=port, timeout=5)  # Ajout du paramètre timeout
        print(f'SSH connection established with {host}')
        # Effectuez ici les opérations nécessaires sur l'hôte distant
        # ...
    except paramiko.AuthenticationException:
        print(f'Authentication failed for {host}')
    except paramiko.SSHException as e:
        print(f'Error while establishing SSH connection with {host}: {str(e)}')
    except socket.timeout:
        print(f'Timeout while establishing SSH connection with {host}')
    except socket.gaierror as e:
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

    # Conversion en JSON et écriture dans un fichier
    inventory_json_path = 'inventory.json'
    write_json_file(inventory_data, inventory_json_path)

    # Lecture du fichier de todos YAML
    todos_data = read_yaml_file(args.todos)

    # Conversion en JSON et écriture dans un fichier
    todos_json_path = 'todos.json'
    write_json_file(todos_data, todos_json_path)

    # Chargement de la configuration SSH par défaut
    ssh_config = SSHConfig()
    user_config_file = os.path.expanduser('~/.ssh/config')
    if os.path.exists(user_config_file):
        with open(user_config_file) as f:
            ssh_config.parse(f)

    # Établissement de la connexion SSH avec chaque hôte
    for host, host_info in inventory_data['hosts'].items():
        address = host_info.get('ssh_address')
        port = host_info.get('ssh_port', 22)
        print(address, port)

        if address:
            establish_ssh_connection(address, port)
        else:
            print(f'SSH address not found for host {host}')