import requests

def get_API_key(file='maps.key'):
    # See https://developers.google.com/maps/documentation/javascript/get-api-key?hl=fr
    with open(file, 'r') as key_file:
        return key_file.read().strip()

def get_image_from_coordinates(api_key, latitude, longitude, zoom=16, largeur=1280, hauteur=960, output_file="image_satellite.png"):
    # URL de l'API Google Maps Static
    url = f"https://maps.googleapis.com/maps/api/staticmap?center={latitude},{longitude}&zoom={zoom}&size={largeur}x{hauteur}&maptype=satellite&key={api_key}"

    # Envoi de la requête HTTP pour récupérer l'image
    response = requests.get(url)

    # Vérification de la réponse
    if response.status_code == 200:
        # Enregistrement de l'image récupérée
        with open(output_file, "wb") as f:
            f.write(response.content)
        print("Image satellite enregistrée avec succès sous le nom {}".format(output_file))
    else:
        print(f"Erreur lors de la récupération de l'image. Code d'erreur : {response.status_code}")


if __name__ == "__main__":
    # Coordonnées GPS (latitude et longitude)
    latitude = 45.54002
    longitude = 5.38982

    # Récupération de l'image
    api_key=get_API_key()
    get_image_from_coordinates(api_key, latitude, longitude)
