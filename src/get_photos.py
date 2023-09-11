import requests

def get_API_key(file='maps.key'):
    # See https://developers.google.com/maps/documentation/javascript/get-api-key?hl=fr
    with open(file, 'r') as key_file:
        return key_file.read().strip()

def get_image_from_coordinates(latitude, longitude, zoom=16, largeur=1280, hauteur=960):
    # URL de l'API Google Maps Static
    url = f"https://maps.googleapis.com/maps/api/staticmap?center={latitude},{longitude}&zoom={zoom}&size={largeur}x{hauteur}&maptype=satellite&key={API_KEY}"

    # Envoi de la requête HTTP pour récupérer l'image
    response = requests.get(url)

    # Vérification de la réponse
    if response.status_code == 200:
        # Enregistrement de l'image récupérée
        with open("image_satellite.png", "wb") as f:
            f.write(response.content)
        print("Image satellite enregistrée avec succès sous le nom 'image_satellite.png'")
    else:
        print(f"Erreur lors de la récupération de l'image. Code d'erreur : {response.status_code}")


# Coordonnées GPS (latitude et longitude)
latitude = 45.502784142511715
longitude = 5.354623871233328

# Zoom de la carte (valeur recommandée pour une vue satellite)
zoom = 16

# Taille de l'image en pixels
largeur = 1280
hauteur = 960

# Récupération de l'image
API_KEY=get_API_key()
get_image_from_coordinates(latitude, longitude)
