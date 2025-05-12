import subprocess
import argparse
from datetime import datetime
from beets_utils.commands import run_beet_command
from utils.logger import get_logger

# def run_beet_command(command, target=None, dry_run=False):
#     cmd = ["beet"] + command.split()
#     if target:
#         cmd.append(target)

#     if dry_run:
#         logger.info(f"[SIMULATION] {' '.join(cmd)}")
#         return

#     try:
#         subprocess.run(cmd, check=True)
#         logger.info(f"[OK] {command} {'sur ' + target if target else '(base complète)'}")
#     except subprocess.CalledProcessError as e:
#         logger.warning(f"[ERREUR] {command} échoué {'sur ' + target if target else ''}")
#         logger.warning(e)

def sync_metadata(target_path=None, dry_run=False):
    #logger=get_new_logger_or_not(name="Musicbrainz Sync", logname=args.logname)
    logger = get_logger("Musicbrainz Sync")
        
    logger.info(f"📅 SYNC MUSICBRAINZ : {datetime.now().strftime('%d-%m-%Y')}")
    logger.info("--- (synchronise les données avec la base Musicbrainz) ---")
    scope = target_path if target_path else "toute la base"
    logger.info(f"🎯 Portée : {scope}")

    run_beet_command(command="mbsync", args=[target_path], capture_output=False, dry_run=dry_run, logname="Musicbrainz Sync")
    run_beet_command(command="write -f", args=[target_path], capture_output=False, dry_run=dry_run, logname="Musicbrainz Sync")
    run_beet_command(command="move", args=[target_path], capture_output=False, dry_run=dry_run, logname="Musicbrainz Sync")

    logger.info(f"🏁 SYNC MUSICBRAINZ : TERMINE !! \n\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync Beets via MB (globale ou ciblée)")
    parser.add_argument("--path", help="Chemin d'un dossier album (sinon toute la base)")
    parser.add_argument("--dry-run", action="store_true", help="Simulation sans modification")
    args = parser.parse_args()

    sync_metadata(target_path=args.path, dry_run=args.dry_run)
