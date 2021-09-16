from itertools import permutations
import argparse
from pathlib import Path
from typing import List

def wordlist(path_to_wordlist):
    try:
        Path(path_to_wordlist).read_text()
    except:
        print(f'failed to read a file from path: {path_to_wordlist}')
        exit(-1)
    return path_to_wordlist

def permutation_int(l):
    if (int(l) <= 0):
        print(f'permutation\'s max length should be bigger than 0 but received: {l}')
        exit(-1)
    return l

def generate_permutation_at_length(wordlist_arr: List[str], permutation_length: int, is_verbose: bool):
    for p in permutations(wordlist_arr, permutation_length):
        generatedWord = '.'.join(p)
        if is_verbose:
            print(generatedWord)

def parse_args():
    parser = argparse.ArgumentParser(description='Generate simple permutations from words.', add_help=False)
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    # Add back help 
    optional.add_argument(
        '-h',
        '--help',
        action='help',
        default=argparse.SUPPRESS,
        help='show this help message and exit'
    )

    optional.add_argument("-l", help="max length of permutations", type=permutation_int)
    optional.add_argument("-e", help="exact permutation length to generate. if supplied, -l option is ignored.", type=permutation_int)
    required.add_argument("-w", help="path to input wordlist, each word separated by newline", type=wordlist)
    optional.add_argument("-v", help="verbose", action='store_true')
    args = parser.parse_args()

    wordlist_str = Path(args.w).read_text() 
    wordlist_arr = list(filter(lambda word : len(word.strip()) > 0, wordlist_str.split('\n')))
    permutation_max_length = - 1
    exaxct_permutation_length = -1

    if args.l:
        permutation_max_length = int(args.l)
    if args.e:
        exaxct_permutation_length = int(args.e)
    
    return (wordlist_arr, permutation_max_length, exaxct_permutation_length, args)

def generate_permutations(*allParams):
    (wordlist_arr, permutation_max_length, exaxct_permutation_length, args) = allParams
    if (exaxct_permutation_length and exaxct_permutation_length != -1):
        generate_permutation_at_length(wordlist_arr, exaxct_permutation_length, args.v)
    else:
        for permutation_length in range(1, permutation_max_length): 
            generate_permutation_at_length(wordlist_arr, permutation_length, args.v)

def run():
    parsed_args = parse_args()
    generate_permutations(*parsed_args)

run()
