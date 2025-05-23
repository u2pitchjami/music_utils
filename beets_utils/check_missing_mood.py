from datetime import datetime
from music_utils import get_beet_list
from utils.logger import get_logger


def check_missing_moods():
    logger = get_logger("Check_Beets_Mood")
    logger.info(f"🧠 CHECK MOOD BEETS : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    logger.info("--- (identifie les morceaux sans champ `mood` dans Beets) ---")

    # Requête : mood vide ou non défini
    lines = get_beet_list(
        query="mood::^$",
        format=True,
        format_fields="$id|$path",
        logname="Check_Beets_Mood"
    )

    if not lines:
        logger.info("🎉 Tous les morceaux ont un champ mood défini.")
        return

    logger.info(f"🟡 Nombre de morceaux sans mood : {len(lines)}")

    # Extraction et affichage des chemins/id
    for line in lines:
        try:
            beet_id, path = [p.strip() for p in line.split("|")]
            logger.info(f" - ID: {beet_id} | {path}")
        except ValueError:
            logger.warning(f"Ligne mal formatée : {line}")

    logger.info("🏁 CHECK MOOD BEETS : TERMINE \n")
