import os
from app import app

def get_uploaded_images():
    upload_folder = app.config['UPLOAD_FOLDER']
    image_list = []

    if not os.path.exists(upload_folder):
        return image_list  

    for subdir, _, files in os.walk(upload_folder):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
                image_list.append(file)  

    return image_list
