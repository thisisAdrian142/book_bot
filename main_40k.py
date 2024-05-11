## OBJECTIVE ##

## Print the whole list of characters that appears in 40k novel ##

## Functions structure ##

# read the book
def main():
    book_path = 40k_books_bot/astrum_militarum.txt 
    with open(book_path) as f:
        read_book = f.read()
        print(read_book)

main()
