import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Script to process inventory and todos')
    parser.add_argument('-i', '--inventory', help='Inventory file path')
    parser.add_argument('-f', '--todos', help='Todos file path')
    return parser.parse_args()

def check_arguments(args):
    if not args.inventory:
        print('Veuillez spécifier un fichier d\'inventaire avec le flag -i')
        exit(1)
    if not args.todos:
        print('Veuillez spécifier un fichier de todos avec le flag -f')
        exit(1)
