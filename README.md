# Offline-Password-Cracker

### INTRODUCTION :
Offline-Password-Cracker est un simple script Python capable de retrouver un mot de passe d'après son hash.

### Usage :
       python PasswordCracker.py [-h]
       python PasswordCracker.py [-t TARGET] [-p PASSWORD] [-o OUTPUT] [-v] [-md5] [-sha1] [-sha256] [-sha512] [-u]
       
### Paramètres:
       [-h] Affiche l'aide.
       [-t] Obligatoire. Précède le fichier contenant la liste de hashs à traiter.
       [-p] Obligatoire. Précède le fichier contenant la wordlist custom à appliquer.
       [-o] Obligatoire. Précède le fichier dans lequel le résultat sera sauvegardé.
       [-v] Optionnel. Active le mode verbeux.
       [-md5] Optionnel. Les hashs sont tous au format md5.
       [-sha1] Optionnel. Les hashs sont tous au format sha1.
       [-sha256] Optionnel. Les hashs sont tous au format sha256.
       [-sha512] Optionnel. Les hashs sont tous au format sha512.
       [-u] Optionnel. Le format des hashs n'est pas identifié (defaut).
            Les hashs peuvent aussi être mélangés entre eux. 
            Attention : consomme plus de ressources.
       
### Exemples d'utilisation:
       python PasswordCracker.py -t hash.txt -p list.txt -o result.txt -md5
       python PasswordCracker.py -t hash.txt -p list.txt -o result.txt -v -sha256
       python PasswordCracker.py --target hash.txt --password list.txt --output result.txt --verbose --unknown
  
### Capacités :
Suporte actuellement le SHA1 - SHA254 - SHA512 - MD5

### Démonstration :
 ![Screenshot](https://github.com/HomardBoy/Offline-Password-Cracker/blob/master/Capture.PNG)
 Démonstration contre une liste de hashs réel :
 https://www.youtube.com/watch?v=HuS3uuI5p1w&feature=youtu.be

### Mise en forme des hashs :
Dans le but de tester l'efficacité du programme, il est nécessaire d'utiliser un grand nombre de hashs. La mise en forme de ces hashs peut parfois êtres très longue est fastidieuse, c'est pourquoi un script additionel est fournis pour mettre en forme les hashs avant de les analyser. (voir la vidéo démonstration).
