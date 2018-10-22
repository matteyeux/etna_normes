#!/usr/bin/python3
#-*- coding:utf-8 -*-
## ETNA PROJECT, 22-10-2018 by hauteb_m
## project_name
## File description: 
##     project_description
##

import sys

def check_for_spaces(c_file):
    with open(file_to_test, 'r') as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            i += 1
            if line.endswith(" \n"):
                print("space at the EoL : %d" % i)
"""
def check_for_var_dec(c_file):
    with open(file_to_test, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            for i in range(0, len(lines[i]):
                if 
"""

def check_for_tabs(c_file):
    with open(c_file, "r") as file:
        this = file.read()
        line = 0
        for i in range(0, len(this)):
            if this[i] == '\n':
                line += 1
            if this[i] == '\t':
                print("found tab line : %d" % line)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage : norme.py [C file]")
        sys.exit(1)

    file_to_test = sys.argv[1]
    check_for_tabs(file_to_test)
    #check_for_spaces(file_to_test)
