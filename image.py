import os
from pathlib import Path
from PIL import Image


def convert_to_webp(source):
    destination = source.with_suffix(".webp")

    image = Image.open(source)  
    image.save(destination, format="webp")  

    return destination


def main():
    n = os.path.getsize('static/steak.png')
    print("Origin: ", n/1024, "KB")

    paths = Path("static").glob("**/*.png")
    for path in paths:
        webp_path = convert_to_webp(path)
        print(webp_path)

    n = os.path.getsize('static/steak.webp')
    print("Webp: ", n/1024, "KB")


main()
