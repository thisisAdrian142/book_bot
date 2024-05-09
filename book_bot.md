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

## Correct implementation:

```
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

```
