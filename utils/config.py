# config.py
from dotenv import load_dotenv
from pathlib import Path
import os
import sys

# Chargement du .env à la racine du projet
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

# --- Fonctions utilitaires ---

def get_required(key: str) -> str:
    value = os.getenv(key)
    if value is None:
        print(f"[CONFIG ERROR] La variable {key} est requise mais absente.")
        sys.exit(1)
    return value

def get_bool(key: str, default: str = "false") -> bool:
    return os.getenv(key, default).lower() in ("true", "1", "yes")

def get_str(key: str, default: str = "") -> str:
    return os.getenv(key, default)

def get_int(key: str, default: int = 0) -> int:
    try:
        return int(os.getenv(key, str(default)))
    except ValueError:
        print(f"[CONFIG ERROR] La variable {key} doit être un entier.")
        sys.exit(1)

# --- Variables d'environnement accessibles globalement ---

MUSIC_BASE_PATH = get_required("MUSIC_BASE_PATH")
SCRIPT_DIR = get_required("SCRIPT_DIR")
REPORT_PATH = get_required("REPORT_PATH")

#LOGS
LOG_FILE_PATH = get_required("LOG_FILE_PATH")
LOG_ROTATION_DAYS = get_int("LOG_ROTATION_DAYS", 100)

#BEET
BEETS_CONFIG_MANUEL = get_required("BEETS_CONFIG_MANUEL")
BEETS_CONFIG_NORMAL = get_required("BEETS_CONFIG_NORMAL")
BEETS_CONFIG = get_required("BEETS_CONFIG")
BEETS_CONFIG_DIR = get_required("BEETS_CONFIG_DIR")
BEETS_BACKUP_DIR = get_str("BEETS_BACKUP_DIR", "./sav_base")
BEETS_LOGS = get_required("BEETS_LOGS")
BEETS_MANUAL_LIST = get_str("BEETS_MANUAL_LIST", "beets_manuel.txt")
BEETS_IMPORT_PATH = get_required("BEETS_IMPORT_PATH")
BEETS_RECAP_DIR = get_required("BEETS_RECAP_DIR")

EDM_GENRES = {"techno", "house", "trance", "edm", "dance", "psychedelic", "rave", "space"}
AUDIO_EXTENSIONS = {'.mp3', '.flac', '.wav', '.ogg', '.m4a', '.aac', '.alac', '.wma'}
IGNORED_EXTENSIONS = {
    '.jpg', '.jpeg', '.png', '.nfo', '.txt', '.log', '.cue',
    '.pdf', '.db', '.ini', '.url', '.sfv', '.m3u'
}

