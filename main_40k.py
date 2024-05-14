# words count
def count_words(text_string):
    words = text_string.split()
    return len(words)

# special chars filter
def filter(freq):
    filter_freq = {key: value for key, value in freq.items() if key.isalpha()}
    return filter_freq

# letters count
def letters_count(text_string):
    lowercase_words = text_string.lower()
    freq = {}

    for characters in lowercase_words:
        if characters in freq:
            freq[characters] += 1
        else: 
            freq[characters] = 1
    return filter(freq)           

# read the book
def main():
    book_path = "books/frankenstein.txt" 
    with open(book_path) as f:
        read_book = f.read()
        #print(read_book)
        text_string = str(read_book)
        print("--- Begin report of books/frankenstein.txt ---")
        print(count_words(text_string), "words found in the document")
        print()        
        print()
#        listforthisstr = []
#        for item in :
#            if item.isalnum():
#                listforthisstr.append(item)
#        no_spec_chars = "".join(listforthisstr)
#        no_num_chars = "".join((num for num in no_spec_chars if not num.isdigit()))
#        for qualified_char in no_num_chars:
#            print(f"The ", qualified_char, "character was found many times")
        
#        for key, value in letters_count(text_string).items():
#            print(f"The ", key, "character was found", value, "times")

        freq_dict = letters_count(text_string)
        sorted_dict = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)
        for key, value in sorted_dict:
            print(f"The '{key}' character was found {value} times ")

        print("--- End report ---")

main()

