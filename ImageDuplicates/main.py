import argparse
from loader import load_images_from_folder
from duplicate_finder import find_duplicates
from image_browser import ImageBrowser
"""
   Main function to load images, find duplicates, and display them.

   Parameters:
       folder1 (str): Path to the first folder containing images.
       folder2 (str, optional): Path to the second folder containing images. Defaults to None.
   """


def main(folder1, folder2=None):
    # Load images from specified folders
    images1 = load_images_from_folder(folder1)
    if folder2:
        images2 = load_images_from_folder(folder2)
        images = images1 + images2
    else:
        images = images1

    # Find and display duplicates
    duplicates = find_duplicates(images)

    if duplicates:
        app = ImageBrowser(duplicates)
        app.mainloop()
    else:
        print("No duplicates found.")


if __name__ == "__main__":
    # Parse folders to be checked for duplicates
    parser = argparse.ArgumentParser(description="Process some images.")
    parser.add_argument('folder1', type=str, help="Path to the first folder with images")
    parser.add_argument('--folder2', type=str, default=None, help="Path to the second folder with images (optional).")

    args = parser.parse_args()

    main(args.folder1, args.folder2)
