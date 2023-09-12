import get_photos
import kml_coordinates
import os


def get_photos_on_turnpoint(api_key, kml_filename, output_directory='images'):
    # Vérifie si le dossier existe
    if os.path.exists(output_directory):
        # Liste les fichiers et dossiers dans le répertoire
        for file_name in os.listdir(output_directory):
            file_path = os.path.join(output_directory, file_name)
            # Vérifie si c'est un fichier
            if os.path.isfile(file_path):
                # Supprime le fichier
                os.remove(file_path)
            # Vérifie si c'est un dossier
            elif os.path.isdir(file_path):
                # Supprime le dossier et tout son contenu récursivement
                os.rmdir(file_path)
    else:
        # Crée le dossier
        os.mkdir(output_directory)

    coordinates = kml_coordinates.extract_coordinates(kml_filename)

    for coordinate in coordinates:
        latitude, longitude = coordinate[0], coordinate[1]
        output_file = f"{output_directory}/{latitude}_{longitude}.png"
        get_photos.get_image_from_coordinates(api_key,
                                              latitude, longitude, output_file=output_file)


if __name__ == "__main__":
    # Exemple d'utilisation de la fonction
    get_photos_on_turnpoint(get_photos.get_API_key(),
                            "junction_flight_random_loop.kml")
