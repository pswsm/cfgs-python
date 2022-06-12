"""
Commandline module: Parses command line arguments.
"""
from pathlib import Path
import argparse
import sys

# -----------------------------------------------------------------------------
def parse_args():
    """Generates the arguments using the argparse lib"""

    # Description
    description: str = "Reads markdown entries and writes them in an html blog."

    # Create parser
    parser = argparse.ArgumentParser(prog=sys.argv[0], description=description)

    # Define expected arguments
    parser.add_argument("-i", "--inputDir",  help="Input directory",  type=Path, required=True)
    parser.add_argument("-o", "--outputDir", help="Output directory", type=Path, required=True)

    # Parse program arguments
    parsed_args: argparse.Namespace = parser.parse_args()

    # Return arguments
    return parsed_args


# -----------------------------------------------------------------------------
