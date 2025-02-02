import hashlib


def get_file_hash(file_path, algo="sha256"):
    """Calcule l'empreinte (hash) d'un fichier avec l'algorithme spécifié (par défaut SHA-256)."""
    hash_func = hashlib.new(algo)
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):  # Lire par blocs pour éviter une consommation excessive de RAM
            hash_func.update(chunk)
    return hash_func.hexdigest()
