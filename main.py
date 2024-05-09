def get_num_words(book_to_string):
    words = book_to_string.split()
    return len(words)


def get_num_letters(book_to_string):
    counter = {}
    convert_words = book_to_string.lower()
    for letter in convert_words:
        if ' ' == letter:
            continue
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

# ! count how often each character appears in given text.
def get_chars_dict(book_to_string):
    set_chars = {}
    for c in book_to_string:
        lowered = c.lower()
        if lowered in set_chars:
            set_chars[lowered] += 1
        else:
            set_chars[lowered] = 1
    return set_chars


def main():
    book_path = "books/frankenstein.txt"
    book_to_string = get_book_text(book_path)
    num_words = get_num_words(book_to_string)
    num_letters = get_num_letters(book_to_string)
    
    char_dict = get_chars_dict(book_to_string)
    chars_sorted_list = chars_dict_to_sorted_list(char_dict)

    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print(f"--- End report ---")


def get_book_text(path):
    with open(path) as file:
        return file.read()

main()
