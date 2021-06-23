#!/usr/bin/python3
"""
Demo script for NNL class.

This script reads knight data from a file and displays it in various ways.
"""
from pprint import pprint

def main():
    """
    Program entry point.

    :return: None
    """
    data = read_file()
    print_ugly(data)
    print()
    print_pretty(data)
    print()
    print(get_field(data, 'Arthur', 2))
    print()
    print_names_and_titles(data)

def read_file():
    """
    Read knight data from text file into dictionary.

    :return: Dictionary of knight data.
    """
    knight_info = {}  # create empty dict

    with open("../DATA/knights.txt") as knights_in:  #open file
        for line in knights_in:  # read one line at a time
            name, title, color, quest, comment = line.rstrip().split(":") # strip and split line
            knight_info[name] = title, color, quest, comment  # add key/value to dict

    return knight_info  # return entire dict

def print_ugly(info):
    """
    Print dictionary using normal print() function.

    :param info: Dictionary of knight info
    :return: None
    """
    print(info)

def print_pretty(info):
    """
    Pretty-print dictionary of knight info

    :param info: Dictionary of knight info
    :return: None
    """
    pprint(info)

def get_field(info, knight, field):
    """
    Retrieve one field for a specified knight from the knight info dictionary

    :param info: Dictionary of knight data
    :param knight: Name of knight
    :param field: Field #
    :return: field value
    """
    return info[knight][field]

def print_names_and_titles(info):
    """
    Output knights and their titles, one per line.

    :param info: Dictionary of knight info
    :return: None
    """
    for knight_name, knight_data in info.items():
        print(knight_data[0], knight_name, knight_data[2])

main()  # call functions defined above