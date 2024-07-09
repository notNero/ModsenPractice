import tkinter as tk
from PIL import Image, ImageTk


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
        self.next_button = tk.Button(self, text="Next", command=self.next, width=20, height=2, bg='lightgreen')
        self.next_button.pack(side=tk.RIGHT, padx=10)

        self.prev_button = tk.Button(self, text="Prev", command=self.prev, width=20, height=2, bg='gray')
        self.prev_button.pack(side=tk.LEFT, padx=10)

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

    def next(self):
        # Move to the next set of duplicates
        self.index = (self.index + 1) % len(self.duplicates)
        self.show_images()

    def prev(self):
        # Move to the previous set of duplicates
        self.index = (self.index - 1) % len(self.duplicates)
        self.show_images()
