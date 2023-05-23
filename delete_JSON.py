import os

def delete_JSON(inventory_json_path, todos_json_path):
    os.remove(inventory_json_path)
    os.remove(todos_json_path)
