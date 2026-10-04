import getpass

print("OUTIL D'AUDIT DE MOT DE PASSE V5 (Édition RockYou)")
mdp = getpass.getpass("Entre un mot de passe à tester : ")

speciaux = "!@#$%^&*?+"
trouve_dans_rockyou = False

print("[*] Scan des 14 millions de mots de passe en cours... (0% de RAM utilisée)")

# Lecture "Ligne par ligne" (Économie totale de la mémoire)
try:
    with open("rockyou.txt", "r", encoding="latin-1") as fichier:
        for ligne in fichier:
            # On vérifie la ligne actuelle en retirant les espaces cachés
            if mdp == ligne.strip():
                trouve_dans_rockyou = True
                break # On arrête immédiatement de scanner pour gagner du temps !
except FileNotFoundError:
    print("[!] Erreur : Le fichier rockyou.txt est introuvable. As-tu fait le wget ?")

# Affichage des résultats
if trouve_dans_rockyou:
    print("DANGER EXTRÊME : Ce mot de passe est dans la base piratée RockYou !")
elif len(mdp) < 8:
    print("Faille critique : Mot de passe trop court.")
elif mdp.isalpha() or mdp.isnumeric():
    print("Attention : Il faut mélanger lettres ET chiffres.")
elif not any(char in speciaux for char in mdp):
    print("Vulnérabilité : Il manque au moins un caractère spécial.")
else:
    print("Robuste : Ton mot de passe est solide et introuvable dans RockYou !")
