import hashlib, os
from tempfile import NamedTemporaryFile


def get_file_hash(file_path, algo="sha256"):
    """Calcule l'empreinte (hash) d'un fichier avec l'algorithme spécifié (par défaut SHA-256)."""
    hash_func = hashlib.new(algo)
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):  # Lire par blocs pour éviter une consommation excessive de RAM
            hash_func.update(chunk)
    return hash_func.hexdigest()


def save_temp_file(file) -> str:
    """Sauvegarde un fichier temporaire et retourne son chemin"""
    suffix = os.path.splitext(file.filename)[-1]
    temp_file = NamedTemporaryFile(delete=False, suffix=suffix)
    temp_file.write(file.file.read())
    temp_file.close()
    return temp_file.name
