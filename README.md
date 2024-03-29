# FICHIER-EXECUTABLE-PYTHON
dans ce repository je détails comment créer  un executable en python
Voici quelques méthodes pour y parvenir :
Avec cx_Freeze:
I.	Prérequis
Assurez-vous d’avoir de la connexion
1-Assurez-vous d’avoir Python installé sur votre machine.   https://www.python.org/downloads/windows/
2-ouvrir votre éditeur de code (vscode) https://code.visualstudio.com/Download
3-céer un dossier ‘EXECUTABLE	‘ sur votre bureau 
4-ouvrez ce dossier avec votre éditeur de code 
5-créer le  fichier nommé (calculater.py) dans le même dossier que (calculater.py) très important, qui va contenir le script de python de calculatrice en fessant
             - Ctrl+N,
- Ctrl+S,
-Entrée
-puis placer ce fichier dans le dossier que vous venez de créer (EXECUTABLE)
6- créer le  fichier (setup.py)  qui va contenir le script de python conversion du fichier ‘calculateur.py’ en exécutable (.exe)
II.	LE CODAGE
1.	ouvrez votre invite de commande en fessant 
-Windows +R
-taper (cmd)
-Entrée

2.	Installez le module cx_Freeze en utilisant la commande :      
             pip install cx_Freeze 
(Patientez que toutes les installations requis puis être terminer)

3.	Telechargez le code source du programme de calculatrice sur mon git hub puis coller le code dans votre fichier ‘calculater.py’
4.	Telechargez le code de setup sur mon git hub puis coller le code dans votre fichier setup.py

NB : si vous utiliser la version la plus ressente de python qui est 3.12.2 il aura un petit problème de mise à jour au niveau du package ‘idna’ mais ne vous inquiétez pas j’ai la solution, il faut le mettre à jour en tapant ce code dans votre invite de commande

- pip install --upgrade cx_Freeze

Et en fin exécutez la commande suivante dans l’invite de commande pour générer l’exécutable : python setup.py build.
L’exécutable sera créé dans le dossier "build" du répertoire de votre programme.
Vous n’aurez qu’à ouvrir le dossier build, puis vous verrez un fichier avec l’extension .exe
C’est votre exécutable pour pouvez double cliquer dessus pour l’exécuter et le partager à vos amies sans qu’ils sont accès à votre code source


NB : si vous êtes satisfait, faites preuve de bonté en vous abonnent a ma chaine YouTube et liker mes vidéos.
Merci et on retrouve la prochaine pour un autre projet.

https://youtube.com/@NK2DCoding-City?si=KxLgtj6kL0F4Nb7y

En cas d'incompréhension de quelque chose n'existez surtout pas à me le faire savoir soit
Mon site web ----https://nk2d-coding-city.000webhostap... 
Communauté développeur --------------------------https://chat.whatsapp.com/gbqxpnrhjid...
Abonnez-vous ici -------------------------- https://youtube.com/@nk2dcoding-city?... 
Mon site web : https://nk2d-coding-city.000webhostap... 
Téléphone : +225 054 470 485 4 - https://wa.me/+2250544704854 
Facebook :    / nk2d.codingcity   
Télégramme : https://t.me/+8vogh2gxng1kywzk
