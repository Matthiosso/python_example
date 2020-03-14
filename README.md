# Exemple de projet Python


## Help ?

Voir [ici](https://dev.to/codemouse92/introducing-dead-simple-python-563o) pour les bonnes pratiques.

## Set up environment

```shell script
# Installer python
sudo apt install virtualenv python3-virtualenv python3-pip

# Installer la librairie de virtualenv
pip install virtualenv

# Voir les paquets actuellement installés
# pip freeze

# Se placer dans l'environnement virtuel
virtualenv -p python3 my-project-venv
source venv/bin/activate


# Pour quitter l'environnement virtuel
#deactivate

```


## Build

```shell script
# Installer les dépendances
pip install -r requirements.txt
```


### Start application

```shell script
python -m example
```


### Test application
```shell script
pytest
```


### Bonnes pratiques

> Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. 
> Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.
