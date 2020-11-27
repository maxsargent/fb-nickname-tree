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

def get_json_files(directory):
    json_files = sorted_alphanumeric([pos_json for pos_json in os.listdir(directory) if pos_json.endswith('.json')])
    json_files.reverse()

    return json_files

def match_nickname_change(message_content):
    pass

def extract_nickname(message_content):
    pass

def generate_participants(json_files, in_directory):
    participants_list = []

    for f in json_files:
        with open(os.path.join(in_directory, f)) as json_file:
            json_text = json.load(json_file)

            messages = json_text['messages']

            for message in messages:
                participants_list.append(message['sender_name'])
    
    participants_list = sorted(list(dict.fromkeys(participants_list)))
    
    return participants_list

def generate_nicknames(json_files, in_directory):
    nickname_change_list = []

    for f in json_files:
        with open(os.path.join(in_directory, f)) as json_file:
            json_text = json.load(json_file)

            messages = json_text['messages']

            for message in messages:
                if 'content' in message:
                    if match_nickname_change(message['content']):
                        nickname_change_list.append(extract_nickname(message['content']))
    
    return nickname_change_list

def generate_graph(json_files, in_directory):
    participants = generate_participants(json_files, in_directory)
    nicknames = generate_nicknames(json_files, in_directory)


def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('indirectory', help="Input Chat Directory", type=dir_path)
    parser.add_argument('-o', '--outfile', help="Output file",
                        default=sys.stdout, type=argparse.FileType('w'))

    args = parser.parse_args(arguments)
    in_directory = args.indirectory

    json_files = get_json_files(in_directory)
    generate_graph(json_files, in_directory)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))