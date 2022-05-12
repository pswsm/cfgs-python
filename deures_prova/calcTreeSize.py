# @Author: Pau Figueras <pswsm>
# @Date:   2022-02-17T15:52:54+01:00
# @Email:  pau@pswsm.cat
# @Last modified by:   pswsm
# @Last modified time: 2022-02-17T15:52:54+01:00

from pathlib import Path
import argparse


def getTree(basedir: Path, globe: str = '**/*') -> list[Path]:
    """Lists all files from all subdirectories from the given base directory
       and returns them as a list of Paths"""
    dir: Path = basedir
    pathsInDir: list[Path] = list(dir.rglob(globe))
    filesInDir: list[Path] = [file for file in pathsInDir if file.is_file()]
    return filesInDir


def getSize(fileList: list[Path]) -> tuple[int, float, float, list[tuple[Path, int]]]:
    """From a list of filepaths, gets all sizes and returns the as Byte sizes, KB sizes and MB sizes."""
    files: list[Path] = fileList.copy()
    sizes: list[int] = [file.stat().st_size for file in files]
    eachFileSize = list(zip(files, sizes))
    totalByteSize: int = sum(sizes)
    totalKBSize: float = totalByteSize / 1024
    totalMBSize: float = totalByteSize / 1048576
    return totalByteSize, totalKBSize, totalMBSize, eachFileSize


# if __name__ == '__main__':
def mkArgs():
    parser = argparse.ArgumentParser(
        description='Get size from given directory.')
    noKBwithMB = parser.add_mutually_exclusive_group()
    noKBwithMB.add_argument('-kb', '--kilobytes',
                            help='Returns size in Kilobytes', action='store_true')
    noKBwithMB.add_argument('-mb', '--megabytes',
                            help='Returns size in Megabytes', action='store_true')
    parser.add_argument(
        'baseTree', help='Base directory to make tree.', type=Path)
    parser.add_argument(
        '-g', '--glob', help='Glob to search for files. Must be quoted or double quoted.', type=str, default='**/*')
    parser.add_argument('-l', '--showfiles',
                        help='Shows found files.', action='store_true')
    parsed_args = parser.parse_args()

    return parsed_args

if __name__ == '__main__':

    parsed_args = mkArgs()

    files: list[Path] = getTree(parsed_args.baseTree, parsed_args.glob)
    sizeB, sizeKB, sizeMB, sizeFile = getSize(files)

    if parsed_args.showfiles:
        if parsed_args.kilobytes:
            print(f'Total 木 size is: {sizeKB}K\n')
            for key, value in sizeFile:
                print(f'{key}:\t{value} bytes')
        elif parsed_args.megabytes:
            print(f'Total 木 size is: {sizeMB}M\n')
            for key, value in sizeFile:
                print(f'{key}:\t{value} bytes')
        elif not parsed_args.kilobytes or not parsed_args.megabytes:
            print(f'Total 木 size is: {sizeB}B\n')
            for key, value in sizeFile:
                print(f'{key}:\t{value} bytes')
        else:
            print('Error :/')
    elif not parsed_args.showfiles:
        if parsed_args.kilobytes:
            print(f'Total 木 size is: {sizeKB}K\n')
        elif parsed_args.megabytes:
            print(f'Total 木 size is: {sizeMB}M\n')
        elif not parsed_args.kilobytes or not parsed_args.megabytes:
            print(f'Total 木 size is: {sizeB}B\n')
        else:
            print('Error :/')
    else:
        print('You did something really really wrong')
