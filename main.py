from stats import count_book_words, count_book_chars

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    book_words_count = count_book_words(text)
    
    print("============ BOOKBOT ============")
    
    
    
    
    print(f"{book_words_count} words found in the document")
    print(count_book_chars(text))
    
    
    
    
    print("============= END ===============")
main()
