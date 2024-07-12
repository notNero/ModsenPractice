import unittest
from unittest.mock import patch, MagicMock
from image_browser import ImageBrowser


class TestImageBrowser(unittest.TestCase):
    @patch('image_browser.ImageTk.PhotoImage')
    @patch('image_browser.Image.open')
    @patch('image_browser.tk.Canvas')
    def test_show_images(self, mock_canvas, mock_open, mock_photo):
        # Mocking image open and PhotoImage
        mock_img = MagicMock()
        mock_open.return_value = mock_img
        mock_photo.return_value = MagicMock()

        # Mocking Canvas
        mock_canvas_instance = MagicMock()
        mock_canvas.return_value = mock_canvas_instance

        # Create a fake set of duplicates
        duplicates = {'hash1': ['img1.png', 'img2.png']}

        # Initialize the ImageBrowser with the fake duplicates
        app = ImageBrowser(duplicates)

        # Track original counts of calls before invoking show_images
        initial_open_call_count = mock_open.call_count
        initial_photo_call_count = mock_photo.call_count
        initial_create_image_call_count = mock_canvas_instance.create_image.call_count

        # Call the show_images method
        app.show_images()

        # Check if Image.open and ImageTk.PhotoImage are called correctly
        self.assertTrue(mock_open.called)
        self.assertTrue(mock_photo.called)

        # Check if the number of times images are processed matches expected calls
        self.assertEqual(mock_open.call_count - initial_open_call_count, 2)
        self.assertEqual(mock_photo.call_count - initial_photo_call_count, 2)

        # Check if the canvas create_image method was called
        self.assertTrue(mock_canvas_instance.create_image.called)

        # Ensure that create_image was called for both images
        self.assertEqual(mock_canvas_instance.create_image.call_count - initial_create_image_call_count, 2)


if __name__ == '__main__':
    unittest.main()
