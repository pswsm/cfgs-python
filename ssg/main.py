#! /usr/bin/env python3

"""
SSG v09.1.1
- Changed how files are handled
- Arguments now directly handled by cmdline.py
- Files keep their original name, since each .md is written in a differetn file
- Modularized the main function
- Changed variables name
"""

from pathlib import Path
from typing import Iterator

import shutil, cmdline, engine


# -----------------------------------------------------------------------------
def mkDirs(inputDir: Path, outputDir: Path) -> None:
    """Creates outputDir and copies arbitrary folders inside inputDir to the outputDir"""

    outputDir.mkdir(exist_ok=True)
    shutil.copytree(inputDir/"css", outputDir/"css", dirs_exist_ok=True)
    shutil.copytree(inputDir/"img", outputDir/"img", dirs_exist_ok=True)

def readMdFiles(inputDir: Path) -> tuple[list[Path], list[str]]:
    """Returns the filenames and filepaths of markdown files from given inputDir"""

    mdDir:           Path          = inputDir/"md"
    mdFilepathIter: Iterator[Path] = mdDir.glob("*.md")
    mdFilepathList: list[Path]     = sorted(mdFilepathIter, reverse=True)
    mdFilenames: list[str]         = [filename.stem for filename in mdFilepathList if filename.is_file()]

    return mdFilepathList, mdFilenames

def mkMdMetadata(mdFilepaths: list[Path]) -> tuple[list[str], list[dict]]:
    """From a list of markdown filepaths, returns metadata and its contents coneverted to html"""

    mdStrList:    list[str]  = [path.read_text() for path in mdFilepaths]
    htmlStrList:  list[str]  = [engine.convert_md_to_html(mdStr) for mdStr in mdStrList]
    metadataList: list[dict] = [engine.get_md_metadata(mdStr) for mdStr in mdStrList]

    return htmlStrList, metadataList

def main(inputDir: Path, outputDir: Path) -> None:
    """Reads a markdown file and writes its html conversion.
       inputDir is the Path where resources (template, css, js, md) are located
       outputDir is the Path where resources will be written"""

    # Creates variables
    filepaths, filenames = readMdFiles(inputDir)
    mkDirs(inputDir, outputDir)
    stringList, metadataList = mkMdMetadata(filepaths)

    # Fill template with entries (html, metadata)
    template_dir:      Path = inputDir/"html"
    template_filename: str  = "template.html"

    # Loops trought each and creates each file.
    for (html, meta, counter) in zip(stringList, metadataList, range(len(filenames))):
        vars_dict: dict = {"html_list": html, "meta_list": meta}
        html_str: str   = engine.fill_template(template_dir, template_filename, vars_dict)
        filename: str   = f"{filenames[counter]}.html"
        (outputDir / filename).write_text(html_str)


# -----------------------------------------------------------------------------
if __name__ == "__main__":

    args = cmdline.parse_args()

    inputDir, outputDir = args.inputDir, args.outputDir

    main(inputDir, outputDir)

# -----------------------------------------------------------------------------
