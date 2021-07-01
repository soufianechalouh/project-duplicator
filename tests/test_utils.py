import os
import shutil
import unittest
from pathlib import Path
from distutils.dir_util import copy_tree

from src.utils import render_file, render_tree
from tests.rendering import rendering


class TestUtils(unittest.TestCase):

    test_file_path = "sample_template_file.txt"
    test_copied_dir = "copied_dir"

    def setUp(self):
        with open(self.test_file_path, "w") as f:
            f.write('Sample {{old_text}}')
        Path("./template_dir_test/").mkdir(parents=True, exist_ok=True)
        with open(f"./template_dir_test/{self.test_file_path}", "w") as f:
            f.write('Sample {{old_text}}')

    def test_render_file(self):
        render_file(self.test_file_path, rendering)
        with open(self.test_file_path, "r") as f:
            self.assertIn("new_text", f.read())

    def test_render_directory(self):
        dst = self.test_copied_dir
        copy_tree("template_dir_test", dst)
        render_tree(dst, rendering)
        with open(f"./{self.test_copied_dir}/{self.test_file_path}", "r") as f:
            self.assertIn("new_text", f.read())

    def tearDown(self):
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)
        try:
            shutil.rmtree(self.test_copied_dir)
        except OSError as e:
            print("Error deleting folders: %s" % e.strerror)

