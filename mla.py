import argparse
import yaml
import json

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

    # Lecture du fichier d'inventaire
    inventory_data = read_yaml_file(args.inventory)
    print('Contenu de l\'inventaire :')
    print(inventory_data)

    # Conversion en JSON et écriture dans un fichier
    inventory_json_path = 'inventory.json'
    write_json_file(inventory_data, inventory_json_path)
    print(f'Inventaire converti en JSON et enregistré dans {inventory_json_path}')

    # Lecture du fichier de todos
    todos_data = read_yaml_file(args.todos)
    print('Liste des todos :')
    print(todos_data)

    # Conversion en JSON et écriture dans un fichier
    todos_json_path = 'todos.json'
    write_json_file(todos_data, todos_json_path)
    print(f'Liste de todos convertie en JSON et enregistrée dans {todos_json_path}')
