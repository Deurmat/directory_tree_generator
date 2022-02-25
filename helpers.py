import os

def dir_contents(dir: str, incl_subdir=True, incl_files=True) -> tuple[list, list]:
    files = [item for item in os.listdir(dir) if os.path.isfile(os.path.join(dir, item))]
    dirs = [item for item in os.listdir(dir) if os.path.isdir(os.path.join(dir, item))]

    match [incl_files, incl_subdir]:
        case [True, True]:
            return files, dirs
        case [True, False]:
            return files, []
        case [False, True]:
            return [], dirs
        case [True, False]:
            return [], []

def print_dir_contents():
    pass

def export_dir_contents():
    pass