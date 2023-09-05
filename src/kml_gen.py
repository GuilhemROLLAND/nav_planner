import random
import math

def generate_kml_random_loop_with_start(start_point, distance_km, num_waypoints):
    circunference_km = 40075
    # Generate the KML file
    kml_file = open("flight_random_loop_with_start.kml", "w", encoding="utf-8")
    kml_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    kml_file.write('<kml xmlns="http://earth.google.com/kml/2.0">\n')
    kml_file.write('\t<Document>\n')

    # Add name
    kml_file.write('\t\t<name>Nav Photos Régul</name>\n')

    # Add style
    kml_file.write('\t\t<Style id="roadStyle">\n')
    kml_file.write('\t\t\t<LineStyle>\n')
    kml_file.write('\t\t\t\t<color>9F0000FF</color>\n')
    kml_file.write('\t\t\t\t<width>4</width>\n')
    kml_file.write('\t\t\t</LineStyle>\n')
    kml_file.write('\t\t</Style>\n')

    # Add the starting point
    kml_file.write('\t\t<Placemark id="route">\n')
    kml_file.write('\t\t\t<name>Nav Photos Régul 1</name>\n')
    kml_file.write('\t\t\t<styleUrl>#roadStyle</styleUrl>\n')
    kml_file.write('\t\t\t<MultiGeometry>\n')

    # Invert latitude and longitude to match x and y format
    prev_point = [0,0]
    prev_point[0],prev_point[1] = start_point[1],start_point[0]

    # Build the loop
    for i in range(num_waypoints):
        # Get the angle depending on the number of waypoints
        angle = i * 2 * math.pi / num_waypoints 
        # Compute the x and y distances
        x_dist = distance_km * math.cos(angle) / circunference_km * num_waypoints
        y_dist = distance_km * math.sin(angle) / circunference_km * num_waypoints
        # Compute the perfect intermediate point
        intermediate_point = (prev_point[0] + x_dist, prev_point[1] + y_dist)
        
        # Get random drift
        x_drift = random.uniform(-0.001, 0.001)  
        y_drift = random.uniform(-0.001, 0.001)  
        # Add the drift to the intermediate point
        intermediate_point = (intermediate_point[0] + x_drift, intermediate_point[1] + y_drift)

        # Add to the KML file
        kml_file.write('\t\t\t\t<LineString>\n')
        kml_file.write('\t\t\t\t\t<coordinates>\n')
        kml_file.write(f'\t\t\t\t\t\t{prev_point[0]},{prev_point[1]},0\n')
        kml_file.write(f'\t\t\t\t\t\t{intermediate_point[0]},{intermediate_point[1]},0\n')
        kml_file.write('\t\t\t\t\t</coordinates>\n')
        kml_file.write('\t\t\t\t</LineString>\n')

        # Update the new starting point for the next iteration
        prev_point = intermediate_point
    
    kml_file.write('\t\t\t</MultiGeometry>\n')
    kml_file.write('\t\t</Placemark>\n')

    kml_file.write('\t</Document>\n')
    kml_file.write('</kml>\n')
    kml_file.close()

# Exemple d'utilisation
start_point = (45.43894, 5.51026)  # Coordonnées GPS de départ (à adapter)
distance_km = 50  # kilomètres (boucle complète)
num_waypoints = 20  # Nombre de points intermédiaires
generate_kml_random_loop_with_start(start_point, distance_km, num_waypoints)
