import logging
import sys

configured = False


def configure_logging():
    global configured
    if not configured:
        # Configurer le logging
        logging.basicConfig(filename='logfile.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

        # Créer un gestionnaire de console et le configurer avec le même format de journal
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)

        # Ajouter le gestionnaire de console au logger de base
        logging.getLogger().addHandler(console_handler)

        configured = True
