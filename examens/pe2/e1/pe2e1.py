"""Recurse into directories and show files sorted by size"""
# @Author: Pau Figueras <pswsm>
# @Email:  pau@pswsm.cat

import argparse
from pathlib import Path


def mk_args():
    """Generates the argumens"""
    parser = argparse.ArgumentParser(
        description='Get size from given directory.')
    parser.add_argument(
        'basedir', help='Base directory to make tree.', type=Path)
    parser.add_argument(
        '-g', '--glob', help='Glob to search for files. Must be quoted.',
        type=str, default='**/*')
    parser.add_argument(
        '-l', '--showfiles', help='Shows found files.', action='store_true')
    parsed_args = parser.parse_args()
    return parsed_args


def get_tree(basedir: Path, globe) -> tuple[list[Path], list[Path]]:
    """Lists all files from all subdirectories from the given base directory
       and returns them as a list of Paths"""
    root: Path = basedir
    paths_in_root: list[Path] = list(root.glob(globe))
    dirs_in_root:  list[Path] = [
        dirct for dirct in paths_in_root if dirct.is_dir()]
    files_in_root: list[Path] = [
        file for file in paths_in_root if file.is_file()]
    return dirs_in_root, files_in_root


def get_size(file_list: list[Path]) -> tuple[int, float, float, list[tuple[Path, int]]]:
    """
    From a list of filepaths, gets all sizes and returns them in bytes,
    kibibytes and mebibytes (base 2 not base 10).
    """
    files: list[Path] = file_list.copy()
    sizes: list[int] = [directory.stat().st_size for directory in files]
    each_file_size = list(zip(files, sizes))
    total_byte_size: int = sum(sizes)
    total_kb_size: float = total_byte_size / 1024
    total_mb_size: float = total_byte_size / 1048576
    return total_byte_size, total_kb_size, total_mb_size, each_file_size


def recurse_into_dirs(target_dirs: list[Path]) -> dict[str, list[Path]]:
    """
    Recurses into directories and searches for files.
    Returns a dictionary with the name of the folder as key, and a list
    with filenames as values.
    """
    dirs: list[Path] = target_dirs.copy()
    files: dict[str, list[Path]] = {str(dirname): [file for file in list(
        dirname.glob('*')) if file.is_file()] for dirname in dirs}
    return files


def main(arguments):
    """
    Runs the previous functions.
    """
    root_dirs, root_files = get_tree(arguments.basedir, arguments.glob)
    print(recurse_into_dirs(root_dirs))


if __name__ == '__main__':
    args = mk_args()
    main(args)
