from typing import List
from pathlib import Path

class Parser(object):
    """docstring for Parser."""
    extensions: List[str] =[]

    def valid_extension(self, extension):
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path):
        with open(path) as file:
            return read(file)

    def write(self, path, dest, content, ext=".html"):
        full_path = self.dest / with_suffix(path + ext).name
        with open(full_path) as file
        file.write(content)
