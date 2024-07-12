import imagehash
"""
   Compute a hash for the given image using average hashing.

   Args:
       image (PIL.Image.Image): The image to hash.
       hash_size (int): The size of the hash.

   Returns:
       imagehash.ImageHash: The computed hash of the image.
   """


def compute_image_hash(image, hash_size=8):
    # Compute a hash for the given image using average hashing
    return imagehash.average_hash(image, hash_size=hash_size)
