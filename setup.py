# fichier de convertion en executable

#importation de la bibliothèque après installation dans le cmd
from cx_Freeze import setup, Executable

# inclusion de notre fichier à convertir
base = None
executables = [Executable('calculater.py', base=base)]
packages = ['idna']

# instruction de building
options = {
    'build_exe': {
        'packages': packages,
    },
}

# configuration
setup(
    name='ma calculette',
    options=options,
    version="1.0",
    description='voici le rendu de mon executable',
    executables=executables
)