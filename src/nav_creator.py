import datetime
import os
import kml_gen
import kml_junctions
import photos_on_turnpoint
import photos_pdf_creator
import get_photos
import shutil

def output_nav(kml_file_name):
    folder_name = "nav_{0}".format(datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))
    os.mkdir(folder_name)
    shutil.copy("junction_flight_random_loop.kml", folder_name)
    shutil.copy("photos.pdf", folder_name)
    shutil.copy("photo_list.txt", folder_name)
    shutil.copytree("images", folder_name+"/images/")
    print("Nav created in {0}".format(folder_name))

def nav_creator(latitude, longitude, angle, distance=50):
    print("Creating nav with parameters: lat={0}, long={1}, angle={2}, distance={3}".format(latitude, longitude, angle, distance))

    print("Generating kml file...")
    kml_file_name = kml_gen.generate_kml_random_loop_with_start(
        (latitude, longitude), distance, angle)
    print("Kml file generated: {0}".format(kml_file_name))

    print("Moving points to nearest junction...")
    kml_junctions.move_points_to_nearest_junction(kml_file_name, "junction_flight_random_loop.kml")
    print("Points moved")

    print("Getting photos on turnpoints...")
    photos_on_turnpoint.get_photos_on_turnpoint(
        get_photos.get_API_key(), kml_file_name)
    print("Photos on turnpoints got")

    print("Creating pdf with photos...")
    photos_pdf_creator.create_pdf_with_images()
    print("Pdf created")

    print("Outputing nav...")
    output_nav(kml_file_name)
    print("Nav outputed")


if __name__ == "__main__":
    nav_creator(45.533329, 5.33333, 150, 50)
