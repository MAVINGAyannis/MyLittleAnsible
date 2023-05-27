import paramiko
import scp
from scp import SCPClient
import os

def copy(client, params, host_info):
    src = params.get('src')
    dest = params.get('dest')
    backup = params.get('backup', False)

    # Vérifier si src est un fichier ou un dossier
    if os.path.isfile(src):
        # Copier un fichier
        try:
            if backup:
                # Ajouter un suffixe au nom du fichier pour la sauvegarde
                backup_dest = dest + '.backup'
                scp = SCPClient(client.get_transport())
                scp.get(dest, backup_dest)
                scp.close()
                print(f"Backup created: {dest} -> {backup_dest}")

            # Copier le nouveau fichier
            scp = SCPClient(client.get_transport())
            scp.put(src, dest)
            scp.close()
            print(f"File copied: {src} -> {dest}")
        except Exception as e:
            print(f"Error copying file: {e}")
    elif os.path.isdir(src):
        # Copier un dossier (récursivement)
        try:
            if backup:
                # Ajouter un suffixe au nom du dossier pour la sauvegarde
                backup_dest = os.path.join(dest, os.path.basename(src)) + '.backup'
                scp = SCPClient(client.get_transport())
                scp.get(dest, backup_dest)
                scp.close()
                print(f"Backup created: {dest} -> {backup_dest}")

            # Copier le nouveau dossier
            scp = SCPClient(client.get_transport())
            scp.put(src, recursive=True, remote_path=dest)
            scp.close()
            print(f"Folder copied: {src} -> {dest}")
        except Exception as e:
            print(f"Error copying folder: {e}")
    else:
        print(f"Source path is invalid or does not exist: {src}")
