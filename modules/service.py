def service(client, params):
    name = params.get('name')
    state = params.get('state')

    if state == 'started':
        # Faire quelque chose pour le module service (state: started)
        print(f"Module: service, Name: {name}, State: {state}")

    elif state == 'enabled':
        # Faire quelque chose pour le module service (state: enabled)
        print(f"Module: service, Name: {name}, State: {state}")
