from __future__ import annotations

class Folder():
    def __init__(self, dir: str, files: list = None, dirs: list = None):
        self._dir = dir
        self._containing_files = files if files is not None else []
        self._containing_dirs = dirs if dirs is not None else []
    
    def __str__(self):
        return f'Folder of dir {self.dir} with {str(len(self.containing_files))} files and {str(len(self.containing_dirs))} folders'

    @property
    def dir(self):
        return self._dir

    @property
    def containing_files(self):
        return self._containing_files

    @property
    def containing_dirs(self):
        return self._containing_dirs

    def add_containing_files(self, value: str):
        self._containing_files.append(value)

    def add_containing_dirs(self, value: Folder):
        self._containing_dirs.append(value)
    
