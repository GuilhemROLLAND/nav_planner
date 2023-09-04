import random
import math

def generate_kml_random_loop_with_start(start_point, distance_km, num_waypoints):
    # Convertir la distance en degrés de latitude pour une approximation grossière
    degrees_per_km = 0.00899  # Approximation de la distance en degrés de latitude par kilomètre
    
    # Créer un fichier KML
    kml_file = open("flight_random_loop_with_start.kml", "w")
    kml_file.write("<?xml version='1.0' encoding='UTF-8'?>\n")
    kml_file.write("<kml xmlns='http://www.opengis.net/kml/2.2'>\n")
    kml_file.write("<Document>\n")
    kml_file.write("  <name>Flight Random Loop with Start</name>\n")
    
    # Ajouter le point de départ
    kml_file.write("  <Placemark>\n")
    kml_file.write("    <name>Start/End</name>\n")
    kml_file.write("    <Point>\n")
    kml_file.write(f"      <coordinates>{start_point[1]},{start_point[0]},0</coordinates>\n")
    kml_file.write("    </Point>\n")
    kml_file.write("  </Placemark>\n")
    
    # Calculer les points intermédiaires aléatoires pour former la boucle
    for i in range(num_waypoints):
        fraction = i / num_waypoints
        # Calculer la position le long de la boucle en utilisant un cercle
        angle = fraction * 2 * math.pi
        delta_lat = degrees_per_km * distance_km * math.sin(angle)
        delta_lon = degrees_per_km * distance_km * math.cos(angle)
        intermediate_point = (start_point[0] + delta_lat, start_point[1] + delta_lon)
        
        # Ajouter une variation aléatoire plus importante pour une forme plus aléatoire
        delta_lat_random = random.uniform(-0.1, 0.1)  # Variation plus importante
        delta_lon_random = random.uniform(-0.1, 0.1)  # Variation plus importante
        intermediate_point = (intermediate_point[0] + delta_lat_random, intermediate_point[1] + delta_lon_random)
        
        kml_file.write("  <Placemark>\n")
        kml_file.write(f"    <name>Waypoint {i}</name>\n")
        kml_file.write("    <Point>\n")
        kml_file.write(f"      <coordinates>{intermediate_point[1]},{intermediate_point[0]},0</coordinates>\n")
        kml_file.write("    </Point>\n")
        kml_file.write("  </Placemark>\n")
    
    # Revenir au point de départ pour fermer la boucle
    kml_file.write("  <Placemark>\n")
    kml_file.write("    <name>End (Start)</name>\n")
    kml_file.write("    <Point>\n")
    kml_file.write(f"      <coordinates>{start_point[1]},{start_point[0]},0</coordinates>\n")
    kml_file.write("    </Point>\n")
    kml_file.write("  </Placemark>\n")
    
    kml_file.write("</Document>\n")
    kml_file.write("</kml>\n")
    kml_file.close()

# Exemple d'utilisation
start_point = (48.858844, 2.294351)  # Coordonnées GPS de Paris
distance_km = 50  # 50 kilomètres (boucle complète)
num_waypoints = 36  # Nombre de points intermédiaires
generate_kml_random_loop_with_start(start_point, distance_km, num_waypoints)
