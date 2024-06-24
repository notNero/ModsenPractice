import unittest
from PIL import Image
import os
import tempfile
import shutil
from main import load_images_from_folder, compute_image_hash, find_duplicates

class TestImageDuplicates(unittest.TestCase):

    def setUp(self):
        # Создание временной директории с тестовыми изображениями
        self.test_dir = tempfile.mkdtemp()
        self.test_images = []
        for i in range(3):
            img = Image.new('RGB', (10, 10), color=(i*10, i*10, i*10))
            img_path = os.path.join(self.test_dir, f'test_img_{i}.png')
            img.save(img_path)
            self.test_images.append(img_path)

        # Создание дубликата одного из изображений
        img_dup = Image.new('RGB', (10, 10), color=(0, 0, 0))
        img_dup_path = os.path.join(self.test_dir, 'test_img_dup.png')
        img_dup.save(img_dup_path)
        self.test_images.append(img_dup_path)

    def tearDown(self):
        # Удаление временной директории и изображений после тестов
        shutil.rmtree(self.test_dir)

    def test_load_images_from_folder(self):
        images = load_images_from_folder(self.test_dir)
        self.assertEqual(len(images), 4)
        self.assertTrue(all(isinstance(img[1], Image.Image) for img in images))

    def test_compute_image_hash(self):
        img = Image.open(self.test_images[0])
        img_hash = compute_image_hash(img)
        self.assertIsInstance(img_hash, object)  # Проверка на корректный тип

    def test_find_duplicates(self):
        images = load_images_from_folder(self.test_dir)
        duplicates = find_duplicates(images)
        self.assertEqual(len(duplicates), 1)
        self.assertIn(self.test_images[0], duplicates[list(duplicates.keys())[0]])
        self.assertIn(self.test_images[3], duplicates[list(duplicates.keys())[0]])


if __name__ == '__main__':
    unittest.main()