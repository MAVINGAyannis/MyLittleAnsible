# MyLittleAnsible
MyLittleAnsible est un outil en ligne de commande développé en Python qui vous permet de configurer des hôtes distants en utilisant des fichiers de configuration YAML. Il s'inspire du concept d'Infrastructure as Code (IaC) et implémente un ensemble limité de fonctionnalités pour automatiser l'administration des serveurs.

## Caractéristiques
Connexion à des hôtes distants via le protocole SSH
Exécution de playbooks (todos.yml) avec une suite d'actions à effectuer sur les cibles
Implémentation de modules permettant de configurer les hôtes distants

## Installation

Clonez ce dépôt :

```
git clone https://github.com/MAVINGAyannis/MyLittleAnsible.git
```

Accédez au répertoire du projet :

```
cd MyLittleAnsible
```

Installez les dépendances requises :

```
pip install -r requirements.txt
```

## Utilisation

Exécutez le programme MyLittleAnsible en ligne de commande avec les arguments appropriés :

```
python3 mla -f todos.yml -i inventory.yml
```

L'option -f spécifie le fichier YAML contenant les tâches à exécuter (todos.yml).
L'option -i spécifie le fichier YAML contenant la définition des hôtes cibles (inventory.yml).

Le programme affichera les logs exploitables des actions effectuées.

## Exemple de fichier todos.yml

Voici un exemple de fichier todos.yml qui définit une liste de tâches à effectuer sur les hôtes distants :

```
module: apt
  params:
    name: nginx-common
    state: present

module: copy
  params:
    src: ./public
    dest: /var/www/public
    backup: false

module: template
  params:
    src: default.conf.j2
    dest: /etc/nginx/sites-enabled/default

module: service
  params:
    name: nginx
    state: started

module: service
  params:
    name: nginx
    state: enabled
```

Ce fichier contient des actions telles que l'installation d'un paquet APT, la copie de fichiers, le templating d'un fichier de configuration, et la gestion des services.

## Configuration de l'inventaire (inventory)

Le fichier inventory.yml permet de définir les hôtes cibles sur lesquels les tâches seront exécutées. Voici un exemple de structure de ce fichier :
```
hosts:
  webserver:
    ssh_address: 192.168.1.22
    ssh_port: 22
  bastion:
    ssh_address: 192.168.1.24
    ssh_port: 2222
```
Vous pouvez définir plusieurs hôtes avec leurs adresses IP, ports SSH, etc.

## Authentification SSH

MyLittleAnsible prend en charge trois méthodes d'authentification SSH :

Authentification par défaut, configurée via les fichiers ~/.ssh/.

Authentification par nom d'utilisateur et mot de passe, en spécifiant les attributs ssh_user et ssh_password dans la définition des cibles dans l'inventaire.

Authentification par clé privée, en spécifiant le chemin vers la clé privée avec l'attribut ssh_key dans la définition des cibles dans l'inventaire.

Assurez-vous de configurer l'authentification SSH appropriée dans le fichier inventory.yml en fonction de vos besoins.
