import os

import chevron


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
