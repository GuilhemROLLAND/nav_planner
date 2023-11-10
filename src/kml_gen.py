import random
import math


def generate_kml_random_loop_with_start(start_point, distance_km, start_cap, num_waypoints=20, kml_file_name="flight_random_loop_with_start.kml"):

    CIRCUMFERENCE_KM = 40075

    # Compute the start angle in radians
    start_angle = (-1) * (start_cap - 90) * 2 * math.pi / 360

    # Generate the KML file
    kml_file = open(kml_file_name, "w", encoding="utf-8")
    kml_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    kml_file.write('<kml xmlns="http://earth.google.com/kml/2.0">\n')
    kml_file.write('\t<Document>\n')

    # Add name
    kml_file.write('\t\t<name>Nav Photos reguliere</name>\n')

    # Add style
    kml_file.write('\t\t<Style id="roadStyle">\n')
    kml_file.write('\t\t\t<LineStyle>\n')
    kml_file.write('\t\t\t\t<color>9F0000FF</color>\n')
    kml_file.write('\t\t\t\t<width>4</width>\n')
    kml_file.write('\t\t\t</LineStyle>\n')
    kml_file.write('\t\t</Style>\n')

    # Add the starting point
    kml_file.write('\t\t<Placemark id="route">\n')
    kml_file.write('\t\t\t<name>Nav Photos reguliere</name>\n')
    kml_file.write('\t\t\t<styleUrl>#roadStyle</styleUrl>\n')
    kml_file.write('\t\t\t<MultiGeometry>\n')
    kml_file.write('\t\t\t\t<LineString>\n')
    kml_file.write('\t\t\t\t\t<coordinates>\n')

    # Invert latitude and longitude to match x and y format
    prev_point = [0, 0]
    prev_point[0], prev_point[1] = start_point[1], start_point[0]

    # Build the loop
    for i in range(num_waypoints):
        # Get the angle depending on the number of waypoints
        angle = start_angle + (i * 2 * math.pi / num_waypoints)
        # Compute the x and y distances
        x_dist =  1.2* distance_km * \
            math.cos(angle) / CIRCUMFERENCE_KM * num_waypoints
        y_dist = .8 * distance_km * \
            math.sin(angle) / CIRCUMFERENCE_KM * num_waypoints
        # Compute the perfect intermediate point
        intermediate_point = (prev_point[0] + x_dist, prev_point[1] + y_dist)

        # Get random drift
        x_drift = random.uniform(-0.02, 0.02)
        y_drift = random.uniform(-0.02, 0.02)
        # Add the drift to the intermediate point
        intermediate_point = (
            intermediate_point[0] + x_drift, intermediate_point[1] + y_drift)

        # Add to the KML file
        kml_file.write(
            f'\t\t\t\t\t\t{intermediate_point[0]},{intermediate_point[1]},0\n')

        # Update the new starting point for the next iteration
        prev_point = intermediate_point

    kml_file.write('\t\t\t\t\t</coordinates>\n')
    kml_file.write('\t\t\t\t</LineString>\n')
    kml_file.write('\t\t\t</MultiGeometry>\n')
    kml_file.write('\t\t</Placemark>\n')

    kml_file.write('\t</Document>\n')
    kml_file.write('</kml>\n')
    kml_file.close()
    return kml_file_name


if __name__ == "__main__":
    # Example
    start_point = (45.533329, 5.33333)  # (latitude, longitude) starting point
    # Distance of the loop (in km) (it's better to minimize it)
    distance_km = 50
    num_waypoints = 20  # Number of waypoints
    start_cap = 150  # Cap when you pass the starting point (in degrees)

    generate_kml_random_loop_with_start(
        start_point, distance_km, start_cap, num_waypoints)
