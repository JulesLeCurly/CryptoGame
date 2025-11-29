import json
import string

def sauvegarder_dictionnaire(dictionnaire, fichier):
    """Enregistre un dictionnaire dans un fichier JSON."""
    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(dictionnaire, f, indent=4, ensure_ascii=False)

def charger_dictionnaire(fichier):
    """Charge un dictionnaire à partir d'un fichier JSON."""
    with open(fichier, "r", encoding="utf-8") as f:
        return json.load(f)

def sauvegarder_valeur(valeur, fichier):
    """Enregistre une valeur dans un fichier texte."""
    with open(fichier, "w", encoding="utf-8") as f:
        f.write(str(valeur))

def charger_valeur(fichier):
    """Charge une valeur depuis un fichier texte."""
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            return f.read().strip()  # Supprime les espaces et sauts de ligne inutiles
    except FileNotFoundError:
        print("Erreur : fichier non trouvé.")
        return None

def encode_number(number: int) -> str:
    chars = string.ascii_letters + string.digits  # 26 lowercase + 26 uppercase + 10 digits = 62 characters
    base = len(chars)
    encoded = ""
    while number > 0:
        encoded = chars[number % base] + encoded
        number //= base
    return encoded or "0"

def decode_number(encoded: str) -> int:
    chars = string.ascii_letters + string.digits
    base = len(chars)
    decoded = 0
    for char in encoded:
        decoded = decoded * base + chars.index(char)
    return decoded