import os
from PIL import Image
import matplotlib.pyplot as plt
from collections import defaultdict
import imagehash


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                img = Image.open(os.path.join(folder, filename))
                images.append((os.path.join(folder, filename), img))
            except (IOError, OSError) as e:
                print(f"Error loading {filename}: {e}")
    return images


def compute_image_hash(image, hash_size=8):
    return imagehash.average_hash(image, hash_size=hash_size)


def find_duplicates(images):
    hash_dict = defaultdict(list)
    for filepath, img in images:
        img_hash = compute_image_hash(img)
        hash_dict[img_hash].append(filepath)
    duplicates = {k: v for k, v in hash_dict.items() if len(v) > 1}
    return duplicates


def visualize_duplicates(duplicates):
    for img_hash, filepaths in duplicates.items():
        print(f"Duplicate hash: {img_hash}")
        for filepath in filepaths:
            print(f" - {filepath}")
        fig, axs = plt.subplots(1, len(filepaths), figsize=(15, 5))
        for ax, filepath in zip(axs, filepaths):
            img = Image.open(filepath)
            ax.imshow(img)
            ax.axis('off')
        plt.show()


def main(folder1, folder2=None):
    images1 = load_images_from_folder(folder1)
    if folder2:
        images2 = load_images_from_folder(folder2)
        images = images1 + images2
    else:
        images = images1

    duplicates = find_duplicates(images)

    if duplicates:
        visualize_duplicates(duplicates)
    else:
        print("No duplicates found.")


if __name__ == "__main__":
    folder1 = "Path to the first folder with images."
    folder2 = None  # Optional
    main(folder1, folder2)