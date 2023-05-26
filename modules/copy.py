def copy(client, params):
    src = params.get('src')
    dest = params.get('dest')
    backup = params.get('backup')

    print(f"Module: copy, Src: {src}, Dest: {dest}, Backup: {backup}")