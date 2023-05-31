from modules.exec_command import execute_command

def sysctl(client, params):
    attribute = params.get('attribute')
    value = params.get('value')
    permanent = params.get('permanent')
    shell = "/bin/bash"
    print(f"Module: sysctl, Attribute: {attribute}, Value: {value}, Permanent : {permanent}")

    if permanent:
        command = f'sudo grep -q "{attribute}" /etc/sysctl.conf && sudo sed -i "s/{attribute}.*/{attribute} = {value}/" /etc/sysctl.conf || echo "{attribute} = {value}" | sudo tee -a /etc/sysctl.conf > /dev/null'
    else:
        command = "sysctl " + attribute + "=" + str(value)

    if execute_command(client, command, "false", shell) == 1:
        print("SYCTL MODIFICATION : valid")
        execute_command(client, "sysctl -p", "false", shell)
    else:
        print("SYSCTL MODIFICATION : error")
