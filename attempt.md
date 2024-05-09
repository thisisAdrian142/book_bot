## My attempt

```
def get_num_words(text):
    words = book_to_string.split()
    return len(words)

def get_num_letter(text):
    counter = {}
    convert_words = book_to_string.lower()
    for letter in convert_words:
        if ' ' == letter:
            continue
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter

def main():
    book_path = "books/frankenstein.txt"
    book_to_string = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    print(f"{num_words} words found in the document")
    print(f"The {num_letters} character was found times")
    print(f"--- End report ---")

def get_book_text(path):
    with open(book_path, 'r') as file:
        return file.read()

```

## Correct solution:

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

---

### Core use of chars_dicts_to_sorted_list

#### convert a dictionary of character -> count into -> a sorted list of dictionaries.

#### Output: return a list of dicitonaries, each contain a char & its freq, sort freq in ascending order.

- Input variable: "num_chars_dict"
- Set a list "[ ]"

### Core use of get_char_dicts

- Input the string
- Set a library "{ }"
- Convert all chars to lowercase -> iterate

```
if chars converted statement true:
    -> increase the counr of the char stored in 'lowered' by 1.
    <-> set_chars[lowered] += 1

```
