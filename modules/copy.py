import paramiko

def copy(client, params, host_info):
    src = params.get('src')
    dest = params.get('dest')
    backup = params.get('backup')

    print(f"Module: copy, Src: {src}, Dest: {dest}, Backup: {backup}")

    try:
        sftp = client.open_sftp()

        # Vérifier si la sauvegarde est activée
        if backup:
            # Chemin de sauvegarde (ajouter un timestamp au nom du fichier)
            backup_dest = dest + '.bak'
            sftp.rename(dest, backup_dest)

        # Copier le fichier vers la destination distante
        sftp.put(src, dest)
        print("Fichier copié avec succès.")
    except Exception as e:
        print("Erreur lors de la copie du fichier:", str(e))
    finally:
        if sftp:
            sftp.close()
