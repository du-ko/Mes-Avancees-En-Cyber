# Mes Avancées En Cyber (Projet d'apprentissage personnel)

Ce dépôt contient mes scripts et expérimentations réseau et système, réalisés sous Xubuntu.

## Outils et concepts explorés :
* Reconnaissance : Scan réseau et analyse d'en-têtes HTTP (Nmap, curl, tcpdump).
* Audit de mots de passe : check_mdp.py (Script de validation optimisé avec RockYou).
* Offensif : cracker.py (Moteur de crackage de hash MD5/SHA-256 en Python).
* Défensif : detect_scan.py (Analyseur de logs et IPS communiquant avec le pare-feu UFW).
* Stéganographie : Dissimulation de données dans le fichier image_avec_txt_dissimule.jpg via Steghide.
* Accès Initial : Simulation de Reverse Shell local pour la prise de contrôle d'un terminal via Netcat et Bash.
* Escalade de Privilèges (PrivEsc) : Exploitation d'un binaire Bash mal configuré (bit SUID).
  * Note technique : Analyse et contournement de la protection de montage `nosuid` du répertoire `/tmp` en relocalisant le vecteur d'attaque dans un environnement non restreint.
