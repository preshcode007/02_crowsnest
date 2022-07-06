#!/usr/bin/env python3
"""tests for crowsnest.py"""

""" OS module provides functions for the OS to work with.
    A subprocess in python is a task that the python delegates to the...
    Operating System
"""

import os
from subprocess import getstatusoutput, getoutput

prg = './crowsnest.py'
consonant_words = [
    'brigantine', 'clipper', 'dreadnought', 'frigate', 'galleon', 'haddock',
    'junk', 'ketch', 'longboat', 'mullet', 'narwhal', 'porpoise', 'quay',
    'regatta', 'submarine', 'tanker', 'vessel', 'whale', 'xebec', 'yatch',
    'zebrafish'
]
vowel_words = ['aviso', 'eel', 'iceberg', 'octopus', 'upbound']
template = 'Ahoy, Captain, {} {} off the larboard bow!'






# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'python3 {prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_consonant():
    """brigantine -> a brigantine"""

    for word in consonant_words:
        out = getoutput(f'python3 {prg} {word.lower()}')
        assert out.strip() == template.format('a', word.lower())


# --------------------------------------------------
def test_consonant_upper():
    """brigantine -> A Brigatine"""

    for word in consonant_words:
        out = getoutput(f'python3 {prg} {word.title()}')
        assert out.strip() == template.format('a', word.title())


# --------------------------------------------------
def test_vowel():
    """octopus -> an octopus"""

    for word in vowel_words:
        out = getoutput(f'python3 {prg} {word}')
        assert out.strip() == template.format('an', word)


# --------------------------------------------------
def test_vowel_upper():
    """octopus -> an Octopus"""

    for word in vowel_words:
        out = getoutput(f'python3 {prg} {word.upper()}')
        assert out.strip() == template.format('an', word.upper())

 # -----------------------------------------------------

def test_consonant_matchcase():
    """Brigantine -> A Brigatine
       brigantine -> a brigatine
    """
# how was this test achieved? you start from the docstring and see what you want your result to be like
    for word in consonant_words:
        case = "A" if word[0].isupper() else "a"

        out = getoutput(f'python3 {prg} {word.title()}')

        assert out.strip() == template.format(case, word.title())

#----------------------------------------------------------------------------------

def test_vowel_upper_matchcase():
    """octopus -> an octopus
       Octopus -> An Octopus
    """

    for word in vowel_words:
        case = "An" if word[0].isupper() else "an"
        out = getoutput(f'python3 {prg} {word.upper()}')
        assert out.strip() == template.format(case, word.upper())