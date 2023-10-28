# -*- coding: utf-8 -*-
"""
Task 7.2b

Modify the script from task 7.2a: instead of printing to the standard output,
the script should write the received lines to a file.

File names should be passed as script arguments:
 * name of the source configuration file
 * name of the final configuration file

At the same time, lines that are contained in the ignore list and lines starting with '!' should be filtered out.

Constraint: All tasks must be completed using only covered topics.
"""

from sys import argv

ignored_words = ["duplex", "alias", "configuration"]
source_file = argv[1]
output_file = argv[2]

with open(source_file) as source, open(output_file, 'w') as destination:
    for line in source:
        if line[0] == '!':
            continue
        contains_ignored_word = False
        for ignored_word in ignored_words:
            if ignored_word in line:
                contains_ignored_word = True
                break
        if not contains_ignored_word:
            destination.write(line)
