import os

print("--- DÉTECTEUR ET BLOQUEUR DE BRUTE-FORCE ---")

erreurs_par_ip = {}
limite_alerte = 3

try:
    with open("access.log", "r") as fichier:
        for ligne in fichier:
            elements = ligne.split()
            ip = elements[0]
            statut_http = elements[-1]

            if statut_http == "404":
                if ip in erreurs_par_ip:
                    erreurs_par_ip[ip] += 1
                else:
                    erreurs_par_ip[ip] = 1

    print("[*] Analyse terminée. Déclenchement de la défense...")
    
    for ip, nb_erreurs in erreurs_par_ip.items():
        if nb_erreurs >= limite_alerte:
            print(f"ALERTE : L'IP {ip} a généré {nb_erreurs} erreurs !")
            print(f"[*] Verrouillage du pare-feu en cours...")
            
            # C'est ici que Python envoie la commande à Linux
            commande = f"ufw deny from {ip}"
            os.system(commande)
            
            print(f"Cible neutralisée : L'IP {ip} est définitivement bloquée.")

except FileNotFoundError:
    print("[!] Erreur : Le fichier access.log est introuvable.")
