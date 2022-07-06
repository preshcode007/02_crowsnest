#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2022-06-24
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

# the name used in the first parameter which is (word) in our case,
# is super important in our parsing process. it is the prg's first,
#  positional argument
    parser.add_argument('word',
                        metavar='name',
                        help='The thing that we will announce')

    parser.add_argument('-s', '--side', metavar='boat side', help='what side of the boat?',
                        default='larboard'
                        )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # since we will be using args.word alot, we can simply put it in a variable
    word = args.word
    side = args.side

    vowel = "aeiou"
    vowel_upper = vowel.upper()
    consonant = "bcdfqhjklmnpqrstvwxyz"
    consonant_upper = consonant.upper()

    article = "an" if word[0].lower() in vowel else "a"
    # if word[0] in vowel_upper:
    #     article = "An"
    # elif word[0] in consonant_upper:
    #     article = "A"
    if word[0] in vowel:
        article = "an"
    elif word[0] in consonant:
        article = "a"





    print(f"Ahoy, Captain, {article} {word} off the {side} bow!")


# --------------------------------------------------
if __name__ == '__main__':
    main()
