from typing import List
from pathlib import Path

class Parser(object):
    """docstring for Parser."""
    extensions: List[str] =[]

    def valid_extensions(self, extension):
        return extension in self.extensions

    def parse(path:Path, source:Path, dest:Path)
        raise NotImplementedError
