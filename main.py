import os
import logging
from folders import Folder
from helpers import dir_contents

test_dir = r'C:\AMD\AMD_Radeon_Installer_21.6.1\Packages\Drivers'
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('__name__')
# print(dir_contents(directory, True)[1])

def dir_seeker(directory: str) -> Folder:
    files, directories = dir_contents(directory)
    if len(directories) == 0:
        return Folder(directory, files)
    else:
        fldr = Folder(directory, files)
        for sub_dir in directories:
            logger.debug(f'Working on dir {sub_dir} part of dir {directory}')
            sub_dir_path = os.path.join(directory, sub_dir)
            fldr.add_containing_dirs(dir_seeker(sub_dir_path))
        return fldr

if __name__ == '__main__':
    folder_result = dir_seeker(test_dir)
    print(folder_result)
    for f in folder_result.containing_dirs:
        print(f)
        # print(f.containing_dirs[0])