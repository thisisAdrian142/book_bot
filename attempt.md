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
