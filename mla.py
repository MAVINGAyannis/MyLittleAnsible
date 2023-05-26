from yaml_to_json import read_yaml_file, write_json_file
from arguments import parse_arguments, check_arguments
from delete_JSON import delete_JSON
from process_hosts import process_hosts

# Point d'entrée du script
if __name__ == '__main__':
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

    # Traitement des hôtes
    process_hosts(inventory_data, todos_data)

    # Suppression des fichiers JSON
    delete_JSON('inventory.json', 'todos.json')
