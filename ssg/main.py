#! /usr/bin/env python3

"""
SSG v09.1.2
- Refactor
"""

from pathlib import Path
from typing import Iterator

import shutil
import cmdline
import engine


# -----------------------------------------------------------------------------
def mk_dirs(input_dir: Path, output_dir: Path) -> None:
    """Creates output_dir and copies arbitrary folders
       inside input_dir to the output_dir"""
    output_dir.mkdir(exist_ok=True)
    shutil.copytree(input_dir/"css", output_dir/"css", dirs_exist_ok=True)
    shutil.copytree(input_dir/"img", output_dir/"img", dirs_exist_ok=True)


def read_md_files(input_dir: Path) -> tuple[list[Path], list[str]]:
    """Returns the filenames and filepaths
       of markdown files from given input_dir"""
    md_dir: Path = input_dir/"md"
    md_filepath_iter: Iterator[Path] = md_dir.glob("*.md")
    md_filepath_list: list[Path] = sorted(md_filepath_iter, reverse=True)
    md_filenames: list[str] = [filename.stem for filename in md_filepath_list
                               if filename.is_file()]
    return md_filepath_list, md_filenames


def mk_md_metadata(md_filepaths: list[Path]) -> tuple[list[str], list[dict]]:
    """From a list of markdown filepaths,
       returns metadata and its contents coneverted to html"""
    md_str_list: list[str] = [path.read_text() for path in md_filepaths]
    html_str_list: list[str] = [engine.convert_md_to_html(mdStr)
                                for mdStr in md_str_list]
    metadata_list: list[dict] = [engine.get_md_metadata(mdStr)
                                 for mdStr in md_str_list]

    return html_str_list, metadata_list


def main(input_dir: Path, outpu_dir: Path) -> None:
    """Reads a markdown file and writes its html conversion.
       inputDir is the Path where resources (template, css, js, md) are located
       outputDir is the Path where resources will be written"""

    # Creates variables
    filepaths, filenames = read_md_files(input_dir)
    mk_dirs(input_dir, outpu_dir)
    string_list, metadata_list = mk_md_metadata(filepaths)

    # Fill template with entries (html, metadata)
    template_dir: Path = input_dir/"html"
    template_filename: str = "template.html"

    # Loops trought each and creates each file.
    for (html, meta, counter) in zip(string_list, metadata_list,
                                     range(len(filenames))):
        vars_dict: dict = {"html_list": html, "meta_list": meta}
        html_str: str = engine.fill_template(template_dir, template_filename,
                                             vars_dict)
        filename: str = f"{filenames[counter]}.html"
        (outpu_dir / filename).write_text(html_str)


# -----------------------------------------------------------------------------
if __name__ == "__main__":

    args = cmdline.parse_args()

    inputDir, outputDir = args.inputDir, args.outputDir

    main(inputDir, outputDir)

# -----------------------------------------------------------------------------
