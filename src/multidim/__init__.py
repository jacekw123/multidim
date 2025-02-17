import os, shutil, sys


def copy():
    """ """
    try:
        path = sys.argv[1]
    except:
        path = "."
    # build lecture dir
    new_dir = os.path.join(path, "notebooks")
    lecture_dir = os.path.join(os.path.dirname(__file__), "notebooks")

    # check the path
    if not os.path.isdir(path):
        raise TypeError("%s is not a directory")

    shutil.copytree(lecture_dir, new_dir)
