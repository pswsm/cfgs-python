import argparse
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from jinja2.environment import Template


def mkArgs():
    parser = argparse.ArgumentParser(
        description='From a given list of friends, make an invitation text for each of them.')
    parser.add_argument(
        '-f', '--friend', nargs='+', help='A list of friends.', required=True)
    parser.add_argument(
        '-i', '--templateDir', help='Where template files are located', type=Path, default='template.txt', required=True)
    parser.add_argument(
        '-if', '--templateName', help='Filename of the template', type=str, required=True)
    parser.add_argument('-o', '--outputDir', help='Output directory',
                        type=Path, default='textOut/')
    parser.add_argument('-of', '--outputFile', help='Output file',
                        type=str, default='output')
    parsed_args = parser.parse_args()
    return parsed_args


def jinjaCreate(names: list[str]) -> dict[list[dict[str, str]]]:
    namesDict: list[[dict[str, str]]] = []
    for name in names:
        namesDict.append({'name': name})
    finalDict: dict[list[dict[str, str]]] = {'friends': namesDict}
    return finalDict


def fillTemplate(stringsDict: list[dict[str, str]], templateDir, templateName) -> str:
    env: Environment = Environment(loader=FileSystemLoader(
        templateDir), autoescape=select_autoescape())
    template:   Template = env.get_template(templateName)
    filledTemplate: str = template.render(stringsDict)
    return filledTemplate


if __name__ == '__main__':
    args = mkArgs()
    friends = jinjaCreate(args.friend)
    args.outputDir.mkdir(exist_ok=True)
    for dictionary in friends['friends']:
        # for name in friends:
        text = fillTemplate(dictionary, args.templateDir, args.templateName)
        outPath: Path = args.outputDir / \
            (args.outputFile + f"{dictionary['name']}.txt")
        outPath.write_text(text)
