from collections import defaultdict
from hasher import compute_image_hash


def find_duplicates(images):
    # Find duplicate images based on their hashes
    hash_dict = defaultdict(list)
    for filepath, img in images:
        img_hash = compute_image_hash(img)
        hash_dict[img_hash].append(filepath)
    duplicates = {k: v for k, v in hash_dict.items() if len(v) > 1}
    return duplicates
