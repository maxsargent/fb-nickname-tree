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
import re
import json

def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

def generate_participants(directory):
    json_files = sorted_alphanumeric([pos_json for pos_json in os.listdir(directory) if pos_json.endswith('.json')])
    json_files.reverse()

    participants_list = []

    for index, js in enumerate(json_files):
        with open(os.path.join(directory, js)) as json_file:
            json_text = json.load(json_file)

            messages = json_text['messages']

            for message in messages:
                participants_list.append(message['sender_name'])
    
    participants_list = sorted(list(dict.fromkeys(participants_list)))
    
    return participants_list

def generate_graph(directory):
    participants = generate_participants(directory)

    for participant in participants:
        nickname_dict = {}
        print(participant)

def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('indirectory', help="Input Chat Directory", type=dir_path)
    parser.add_argument('-o', '--outfile', help="Output file",
                        default=sys.stdout, type=argparse.FileType('w'))

    args = parser.parse_args(arguments)

    generate_graph(args.indirectory)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))