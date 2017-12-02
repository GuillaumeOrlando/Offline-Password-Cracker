# Offline-Password-Cracker

### INTRODUCTION :
Offline-Password-Cracker est un simple script Python capable de retrouver un mot de passe d'après son hash.

### Usage :
       python PasswordCracker.py [-h]
       python PasswordCracker.py [-t TARGET] [-p PASSWORD] [-o OUTPUT] [-v]
       
### Paramètres:
       [-h] Affiche l'aide.
       [-t] Obligatoire. Précède le fichier contenant la liste de hashs à traiter.
       [-p] Obligatoire. Précède le fichier contenant la wordlist custom à appliquer.
       [-o] Obligatoire. Précède le fichier dans lequel le résultat sera sauvegardé.
       [-v] Optionnel. Active le mode verbeux.
       
### Exemples d'utilisation:
       python PasswordCracker.py -t hash.txt -p list.txt -o result.txt
       python PasswordCracker.py -t hash.txt -p list.txt -o result.txt -v
       python PasswordCracker.py --target hash.txt --password list.txt --output result.txt --verbose
  
### Capacités :
Suporte actuellement le SHA1 - SHA254 - SHA512 - MD5

### Démonstration :
 ![Screenshot](https://github.com/HomardBoy/Offline-Password-Cracker/blob/master/git2.PNG)
 ![Screenshot](https://github.com/HomardBoy/Offline-Password-Cracker/blob/master/git1.PNG)

