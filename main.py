def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

def get_num_words(text):
    words = text.split()
    return len(words)

def count_letter(text)):
    convert = text.lower()
    convert_no_duplicate = set(convert)
    return count(convert_no_duplicate)

def get_book_text(path):
    with open(book_path) as file:
        return file.read()
