import os
from PIL import Image
"""
    Load images from the specified folder.

    Args:
        folder (str): Path to the folder containing images.

    Returns:
        list: A list of tuples containing the file path and the loaded image object.
    """


def load_images_from_folder(folder):
    # Load images from the specified folder
    images = []
    for filename in os.listdir(folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                img = Image.open(os.path.join(folder, filename))
                images.append((os.path.join(folder, filename), img))
            except (IOError, OSError) as e:
                print(f"Error loading {filename}: {e}")
    return images
