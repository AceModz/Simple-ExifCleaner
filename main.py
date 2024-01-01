import os
from PIL import Image
from moviepy.editor import VideoFileClip
import shutil
import tkinter as tk
from tkinter import filedialog

def remove_exif(file_path, output_folder):
    try:
        # Créer un dossier pour les fichiers sans données Exif si celui-ci n'existe pas
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Déterminer le type de fichier
        image_extensions = ('.jpeg', '.jpg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.raw', '.svg', '.psd', '.ico', '.heif', '.heic')
        video_extensions = ('.mp4', '.avi', '.mkv', '.wmv', '.mov', '.flv', '.webm', '.3gp', '.mpeg', '.vob')

        if file_path.lower().endswith(image_extensions):
            # Ouvrir l'image avec Pillow
            with Image.open(file_path) as img:
                # Sauvegarder l'image sans les données Exif dans le dossier spécifié
                output_path = os.path.join(output_folder, os.path.basename(file_path))
                img.save(output_path)
        elif file_path.lower().endswith(video_extensions):
            # Charger la vidéo avec moviepy
            video_clip = VideoFileClip(file_path)

            # Créer un nouveau clip vidéo sans métadonnées
            new_video_clip = video_clip.subclip(0, video_clip.duration)

            # Sauvegarder la nouvelle vidéo dans le dossier spécifié
            output_path = os.path.join(output_folder, os.path.basename(file_path))
            new_video_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", remove_temp=True)
        else:
            print(f"Le fichier {file_path} n'est ni une image ni une vidéo. Les données Exif n'ont pas été supprimées.")
            return

        print(f"Les données Exif ont été supprimées avec succès de {file_path}")
        print(f"Une copie du fichier sans données Exif a été créée à {output_path}")

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

def select_file():
    file_path = filedialog.askopenfilename(title="Sélectionner un fichier",
                                           filetypes=[("Fichiers image et vidéo",
                                                       "*.jpeg;*.jpg;*.png;*.gif;*.bmp;*.tiff;*.tif;*.raw;*.svg;*.psd;*.ico;*.heif;*.heic;*.mp4;*.avi;*.mkv;*.wmv;*.mov;*.flv;*.webm;*.3gp;*.mpeg;*.vob"),
                                                      ("Tous les fichiers", "*.*")])
    if file_path:
        # Déterminer le type de fichier
        image_extensions = ('.jpeg', '.jpg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.raw', '.svg', '.psd', '.ico', '.heif', '.heic')
        video_extensions = ('.mp4', '.avi', '.mkv', '.wmv', '.mov', '.flv', '.webm', '.3gp', '.mpeg', '.vob')

        if file_path.lower().endswith(image_extensions):
            remove_exif(file_path, "Removed Exif Image")
        elif file_path.lower().endswith(video_extensions):
            remove_exif(file_path, "Removed Exif Video")
        else:
            print(f"Le fichier {file_path} n'est ni une image ni une vidéo. Les données Exif n'ont pas été supprimées.")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Cacher la fenêtre principale de tkinter

    # Appeler la fonction pour sélectionner le fichier
    select_file()
