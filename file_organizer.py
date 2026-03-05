import os
import shutil

# Folder path you want to organize
path = input("Enter folder path (C:\\Users\\yourname\\Downloads) :")

# File type categories
folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Music": [".mp3", ".wav"],
    "Programs": [".exe", ".msi"]
}

# Create folders if they don't exist
for folder in folders:
    folder_path = os.path.join(path, folder)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

# Organize files
for file in os.listdir(path):
    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):
        for folder, extensions in folders.items():
            if file.endswith(tuple(extensions)):
                shutil.move(file_path, os.path.join(path, folder, file))
                break
