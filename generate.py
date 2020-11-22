#!/usr/bin/env python3

"""
Generate a graphviz tree of facebook nicknames,
point the script to a directory of facebook chat 
history. Output location defaults to the input 
directory but can be modified.
"""

import os
import sys
import argparse

def generate_tree(directory):
    print(os.listdir(directory))

def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('indirectory', help="Input Chat Directory", type=dir_path)
    parser.add_argument('-o', '--outfile', help="Output file",
                        default=sys.stdout, type=argparse.FileType('w'))

    args = parser.parse_args(arguments)

    generate_tree(args.indirectory)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))