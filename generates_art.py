import climage
import sys
import requests
from io import BytesIO
from PIL import Image

def generate_art(image_source, width=100):
    try:
        if image_source.startswith(('http://', 'https://')):
            response = requests.get(image_source)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content))
            # climage doesn't support PIL images directly, so we need to save it to a temporary file
            temp_image_path = "temp_rose.jpg"
            img.save(temp_image_path)
            output = climage.convert(temp_image_path, is_unicode=True, width=width)
            print(output)
            print("CommandCraft")
        else:
            output = climage.convert(image_source, is_unicode=True, width=width)
            print(output)
            print("CommandCraft")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generates_art.py <image_file_path_or_url> [width]")
        sys.exit(1)

    img_source = sys.argv[1]
    
    output_width = 100
    if len(sys.argv) > 2:
        try:
            output_width = int(sys.argv[2])
        except ValueError:
            print("Error: Width must be an integer.")
            sys.exit(1)

    generate_art(img_source, output_width)