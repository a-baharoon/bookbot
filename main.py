import sys 
from stats import count_book_words, count_book_chars, format_chars, sort_dict

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    
    book_text = get_book_text(book_path)
    
    book_words_count = count_book_words(book_text)
    book_chars_count = count_book_chars(book_text)
    stats = format_chars(book_chars_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_words_count} total words")
    print("--------- Character Count -------")


    for i in range (len(stats)):
        if str.isalpha(stats[i]["char"]):
            print(stats[i]["char"] + ": " + str(stats[i]["num"]))


    print("============= END ===============")
main()
