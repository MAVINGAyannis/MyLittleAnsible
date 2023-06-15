from logging_config import configure_logging
import logging

def template(client, params):
    src = params.get('src')
    dest = params.get('dest')

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    address = host_info.get('ssh_address')

    configure_logging()

    # Faire quelque chose pour le module template
    logging.info("Module: template, Src: {src}, Dest: {dest}")