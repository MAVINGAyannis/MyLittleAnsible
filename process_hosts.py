from ssh_connect import connect_ssh_user, connect_ssh_key_file, connect_default

def process_hosts(inventory_data):

    # Lecture de chaque hôte
    for host, host_info in inventory_data['hosts'].items():

        print(f'Host: {host}')
        print(f'  ssh_address: {host_info["ssh_address"]}')
        print(f'  ssh_port: {host_info["ssh_port"]}')

        if 'ssh_user' in host_info and 'ssh_password' in host_info:
            connect_ssh_user(host_info)
        if 'ssh_key_file' in host_info:
            connect_ssh_key_file(host_info['ssh_key_file'], host_info["ssh_address"], host_info["ssh_port"])
        if 'ssh_user' not in host_info and 'ssh_key_file' not in host_info:
            connect_default(host_info["ssh_address"], host_info["ssh_port"], host_info)
