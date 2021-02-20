import os
from typing import List


def find_files(suffix, path) -> List[str]:
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    if not suffix:
        raise Exception("suffix is not valid")

    if not path.startswith("./"):
        raise Exception("path is not valid")

    file_paths = []

    def _find_files(inner_path):
        for sub_path in os.listdir(inner_path):
            current_path = inner_path + "/" + sub_path
            if os.path.isfile(current_path):
                if current_path.endswith(suffix):
                    file_paths.append(current_path)
            else:
                _find_files(current_path)

    _find_files(path)
    return file_paths


files = find_files(".c", "./testdir")

valid_path = [
    "./testdir/subdir1/a.c",
    "./testdir/subdir3/subsubdir1/b.c",
    "./testdir/subdir5/a.c",
    "./testdir/t1.c"
]

print("\nfind_files result:")

print("\nexpected paths:")
for path in valid_path:
    print(path)

print("\nactual paths:")
files.sort()
for file in files:
    print(file)

print()
try:
    find_files("", "./")
except Exception:
    print("throws exceptions for invalid suffix")

try:
    find_files(".c", "")
except Exception:
    print("throws exception for empty path")
