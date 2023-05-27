import paramiko
import scp
from scp import SCPClient
import os

def copy(client, params, host_info):
    src = params.get('src')
    dest = params.get('dest')
    backup = params.get('backup')

    # Vérifier si src est un fichier ou un dossier
    if os.path.isfile(src):
        # Copier un fichier
        try:
            scp = SCPClient(client.get_transport())
            scp.put(src, dest)
            scp.close()
            print(f"File copied: {src} -> {dest}")
        except Exception as e:
            print(f"Error copying file: {e}")
    elif os.path.isdir(src):
        # Copier un dossier (récursivement)
        try:
            scp = SCPClient(client.get_transport())
            scp.put(src, remote_path=dest, recursive=True)
            scp.close()
            print(f"Folder copied: {src} -> {dest}")
        except Exception as e:
            print(f"Error copying folder: {e}")
    else:
        print(f"Source path is invalid or does not exist: {src}")
