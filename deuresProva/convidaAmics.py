import engine
from pathlib import Path
import argparse


def mkArgs():
    parser = argparse.ArgumentParser(
        description='From a given list of friends, make an invitation text for each of them.')
    parser.add_argument(
        'friendList', help='A list of friends. Must be a python list', type=list[str])
    parser.add_argument(
        'templateDir', help='Where template files are located', type=Path)
    parser.add_argument(
        'templateName', help='Filename of the template', type=str)
    parser.add_argument('outputDir', help='Output directory',
                        type=Path, default='textOut/')
    parsed_args = parser.parse_args()
    return parsed_args


if __name__ == '__main__':
    args = mkArgs()
    engine.fill_template(args.templateDir, args.templateName, vars_dict)
