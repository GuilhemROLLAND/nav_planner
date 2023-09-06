import xml.etree.ElementTree as ET
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

# Function to find the nearest road junction to a point
def find_nearest_junction(point, junctions):
    distances = [(junction, geodesic(point, junction).meters) for junction in junctions]
    distances.sort(key=lambda x: x[1])
    return distances[0][0]

# Load the KML file
tree = ET.parse('flight_random_loop_with_start.kml')
root = tree.getroot()

# Extract coordinates of the points
points = []
for coordinates_elem in root.findall('.//{http://earth.google.com/kml/2.0}coordinates'):
    coordinates = coordinates_elem.text.strip().split(',')
    lat, lon = float(coordinates[1]), float(coordinates[0])
    points.append((lat, lon))

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
for coordinates_elem, start, end in zip(root.findall('.//{http://earth.google.com/kml/2.0}coordinates'), new_points, new_points[1:]):
    coordinates_elem.text = f"{start[1]},{start[0]},0\n{end[1]},{end[0]},0"

# Save the updated KML file
tree.write('junction_flight_random_loop.kml', encoding='utf-8', xml_declaration=True)
