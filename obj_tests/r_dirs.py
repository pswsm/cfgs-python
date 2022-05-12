# @Author: Pau Figueras <pswsm>
# @Email:  pau@pswsm.cat
from pathlib import Path
import argparse
import pprint as pp

def list_files(root_path: Path):
    files: list[Path] = []
    if root_path.is_file():
        files.append(root_path)

    if root_path.is_dir():
        paths_in_dir: list[Path] = list(root_path.glob("*"))
        for new_root in paths_in_dir:
            files.extend(list_files(new_root))

    final_files: list[str] = [str(file) for file in files]
    return final_files

def main():
    #  args = mkArgs()
    base_path: Path = Path("/home/pswsm/github/pswsm-repo/cpp/cppTests")
    fList: list[Path] = []
    fList.extend(list_files(base_path))
    pp.pp(fList)

main()
