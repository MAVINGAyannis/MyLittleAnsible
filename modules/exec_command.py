import paramiko

def execute_command(ssh_client, command):
    try:
        stdin, stdout, stderr = ssh_client.exec_command("sudo " + command)
        output = []
        for line in stdout:
            line = line.strip()
            # "line" contient la ligne de sortie
            output.append(line)

        errors = stderr.read().decode()
        if errors:
            # "errors_line" contient la ligne d'erreur
            errors_line = errors

        return 1
    except Exception as e:
        # "e" contient la commande défectueuse
        return 401
