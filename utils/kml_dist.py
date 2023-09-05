import xml.etree.ElementTree as ET
from geopy.distance import great_circle

# Charger le fichier KML
tree = ET.parse('flight_random_loop_with_start.kml')
root = tree.getroot()

# Extraire les coordonnées de toutes les balises <coordinates>
coordinates = []
for elem in root.iter('{http://earth.google.com/kml/2.0}coordinates'):
    coord_text = elem.text.strip()
    coords = coord_text.split(',')
    coordinates.append((float(coords[0]), float(coords[1])))

# Calculer la distance totale
total_distance = 0.0
for i in range(len(coordinates) - 1):
    coord1 = coordinates[i]
    coord2 = coordinates[i + 1]
    total_distance += great_circle(coord1, coord2).kilometers

print(f"Distance totale de la trace : {total_distance:.2f} kilomètres")
