def count_book_words(book_text): 
    return len(book_text.split())

def count_book_chars(book_text):
    book_text = book_text.lower()
    
    book_chars_count = {}

    for char in book_text:
        
        if char not in book_chars_count:
            book_chars_count[char] = 1
        
        elif  char in book_chars_count:
            book_chars_count[char] += 1 
            
    return book_chars_count
        

    