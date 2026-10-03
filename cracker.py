import hashlib

print("--- CRACKER DE HASH SHA-256 (Moteur Python) ---")
# Le SHA-256 attend un hash plus long (64 caractères hexadécimaux)
hash_cible = input("Entre le Hash SHA-256 à casser : ").strip().lower()

print("[*] Démarrage du moteur SHA-256... (0% RAM)")

mot_de_passe_trouve = None

try:
    with open("rockyou.txt", "r", encoding="latin-1") as fichier:
        for ligne in fichier:
            mot_clair = ligne.strip()
            
            # On change simplement md5 par sha256 ici !
            hash_test = hashlib.sha256(mot_clair.encode('latin-1')).hexdigest()
            
            if hash_test == hash_cible:
                mot_de_passe_trouve = mot_clair
                break
                
except FileNotFoundError:
    print("[!] Erreur : rockyou.txt introuvable.")

if mot_de_passe_trouve:
    print(f"\n✅ BINGO ! L'empreinte SHA-256 a été cassée. Le mot de passe est : {mot_de_passe_trouve}")
else:
    print("\n❌ Échec : Le mot de passe n'est pas dans le dictionnaire.")
