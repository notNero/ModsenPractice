import imagehash


def compute_image_hash(image, hash_size=8):
    # Compute a hash for the given image using average hashing
    return imagehash.average_hash(image, hash_size=hash_size)
