import unittest
import tempfile
import shutil
import os
from PIL import Image
from loader import load_images_from_folder
from duplicate_finder import find_duplicates


class TestDuplicateFinder(unittest.TestCase):
    def setUp(self):
        img_width = 10
        img_height = 10
        self.test_dir = tempfile.mkdtemp()
        self.test_images = []
        for i in range(3):
            img = Image.new('RGB', (img_width, img_height), color=(i*10, i*10, i*10))
            img_path = os.path.join(self.test_dir, f'test_img_{i}.png')
            img.save(img_path)
            self.test_images.append(img_path)
        img_dup = Image.new('RGB', (img_width, img_height), color=(0, 0, 0))
        img_dup_path = os.path.join(self.test_dir, 'test_img_dup.png')
        img_dup.save(img_dup_path)
        self.test_images.append(img_dup_path)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_find_duplicates(self):
        images = load_images_from_folder(self.test_dir)
        duplicates = find_duplicates(images)
        self.assertEqual(len(duplicates), 1)
        self.assertIn(self.test_images[0], duplicates[list(duplicates.keys())[0]])
        self.assertIn(self.test_images[3], duplicates[list(duplicates.keys())[0]])


if __name__ == '__main__':
    unittest.main()
