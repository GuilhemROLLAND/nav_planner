import os
import random
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib import utils
import improve_images


def create_pdf_with_images(image_folder="images/", num_images=12, pdf_filename="photos.pdf", text_filename="photo_list.txt"):
    # Liste des fichiers d'images dans le dossier
    files = os.listdir(image_folder)

    # Augmente la luminosité pour impression
    for file in files:
        improve_images.increase_brightness(os.path.join(image_folder, file))

    # Sélectionne le nombre spécifié de fichiers d'images au hasard sans doublon
    selected_files = random.sample(files, num_images)

    # Crée un nouveau fichier PDF
    pdf = canvas.Canvas(pdf_filename)

    # Ouvre un fichier texte pour écrire les noms de fichiers
    with open(text_filename, "w") as file:
        # Ajoute chaque image au PDF
        for i, filename in enumerate(selected_files):
            # Écrit le nom de fichier dans le fichier texte
            file.write(filename + "\n")

            # Ouvre l'image et redimensionne-la si nécessaire
            image = Image.open(os.path.join("bright_images/", filename))
            if image.width > 290 or image.height > 290:
                image.thumbnail((290, 290))

            # Calcule la position de l'image sur la page
            x = ((i % 6) % 2) * 300 + 5
            y = ((i % 6) // 2) * 300 + 5

            # Convertit l'image PIL en objet ReportLab
            img_data = utils.ImageReader(os.path.join(image_folder, filename))
            pdf.drawImage(img_data, x, y, width=image.width,
                          height=image.height)

            # Ajoute une nouvelle page si nécessaire
            if i == 5:
                pdf.showPage()

    # Enregistre le fichier PDF et ferme-le
    pdf.save()


if __name__ == "__main__":
    # Exemple d'utilisation :
    create_pdf_with_images("images/", 12, "photos.pdf", "photo_list.txt")
