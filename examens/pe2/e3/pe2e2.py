# @Author: Pau Figueras <pswsm>
# @Email:  pau@pswsm.cat

import sys, argparse, shutil
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from jinja2.environment import Template


def mkArgs():
    """Parses arguments if given, uses the defaults when not."""
    parser = argparse.ArgumentParser(
        description="Image visor in HTML. Powered by jinja2")
    parser.add_argument(
        '-f', '--filetype', help='Filetype (extension) of the image. Defaults to "jpg"', nargs='+', required=True)
    parser.add_argument(
        '-td', '--templateDir', help='Template file folder. Defaults to "templates/"', type=Path, default='templates/')
    parser.add_argument(
        '-tf', '--templateName', help='Filename of the template. Defaults to "template.html"', type=str, default='template.html')
    parser.add_argument(
        '-d', '--imageDir', help='Dir to search for images. Defaults to "img/"', type=Path, default='img/')
    parser.add_argument(
        '-od', '--outputDir', help='Where output file will be written. Defaults to "output/"', type=Path, default='output/')
    parser.add_argument(
        '-of', '--outputFile', help='Name of the file where jinja2 will write. Default to "index.html"', type=str, default='index.html')
    parser.add_argument(
        '-css', '--cssDirectory', help='Parent of css Folder (if any). If it is in the same directory, this value should be "./"', type=Path)
    parsedArgs = parser.parse_args()
    return parsedArgs

# This function was divided in two, but there was no need of that, since the last function was just pathDict.
def loadImgPath(fileExtensions: list[str], imageDir: Path) -> dict[str, list[Path]]:
    """Generates the dictionary wich will be used by jinja2 to create the html file.
       root: where the images are
       imgPath: a list populated with the filenames of the images included by the glob
       imgFullPath: a list with the full paths of the images
       pathDict: a dictionary ready for the jinja2 engine"""

    root: Path = imageDir
    imgPath: list[Path] = []
    for ext in fileExtensions:
        # This can't be done in a comprehension, which would be way cleaner.
        fileGlob: str = f"*.{ext}"
        imgPath.extend(list(root.glob(fileGlob)))
    
    imgFullPath: list[Path] = [image.resolve() for image in imgPath]
    
    pathDict: dict[str, list[Path]] = {"entries": imgFullPath}
    return pathDict


# A copypaste of Pablo's engine + some naming and type modification.
def fillTemplate(entries: dict[str, list[Path]], templateDir, templateName) -> str:
    """The engine of jinja. Loads the template and fills it."""
    env: Environment = Environment(loader=FileSystemLoader(
        templateDir), autoescape=select_autoescape())
    template:   Template = env.get_template(templateName)
    filledTemplate: str = template.render(entries)
    return filledTemplate

# Maybe wouldn't even need args as an arguments and could call mkArgs() inside, but idk no need for that.
def main(args):
    """Does everything, using the previous functions"""
    images: dict[str, list[Path]] = loadImgPath(args.filetype, args.imageDir)
    args.outputDir.mkdir(exist_ok=True)
    html: str = fillTemplate(images, args.templateDir, args.templateName) 
    writePath: Path = args.outputDir / args.outputFile
    writePath.write_text(html)
    if args.cssDirectory:
        shutil.copytree(args.cssDirectory/'css', args.outputDir/'css', dirs_exist_ok=True)
    
if __name__ == "__main__":
    args = mkArgs()
    #  print(args.filetype)
    main(args)
