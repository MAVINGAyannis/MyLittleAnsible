def connect_ssh_user(user, password, address, port):
    print('  ssh_type: login')
    print(f'  ssh_user: {user}')
    print(f'  ssh_password: {password}')

def connect_ssh_key_file(key_file, address, port):
    print('  ssh_type: key')
    print(f'  ssh_key_file: {key_file}')

def connect_default(address, port):
    print('  ssh_type: default')
