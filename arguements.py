# Write a program(WAP) in which you will be using a python argparse module to parse
# the input arguments. There will be three inputs 1) string 2) int 3) float
# Example >>python3 arguments.py hello 007 9.11
# [Name of the file should be argumnets.py](1point)

import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('input_string', type = str, help = 'String input')
    parser.add_argument('input_int', type = int, help = 'Int input')
    parser.add_argument('input_float', type = float, help = 'Float input')

    args = parser.parse_args()

    print("The string input was: ", args.input_string)
    print("The int input was: ", args.input_int)
    print("The float input was: ", args.input_float)

if __name__ == '__main__':
    main()