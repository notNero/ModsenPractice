import os
from PIL import Image
import tkinter as tk
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
        self.canvas.delete("all")
        img_hash, filepaths = self.duplicates[self.index]
        print(f"Duplicate hash: {img_hash}")
        for filepath in filepaths:
            print(f" - {filepath}")

        images = [Image.open(filepath) for filepath in filepaths[:2]]
        images = [img.resize((350, 350), Image.LANCZOS) for img in images]
        tk_images = [ImageTk.PhotoImage(img) for img in images]

        x_offset = 50
        for tk_img in tk_images:
            self.canvas.create_image(x_offset, 50, anchor=tk.NW, image=tk_img)
            x_offset += tk_img.width() + 50

        self.images = tk_images

    def next(self):
        self.index = (self.index + 1) % len(self.duplicates)
        self.show_images()

    def prev(self):
        self.index = (self.index - 1) % len(self.duplicates)
        self.show_images()


def main(folder1, folder2=None):
    images1 = load_images_from_folder(folder1)
    if folder2:
        images2 = load_images_from_folder(folder2)
        images = images1 + images2
    else:
        images = images1

    duplicates = find_duplicates(images)

    if duplicates:
        app = ImageBrowser(duplicates)
        app.mainloop()
    else:
        print("No duplicates found.")


if __name__ == "__main__":
    folder1 = "Path to the first folder with images."
    folder2 = None  # Optional
    main(folder1, folder2)
