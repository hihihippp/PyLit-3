#!/usr/bin/env python
#
# :Copyright: 2007 Riccardo Murri, Guenter Milde.
#             Released under the terms of the GNU General Public License
#             (v. 2 or later)

# 99bottles.py
# ============
# Introductory Example to Literate Programming
# ++++++++++++++++++++++++++++++++++++++++++++
#
# Print the famous `99 bottles of beer` song lyrics
#
#
# This was used as an introductory example to literate programming
# in the (no longer available) `LiteratePrograms.org Wiki`.
#
# The lyrics
# ----------
#
# We take the lyrics from the Wikipedia, which says in the
# `99 bottles of beer`_ entry:
#
# The verse format is very formulaic, and can be expressed as follows:
#
# From 99 down to 1::

verse_template = """
<number> bottles of beer on the wall
<number> bottles of beer!
Take one down, pass it around
<number - 1> bottles of beer on the wall!"""

# There is much variation in the final verse. One common final verse (which
# could potentially cause an infinite-loop motif) is::

final_verse = """
No bottles of beer on the wall!
No bottles of beer!
Go to the store and buy some more
99 bottles of beer on the wall!"""

# The Python program
# ------------------
#
# There are a countless number of ways to implement a program that prints the
# whole song in Python. The following examples uses a `for` loop and the
# `replace` method of string objects.
#
# Basic version
#
# Count down from 99 to 1 and print the verses::

def print_verses_1(start_number=99):
    for number in range(start_number, 0, -1):
        verse = verse_template.replace("<number>", str(number))
        print(verse.replace("<number - 1>", str(number-1 or "No")))

# Consider the singular case
#
# There is one problem left, we should check whether to print 'bottles' or
# 'bottle'.
#
# An improved version will replace the "bottles" with a construct that
# takes into account the actual number of bottles::

def print_verses_2(start_number=99):
    for number in range(start_number, 0, -1):
        verse = verse_template.replace("<number>", str(number))
        verse = verse.replace("bottles", "bottle" + plural_suffix(number))
        print(verse.replace("<number - 1>", str(number-1 or "No")))

# where an auxiliary function returns the matching suffix (or not)::

def plural_suffix(number):
    if number != 1:
        return "s"
    else:
        return ""

# Still, the last line come out wrong, as here we have <number-1> bottles. To
# treat this case we either could split the last line and treat it differently,
# or use a modified template as e.g. ::

verse_template_2 = """
<number> bottle<s> of beer on the wall
<number> bottle<s> of beer!
Take one down, pass it around
<number - 1> bottle<s> of beer on the wall!"""

# together with::

def print_verses_3(start_number=99):
    for number in range(start_number, 0, -1):
        verse = verse_template_2.replace("<number>", str(number))
        verse = verse.replace("<s>", plural_suffix(number), 2)
        verse = verse.replace("<s>", plural_suffix(number-1), 1)
        print(verse.replace("<number - 1>", str(number-1 or "No")))


# Command line use
# ----------------
#
# Print the lyrics if this script is called from the command line::

if __name__ == "__main__":
    print_verses_3()
    print(final_verse)


# .. _99 bottles of beer: http://en.wikipedia.org/wiki/99_Bottles_of_Beer
# .. .. _LiteratePrograms.org Wiki:
#        http://en.literateprograms.org/LiteratePrograms:Welcome
