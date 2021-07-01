import chevron


def render_file(file_path, rules):
    with open(file_path, 'r+') as f:
        rendered_text = chevron.render(f, rules)
        f.seek(0)
        f.truncate()
        f.write(rendered_text)


def render_tree(tree_path, rules):
    pass
