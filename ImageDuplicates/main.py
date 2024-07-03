import os
from PIL import Image
import tkinter as tk
from collections import defaultdict
import imagehash


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


def compute_image_hash(image, hash_size=8):
    # Compute a hash for the given image using average hashing
    return imagehash.average_hash(image, hash_size=hash_size)


def find_duplicates(images):
    # Find duplicate images based on their hashes
    hash_dict = defaultdict(list)
    for filepath, img in images:
        img_hash = compute_image_hash(img)
        hash_dict[img_hash].append(filepath)
        # Keep entries only with more than one image (duplicates)
    duplicates = {k: v for k, v in hash_dict.items() if len(v) > 1}
    return duplicates


class ImageBrowser(tk.Tk):
    def __init__(self, duplicates):
        super().__init__()
        self.duplicates = list(duplicates.items())
        self.index = 0
        self.title("Duplicate Images")
        self.geometry("1200x600")

        # Create a canvas for displaying images
        self.canvas = tk.Canvas(self, width=800, height=500)
        self.canvas.pack()

        # Create Next and Prev buttons
        self.next_button = tk.Button(self, text="Next", command=self.next)
        self.next_button.pack(side=tk.RIGHT)

        self.prev_button = tk.Button(self, text="Prev", command=self.prev)
        self.prev_button.pack(side=tk.LEFT)

        self.show_images()

    def show_images(self):
        # Clear the canvas and display images
        self.canvas.delete("all")
        img_hash, filepaths = self.duplicates[self.index]
        print(f"Duplicate hash: {img_hash}")
        for filepath in filepaths:
            print(f" - {filepath}")

        # Limit to two images for display and resize them to the same size
        images = [Image.open(filepath) for filepath in filepaths[:2]]
        images = [img.resize((350, 350), Image.LANCZOS) for img in images]
        tk_images = [ImageTk.PhotoImage(img) for img in images]

        # Display the images side by side on the canvas
        x_offset = 50
        for tk_img in tk_images:
            self.canvas.create_image(x_offset, 50, anchor=tk.NW, image=tk_img)
            x_offset += tk_img.width() + 50

        # Save references to avoid garbage collection
        self.images = tk_images

    # Move to the next set of duplicates
    def next(self):
        self.index = (self.index + 1) % len(self.duplicates)
        self.show_images()

    # Move to the previous set of duplicates
    def prev(self):
        self.index = (self.index - 1) % len(self.duplicates)
        self.show_images()


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
    folder2 = None  # Optional
    main(folder1, folder2)
