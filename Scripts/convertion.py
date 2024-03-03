import os
import time
from PIL import Image

def convert_avif_to_jpg_or_png(input_path, output_path):
    try:
        img = Image.open(input_path)
        if img.format == "AVIF":
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            filename, _ = os.path.splitext(os.path.basename(input_path))
            jpg_path = os.path.join(output_path, filename + ".jpg")
            png_path = os.path.join(output_path, filename + ".png")
            img.save(jpg_path)
            img.save(png_path)
            print(f"Converted {input_path} to JPG: {jpg_path}")
            print(f"Converted {input_path} to PNG: {png_path}")
        else:
            print(f"{input_path} is not an AVIF file.")
    except Exception as e:
        print(f"Error converting {input_path}: {e}")

def watch_directory(directory):
    print(f"Watching directory: {directory}")
    while True:
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath) and filename.lower().endswith('.avif'):
                try:
                    convert_avif_to_jpg_or_png(filepath, directory)
                except Exception as e:
                    print(f"Error converting {filepath}: {e}")
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    directory_to_watch = "C:\\Users\\Redmark\\Documents\\Django\\Web\\Japa\\static\\images\\temp"
    output_directory = "C:\\Users\\Redmark\\Documents\\Django\\Web\\Japa\\static\\images\\food"
    watch_directory(directory_to_watch)
