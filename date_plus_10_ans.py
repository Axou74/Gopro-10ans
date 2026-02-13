import subprocess
import os
from datetime import datetime

VIDEO_EXTENSIONS = (".mp4", ".mov", ".MP4", ".MOV")

def add_10_years(date_str):
    dt = datetime.strptime(date_str, "%Y:%m:%d %H:%M:%S")
    return dt.replace(year=dt.year + 10).strftime("%Y:%m:%d %H:%M:%S")

current_dir = os.getcwd()

for file in os.listdir(current_dir):
    if file.endswith(VIDEO_EXTENSIONS):
        try:
            # Lire la date média
            result = subprocess.check_output(
                ["exiftool", "-CreateDate", "-s3", file],
                stderr=subprocess.DEVNULL,
                text=True
            ).strip()

            if not result:
                continue

            new_date = add_10_years(result)

            # Écrire la nouvelle date
            subprocess.run(
                [
                    "exiftool",
                    f"-CreateDate={new_date}",
                    f"-ModifyDate={new_date}",
                    f"-TrackCreateDate={new_date}",
                    f"-TrackModifyDate={new_date}",
                    "-overwrite_original",
                    file
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            print(f"{file} : {result} → {new_date}")

        except Exception as e:
            print(f"Erreur sur {file}")
