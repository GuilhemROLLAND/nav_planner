import get_photos
import kml_coordinates

def get_photos_on_turnpoint(output_directory='images'):
    coordinates = kml_coordinates.extract_coordinates()

    for coordinate in coordinates:
        latitude, longitude = coordinate[0], coordinate[1]
        output_file = f"{output_directory}/{latitude}_{longitude}.png"
        get_photos.get_image_from_coordinates(latitude, longitude, output_file=output_file)

# Exemple d'utilisation de la fonction
if __name__ == "__main__":
    get_photos_on_turnpoint()
