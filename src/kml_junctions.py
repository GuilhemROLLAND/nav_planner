import xml.etree.ElementTree as ET
from geopy.distance import geodesic
from geopy.geocoders import Nominatim


def move_points_to_nearest_junction(input_kml, output_kml):
    # Function to find the nearest road junction to a point
    def find_nearest_junction(point, junctions):
        distances = [(junction, geodesic(point, junction).meters)
                     for junction in junctions]
        distances.sort(key=lambda x: x[1])
        return distances[0][0]

    # Load the KML file
    tree = ET.parse(input_kml)
    root = tree.getroot()

    # Extract coordinates of the points
    points = []
    coordinates_element = root.find(
        ".//{http://earth.google.com/kml/2.0}coordinates")
    if coordinates_element is not None:
        coordinates_text = coordinates_element.text.strip()
        coordinates_list = [tuple(sorted((map(float, point.split(
            ','))), reverse=True)) for point in coordinates_text.split()]
        points.extend(coordinates_list)

    # Extract coordinates of road junctions (you can use a service like Nominatim to obtain them)
    geolocator = Nominatim(user_agent="my_geocoder")
    junctions = []

    for point in points:
        location = geolocator.reverse(point)
        junctions.append((location.latitude, location.longitude))

    # Move each point to the nearest road junction
    new_points = []
    for point in points:
        nearest_junction = find_nearest_junction(point, junctions)
        new_points.append(nearest_junction)

    # Update the coordinates in the KML file
    coordinates_element.text = "\n"
    for point in new_points:
        coordinates_element.text += f"{point[1]},{point[0]},0\n"

    # Save the updated KML file
    tree.write(output_kml, encoding='utf-8', xml_declaration=True)


if __name__ == "__main__":
    # Example usage:
    move_points_to_nearest_junction(
        'flight_random_loop_with_start.kml', 'junction_flight_random_loop.kml')
