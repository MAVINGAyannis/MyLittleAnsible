from arguments.yaml_to_json import read_yaml_file, write_json_file
from arguments.arguments import parse_arguments, check_arguments
from arguments.delete_JSON import delete_JSON
from process_hosts import process_hosts
import json
from datetime import datetime

# Point d'entrée du script
if __name__ == '__main__':
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    args = parse_arguments()

    # Vérification des arguments
    check_arguments(args)

    # Lecture du fichier d'inventaire YAML
    inventory_data = read_yaml_file(args.inventory)

    # Conversion en JSON et écriture dans un fichier
    write_json_file(inventory_data, 'inventory.json')

    # Lecture du fichier de todos YAML
    todos_data = read_yaml_file(args.todos)

    # Conversion en JSON et écriture dans un fichier
    write_json_file(todos_data, 'todos.json')

    # Charger le fichier JSON d'inventaire
    with open('inventory.json') as f:
        inventory = json.load(f)

    # Récupérer le nombre d'hôtes
    num_hosts = len(inventory['hosts'])

    # Récupérer une liste d'adresses IP
    ip_list = [host_info['ssh_address'] for host_info in inventory['hosts'].values()]

    print(dt_string + " - ROOT - INFO - proccessing " + str(num_hosts) + " task(s) on hosts: " + str(ip_list))

    # Traitement des hôtes
    process_hosts(inventory_data, todos_data)

    print(dt_string + " - ROOT - INFO - done processing tasks for hosts: " + str(ip_list))

    # Suppression des fichiers JSON
    delete_JSON('inventory.json', 'todos.json')
