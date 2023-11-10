import xml.etree.ElementTree as ET


def extract_coordinates(fichier_kml="junction_flight_random_loop.kml"):
    # Charger le fichier KML
    tree = ET.parse(fichier_kml)
    root = tree.getroot()

    # Parcourir le fichier pour extraire les coordonnées
    coordinates = root.find(
        ".//{http://earth.google.com/kml/2.0}coordinates")
    coordinates = coordinates.text.strip().split('\n')

    coordinates_gps = list()  # Utiliser un ensemble pour stocker les coordonnées uniques
    # Parcourir chaque paire de coordonnées
    for coordinate_pair in coordinates:
        parts = coordinate_pair.strip().split(',')
        longitude, latitude, altitude = map(float, parts)
        coordinates_gps.append((latitude, longitude))

    return list(coordinates_gps)


if __name__ == "__main__":
    # Exemple d'utilisation de la fonction
    coordonnees = extract_coordinates()

    # Afficher les coordonnées extraites sans doublons
    for coordonnee in coordonnees:
        print(f"Latitude: {coordonnee[0]}, Longitude: {coordonnee[1]}")
