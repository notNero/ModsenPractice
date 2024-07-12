import unittest
from PIL import Image
from hasher import compute_image_hash


class TestHasher(unittest.TestCase):
    def test_compute_image_hash(self):
        img_width = 10
        img_height = 10
        img = Image.new('RGB', (img_width, img_height), color=(0, 0, 0))
        img_hash = compute_image_hash(img)
        self.assertIsInstance(img_hash, object)


if __name__ == '__main__':
    unittest.main()
