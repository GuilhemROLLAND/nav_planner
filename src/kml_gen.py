import random
import math

def generate_kml_random_loop_with_start(start_point, distance_km, num_waypoints):
    # Convertir la distance en degrés de latitude pour une approximation grossière
    degrees_per_km = 0.01  # Approximation de la distance en degrés de latitude par kilomètre
    
    # Créer un fichier KML
    kml_file = open("flight_random_loop_with_start.kml", "w", encoding="utf-8")
    kml_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    kml_file.write('<kml xmlns="http://earth.google.com/kml/2.0">\n')
    kml_file.write('\t<Document>\n')

    # Ajouter le nom du trajet
    kml_file.write('\t\t<name>Nav Photos Régul 1</name>\n')

    # Ajouter le style pour la ligne
    kml_file.write('\t\t<Style id="roadStyle">\n')
    kml_file.write('\t\t\t<LineStyle>\n')
    kml_file.write('\t\t\t\t<color>9F0000FF</color>\n')
    kml_file.write('\t\t\t\t<width>4</width>\n')
    kml_file.write('\t\t\t</LineStyle>\n')
    kml_file.write('\t\t</Style>\n')

    # Ajouter le point de départ
    kml_file.write('\t\t<Placemark id="route">\n')
    kml_file.write('\t\t\t<name>Nav Photos Régul 1</name>\n')
    kml_file.write('\t\t\t<styleUrl>#roadStyle</styleUrl>\n')
    kml_file.write('\t\t\t<MultiGeometry>\n')

    prev_point = start_point

    # Calculer les points intermédiaires aléatoires pour former la boucle
    for i in range(num_waypoints):
        fraction = i / num_waypoints
        # Calculer la position le long de la boucle en utilisant un cercle
        angle = fraction * 2 * math.pi
        delta_lat = degrees_per_km * distance_km * math.sin(angle)
        delta_lon = degrees_per_km * distance_km * math.cos(angle)
        intermediate_point = (prev_point[0] + delta_lat, prev_point[1] + delta_lon)
        
        # Ajouter une variation aléatoire plus importante pour une forme plus aléatoire
        delta_lat_random = random.uniform(-0.04, 0.04)  # Variation plus importante
        delta_lon_random = random.uniform(-0.04, 0.04)  # Variation plus importante
        intermediate_point = (intermediate_point[0] + delta_lat_random, intermediate_point[1] + delta_lon_random)

        # Ajouter une LineString pour chaque segment
        kml_file.write('\t\t\t\t<LineString>\n')
        kml_file.write('\t\t\t\t\t<coordinates>\n')
        kml_file.write(f'\t\t\t\t\t\t{prev_point[1]},{prev_point[0]},0\n')
        kml_file.write(f'\t\t\t\t\t\t{intermediate_point[1]},{intermediate_point[0]},0\n')
        kml_file.write('\t\t\t\t\t</coordinates>\n')
        kml_file.write('\t\t\t\t</LineString>\n')

        prev_point = intermediate_point
    
    # Revenir au point de départ pour fermer la boucle
    kml_file.write('\t\t\t\t<LineString>\n')
    kml_file.write('\t\t\t\t\t<coordinates>\n')
    kml_file.write(f'\t\t\t\t\t\t{prev_point[1]},{prev_point[0]},0\n')
    kml_file.write(f'\t\t\t\t\t\t{start_point[1]},{start_point[0]},0\n')
    kml_file.write('\t\t\t\t\t</coordinates>\n')
    kml_file.write('\t\t\t\t</LineString>\n')

    kml_file.write('\t\t\t</MultiGeometry>\n')
    kml_file.write('\t\t</Placemark>\n')

    kml_file.write('\t</Document>\n')
    kml_file.write('</kml>\n')
    kml_file.close()

# Exemple d'utilisation
start_point = (45.43894, 5.51026)  # Coordonnées GPS de départ (à adapter)
distance_km = 4.5  # kilomètres (boucle complète)
num_waypoints = 20  # Nombre de points intermédiaires
generate_kml_random_loop_with_start(start_point, distance_km, num_waypoints)
