from src.utils import make_a_twin


def main():
    did_configure = input("Did you configure your renderer in renderer.py file? please type Yes or Y if you did")
    if did_configure.upper().strip() not in ["YES", "Y"]:
        print("please configure renderer.py and restart this program")
        exit()
    project_to_duplicate = input("Please type the path to the file/directory you want to duplicate")
    dest = input("Please type the destination path")
    make_a_twin(project_to_duplicate, dest)


if __name__ == '__main__':
    main()
