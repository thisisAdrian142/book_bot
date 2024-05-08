### Attempt for 'Read file' & 'Count words' exercises

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

## Correct Answer:

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

### Count letters attempt:

```

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

def get_num_words(text):
    words = text.split()
    return len(words)

# count letters -> use count() function
def count_letter(text)):
    convert = text.lower()
    convert_no_duplicate = set(convert)
    return count(convert_no_duplicate)

def get_book_text(path):
    with open(book_path) as file:
        return file.read()

```
