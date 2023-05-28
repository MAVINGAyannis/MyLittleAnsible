import paramiko

def execute_command(ssh_client, command):
    try:
        stdin, stdout, stderr = ssh_client.exec_command("sudo " + command)
        output = []
        for line in stdout:
            line = line.strip()
            print(line)
            output.append(line)

        errors = stderr.read().decode()
        if errors:
            print("Error:")
            print(errors)

        return output
    except Exception as e:
        print("Failed to execute command:", e)
