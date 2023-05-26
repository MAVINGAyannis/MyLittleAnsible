def apt(client, params):
    name = params.get('name')
    state = params.get('state')

    if state == 'present':
        # Faire quelque chose pour le module apt
        print(f"Module: apt, Name: {name}, State: {state}")