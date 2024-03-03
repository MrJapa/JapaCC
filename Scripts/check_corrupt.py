import os
from PIL import Image

def is_avif_corrupted(file_path):
    try:
        with open(file_path, "rb") as f:
            Image.open(f)
        return False  # File is not corrupted
    except Exception as e:
        print(f"Error opening {file_path}: {e}")
        return True  # File is corrupted

if __name__ == "__main__":
    avif_file_path = r"C:\Users\Redmark\Documents\Django\Web\Japa\static\images\temp\amerikansk.avif"  # Change this to the path of your AVIF file
    if is_avif_corrupted(avif_file_path):
        print("The AVIF file is corrupted.")
    else:
        print("The AVIF file is not corrupted.")
