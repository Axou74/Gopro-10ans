# Gopro-10ans
⚙️ Fonctionnement

Le programme parcourt le dossier courant.

Il détecte les fichiers vidéo aux formats :

.mp4, .mov (insensible à la casse)

Pour chaque vidéo :

Lecture de la date EXIF CreateDate via ExifTool

Ajout de 10 ans à cette date

Réécriture des champs suivants :

CreateDate

ModifyDate

TrackCreateDate

TrackModifyDate

Les métadonnées sont écrasées sans créer de fichier de sauvegarde.

Un résumé est affiché dans la console pour chaque fichier traité.

📦 Prérequis (version script)

Python 3.x

ExifTool installé et accessible dans le PATH

https://exiftool.org/

Bibliothèques Python standard uniquement (datetime, os, subprocess)

▶️ Utilisation (script Python)

Copier le script dans le dossier contenant les vidéos

Ouvrir un terminal dans ce dossier

Lancer :

python date_plus_10_ans.py

🧰 Version exécutable (.exe)

Le projet est également disponible sous forme de fichier .exe, ce qui permet :

Une utilisation sans Python installé

Un simple double-clic pour exécuter le traitement

Une utilisation facile sur des postes non techniques

⚠️ ExifTool reste requis, même avec la version .exe, et doit être présent dans le même dossier ou accessible via le PATH.

⚠️ Attention

Les fichiers sont modifiés de manière irréversible

Il est fortement recommandé de faire une copie de sauvegarde avant exécution
