import mmap
import re
import sys

words_path = 'words.txt'

if sys.version_info[0] == 2:
    # sigh.
    input = raw_input

def main():
    while True:
        regex = input("Regex: ")
        regex = '^' + regex + '$'
        print("Matching words:")
        with open(words_path) as f:
            for line in f:
                line = line[:-1] # remove \n
                if re.match(regex, line, flags=re.IGNORECASE):
                    # `print('\t', line)` will not work well for python2
                    print('\t'+line)
        print("=====")

if __name__ == '__main__':
    main()
