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

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage : norme.py [C file]")
        sys.exit(1)

    file_to_test = sys.argv[1]
    check_for_spaces(file_to_test)
