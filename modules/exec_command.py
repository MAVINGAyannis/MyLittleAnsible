import paramiko

def execute_command(ssh_client, command, do_print, shell):
    try:
        stdin, stdout, stderr = ssh_client.exec_command("sudo " + command)
        output = []
        for line in stdout:
            line = line.strip()
            # "line" contient la ligne de sortie
            if do_print == "true":
                print(line)
            output.append(line)

        errors = stderr.read().decode()
        if errors:
            # "errors" contient la ligne d'erreur
            if do_print == "true":
                print(errors)

        return 1
    except Exception as e:
        # "e" contient la commande défectueuse
        return 401
