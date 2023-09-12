import os
import random
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib import utils


# Chemin du dossier contenant les images
path = "images/"

# Liste des fichiers d'images dans le dossier
files = os.listdir(path)

# Sélectionne 12 fichiers d'images au hasard sans doublon
selected_files = random.sample(files, 12)

# Crée un nouveau fichier PDF
pdf = canvas.Canvas("photos.pdf")

# Ajoute chaque image au PDF
for i, filename in enumerate(selected_files):
    # Ouvre l'image et redimensionne-la si nécessaire
    image = Image.open(path + filename)
    if image.width > 290 or image.height > 290:
        image.thumbnail((290, 290))

    # Calcule la position de l'image sur la page
    x = ((i % 6) % 2) * 300 + 5
    y = ((i % 6) // 2) * 300 + 5

    # Convertit l'image PIL en objet ReportLab
    img_data = utils.ImageReader(path + filename)
    pdf.drawImage(img_data, x, y, width=image.width, height=image.height)

    # Ajoute une nouvelle page si nécessaire
    if i == 5:
        pdf.showPage()

# Enregistre le fichier PDF et ferme-le
pdf.save()
