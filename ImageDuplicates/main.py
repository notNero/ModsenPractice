from loader import load_images_from_folder
from duplicate_finder import find_duplicates
from image_browser import ImageBrowser


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
    # Set folders to be checked for duplicates
    folder1 = "Path to the first folder with images."
    folder2 = None  # Optional second folder
    main(folder1, folder2)
