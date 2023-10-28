# -*- coding: utf-8 -*-
"""
Exercise 7.2a

Make a copy of the script for Exercise 7.2.

Enhance the script: The script should not print commands to the standard output that contain words from the ignore list.

Additionally, the script should not print lines that start with '!'.

Test the script on the configuration file config_sw1.txt.
The filename is passed as an argument to the script.

Note: All tasks must be performed using only the topics covered so far.

"""


from sys import argv

ignored_words = ["duplex", "alias", "configuration"]
input_file = argv[1]

with open(input_file) as file_handle:
    for code_line in file_handle:
        if code_line[0] == '!':
            continue
        contains_ignored_word = False
        for word in ignored_words:
            if word in code_line:
                contains_ignored_word = True
                break
        if not contains_ignored_word:
            print(code_line.rstrip())
