#!/usr/bin/python3
#-*- coding:utf-8 -*-
## ETNA PROJECT, 22-10-2018 by hauteb_m
## normes
## File description: 
##     check for ETNA normes. Love u Samantha <3
##

# TODO : open file once, not in every function

import sys

# In ETNA's pool you have to set a specific
# header with your code

def check_needed_spaces(c_file):
    with open(c_file, "r") as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            if "){" in lines[i]:
                print("  [line %d] no space before curly bracket" % (i+1))
            if "if(" in lines[i]:
                print("  [line %d] no space between if and parenthese" % (i+1))
            if "for(" in lines[i]:
                print("  [line %d] no space between for and parenthese" % (i+1))
            if "while(" in lines[i]:
                print("  [line %d] no space between while and parenthese" % (i+1))


def check_for_editor_header(c_file):
     with open(c_file, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            if "ETNA PROJECT," in lines[i]:
                return True
        return False

def check_for_spaces(c_file):
    with open(c_file, 'r') as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            i += 1
            if line.endswith(" \n"):
                print("  [line %d] space at EoL" % i)

def check_for_return(c_file):
    with open(c_file, "r") as f:
         lines = f.readlines()
         for i in range(0, len(lines)):
            if "return" in lines[i]:
                if "return (" in lines[i]:
                    True #print("good")
                elif "return(" in lines[i]:
                    print("  [line %d]  no space after return" % (i+1))
                else:
                    print("  [line %d]  no parentheses found for return" % (i+1))

def check_for_tabs(c_file):
    with open(c_file, "r") as file:
        this = file.read()
        line = 0
        for i in range(0, len(this)):
            if this[i] == '\n':
                line += 1
            if this[i] == '\t':
                print("  [line %d] found tab line" % line)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage : norme.py [C file]")
        sys.exit(1)
    for i in range(1, len(sys.argv)):
        file_to_test = sys.argv[i]
        print("file : %s" % sys.argv[i])
        if check_for_editor_header(file_to_test) != True:
            print("  [ERROR] ETNA header not found")
        check_needed_spaces(file_to_test)
        check_for_tabs(file_to_test)
        check_for_spaces(file_to_test)
        check_for_return(file_to_test)
