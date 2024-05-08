Attempt for 'Read file' & 'Count words' exercises

```
import sys

def main():
    with open(books/frankenstein.txt, 'r') as file:
        file_contents = file.read()

def count_words():
    with open(books/frankenstein.txt, 'r') as file:
        file_contents = file.read()
        count = 0
        words = file_contents.split()
        for words in file_contents:
            count++


if __name__ == "__main__":
    sys.exit(main())


```
