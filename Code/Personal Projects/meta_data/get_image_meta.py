from geopy.geocoders import Nominatim
import os
from PIL import Image, ImageFile

from create_map import create_map


def get_image_metadata(filepath):
    img = Image.open(filepath)
    meta = {'filepath': filepath, 'metadata': {}}
    try:
        for tag, value in img._getexif().items():
            if tag == 34853: # GPSInfo
                gps = {}
                for key in value.keys():
                    gps[key] = value[key]
                meta['metadata']['GPSInfo'] = gps
            elif tag in (0x8298, 0x8825, 271, 272, 305, 306, 42036): # Software and Camera Model
                if value == "Apple":
                    tag = "Phone type"
                elif tag == 272:
                    tag = "Model"
                elif tag == 305:
                    tag = "Bios version"
                elif tag == 306:
                    tag = "Time and Date"
                elif tag == 42036:
                    tag = "Camera info"
                meta['metadata'][tag] = value
        return meta
    except AttributeError as AE:
        print(f"\nNo EXIF data exists in {filepath}\n")
        return "Not able to open"
    
IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.JPEG', '.png', '.gif', '.bmp'] # Add all common image extensions here.
def get_all_image_metadata(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            for ext in IMAGE_EXTENSIONS: # Iterate over all possible image extensions
                if file.endswith(ext): # Check whether the current filename ends with any of these extensions
                    fullfile = os.path.join(root, file)
                    meta_data = get_image_metadata(fullfile)
                    if meta_data != "Not able to open":
                        print("Image: ", meta_data['filepath'])
                        for key, value in meta_data['metadata'].items():
                            if isinstance(value, dict): # If it's a dictionary
                                print("\t", key, ":")
                                for k2, v2 in value.items():
                                    print("\t\t", k2, "=", v2)
                            else:
                                print("\t", key, "=", value)
                        print() # Add a newline for better readability
                        # Create map if GPS coordinates are available
                        if 'GPSInfo' in meta_data['metadata']:
                            create_map(meta_data['metadata'])