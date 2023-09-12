import xml.etree.ElementTree as ET


def extract_coordinates(fichier_kml="junction_flight_random_loop.kml"):
    # Charger le fichier KML
    tree = ET.parse(fichier_kml)
    root = tree.getroot()

    # Trouver tous les éléments 'LineString'
    line_strings = root.findall(
        './/{http://earth.google.com/kml/2.0}LineString')

    coordonnees_gps = set()  # Utiliser un ensemble pour stocker les coordonnées uniques

    # Parcourir chaque 'LineString' pour extraire les coordonnées
    for line_string in line_strings:
        coordinates = line_string.find(
            '{http://earth.google.com/kml/2.0}coordinates').text
        coordinates = coordinates.strip().split('\n')

        # Parcourir chaque paire de coordonnées
        for coordinate_pair in coordinates:
            parts = coordinate_pair.strip().split(',')
            longitude, latitude, altitude = map(float, parts)
            coordonnees_gps.add((latitude, longitude))

    return list(coordonnees_gps)


if __name__ == "__main__":
    # Exemple d'utilisation de la fonction
    coordonnees = extract_coordinates()

    # Afficher les coordonnées extraites sans doublons
    for coordonnee in coordonnees:
        print(f"Latitude: {coordonnee[0]}, Longitude: {coordonnee[1]}")
