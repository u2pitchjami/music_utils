#!/usr/bin/env python3
import datetime
import subprocess
import sys
import os
from utils.logger import get_logger
from utils.config import SCRIPT_DIR
import shlex
import logging

get_logger("music_utils")
logger = logging.getLogger("music_utils")
# logger = get_logger("music_utils")
# print(f"logger hub : {logger}")
def run_python_script(script_name, args: str = ""):
    try:
        full_path = os.path.join(SCRIPT_DIR, script_name)
        logger.info(f"▶️ Exécution de {script_name} {args}")

        # Transforme la chaîne d'arguments en liste (comme le shell)
        cmd = [sys.executable, full_path] + shlex.split(args)

        subprocess.run(cmd, check=True)
        logger.info(f"🌞 Succès : {script_name}")
    except subprocess.CalledProcessError as e:
        logger.error(f"🚨 Erreur lors de l'exécution de {script_name} : {e}")

def main():
    today = datetime.date.today()
    weekday = today.weekday()  # 0 = lundi, 6 = dimanche
    day = today.day
    logger.info(f"📅 MUSIC UTILS CRONHUB : {day} {datetime.datetime.now().strftime('%d-%m-%Y')}")
    # Chaque jour
    run_python_script("backup_beets_config.py")
    run_python_script("beets_recap.py", "--period all")
    run_python_script("check_random_bad_albums.py", "--n 10")
    
    # Conditions
    if weekday == 0: #lundi
        run_python_script("check_and_fix_edm_metadata.py")
    
    if weekday == 1: #mardi
        run_python_script("check_mb_albumid.py")
        run_python_script("check_missing_album_paths.py")
    
    if weekday == 2: #mercredi
        run_python_script("clean_empty_music_dirs.py", "--delete")
        run_python_script("detect_beets_album_duplicates.py")
        
    if weekday == 3: #jeudi
        run_python_script("sync_mb_metadata.py")
               
    if weekday == 5: #samedi
        run_python_script("check_and_fix_edm_metadata.py")
    if weekday == 6: #dimanche
        run_python_script("clean_empty_music_dirs.py", "--delete")
        run_python_script("beets_recap.py", "--period week --markdown")

    if day == 1:
        run_python_script("beet_recap.py", "--period month --markdown")
        
    if day == 15:
        run_python_script("check_random_bad_albums.py", "--n 100")

    logger.info(f"🏁 MUSIC UTILS CRONHUB : TERMINE !! \n\n")

    # Bonus : d'autres idées
    # if today.strftime("%m-%d") == "12-31":  # veille du nouvel an
    #     run_python_script("backup_music_db.py")📢⚙️💊📰📅⏰🍾🛸🚨🏁🚧⭐🌞☀️🌈⚡🔥☣️▶️🕗💭🎵🎸🎹🔍🗓️

if __name__ == "__main__":
    main()
