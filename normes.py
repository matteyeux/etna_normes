#!/usr/bin/python3
#-*- coding:utf-8 -*-
## ETNA PROJECT, 22-10-2018 by hauteb_m
## normes
## File description: 
##     check for ETNA normes. Love u Samantha <3
##

import sys

def check_for_spaces(c_file):
    with open(file_to_test, 'r') as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            i += 1
            if line.endswith(" \n"):
                print("[line %d] space at EoL" % i)

def check_for_return(c_file):
    with open(c_file, "r") as f:
         lines = f.readlines()
         for i in range(0, len(lines)):
            if "return" in lines[i]:
                if "return (" in lines[i]:
                    True #print("good")
                elif "return(" in lines[i]:
                    print("[line %d] no space after return" % (i+1))
                else:
                    print("[line %d] not parentheses found for return" % (i+1))

def check_for_tabs(c_file):
    with open(c_file, "r") as file:
        this = file.read()
        line = 0
        for i in range(0, len(this)):
            if this[i] == '\n':
                line += 1
            if this[i] == '\t':
                print("[line %d] found tab line" % line)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage : norme.py [C file]")
        sys.exit(1)

    file_to_test = sys.argv[1]
    check_for_tabs(file_to_test)
    check_for_spaces(file_to_test)
    check_for_return(file_to_test)
