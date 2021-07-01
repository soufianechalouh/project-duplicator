import os
import unittest

from tests.rendering import rendering


class TestUtils(unittest.TestCase):

    test_file_path = "./sample_template_file.txt"

    def setUp(self):
        with open(self.test_file_path, "w") as f:
            f.write('Sample {{old_text}}')

    def test_render_file(self):
        render_file(self.test_file_path, rendering)
        with open(self.test_file_path, "r") as f:
            self.assertIn("new_text", f.read())

    def tearDown(self):
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)
