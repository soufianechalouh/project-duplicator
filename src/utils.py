import os
import shutil

import chevron
from rendering import rendering


def render_file(file_path, rules):
    with open(file_path, 'r+') as f:
        rendered_text = chevron.render(f, rules)
        f.seek(0)
        f.truncate()
        f.write(rendered_text)


def render_tree(tree_path, rules):
    directory = os.fsencode(tree_path)
    files_list = os.listdir(directory)
    for file in files_list:
        file_path = f"{tree_path}/{file.decode('utf-8')}"
        if os.path.isdir(f"{file_path}"):
            render_tree(file_path, rules)
        else:
            render_file(file_path, rules)


def make_a_twin(source, destination):
    try:
        shutil.copytree(source, destination)
    except FileExistsError:
        print("Exception: Folder exists already. please delete it and re-run the program")
        exit()
    except Exception as e:
        print(e)
        exit()
    render_tree(destination, rendering)
