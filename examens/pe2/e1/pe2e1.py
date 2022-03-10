# @Author: Pau Figueras <pswsm>
# @Email:  pau@pswsm.cat

import argparse
from pathlib import Path

def mkArgs():
    parser = argparse.ArgumentParser(
        description='Get size from given directory.')
    parser.add_argument(
        'basedir', help='Base directory to make tree.', type=Path)
    parser.add_argument(
        '-g', '--glob', help='Glob to search for files. Must be quoted.', type=str, default='**/*')
    parser.add_argument(
        '-l', '--showfiles', help='Shows found files.', action='store_true')
    parsed_args = parser.parse_args()
    return parsed_args

def getTree(basedir: Path, globe) -> tuple[list[Path], list[Path]]:
    """Lists all files from all subdirectories from the given base directory
       and returns them as a list of Paths"""
    root: Path = basedir
    pathsInRoot: list[Path] = list(root.glob(globe))
    dirsInRoot:  list[Path] = [dirct for dirct in pathsInRoot if dirct.is_dir()]
    filesInRoot: list[Path] = [file for file in pathsInRoot if file.is_file()]
    return dirsInRoot, filesInRoot

def getSize(fileList: list[Path]) -> tuple[int, float, float, list[tuple[Path, int]]]:
    """From a list of filepaths, gets all sizes and returns the as Byte sizes, KB sizes and MB sizes."""
    files: list[Path] = fileList.copy()
    sizes: list[int] = [directory.stat().st_size for directory in files]
    eachFileSize = list(zip(files, sizes))
    totalByteSize: int = sum(sizes)
    totalKBSize: float = totalByteSize / 1024
    totalMBSize: float = totalByteSize / 1048576
    return totalByteSize, totalKBSize, totalMBSize, eachFileSize

def recurse2Dirs(targetDirs: list[Path]) -> dict[str, list[Path]]:
    dirs: list[Path] = targetDirs.copy()
    files: dict[str, list[Path]] = {str(dirname): [file for file in list(dirname.glob('*')) if file.is_file()] for dirname in dirs}
    return files

def main(args):
    rootDirs, rootFiles = getTree(args.basedir, args.glob)
    print(recurse2Dirs(rootDirs))

if __name__ == '__main__':
    args = mkArgs()
    main(args)
