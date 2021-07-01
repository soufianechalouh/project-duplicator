import os
import unittest

from tests.rendering import rendering


class TestUtils(unittest.TestCase):

    def setUp(self):
        with open("sample_template_file.txt", "w") as f:
            f.write('Sample {{old_text}}')

    def test_render_file(self):
        render_file("./sample_template_file.txt", rendering)
        with open("./sample_template.txt", "r") as f:
            self.assertIn("new_text", f.read())

    def tearDown(self):
        if os.path.exists("sample_template_file.txt"):
            os.remove("sample_test_file.txt")
