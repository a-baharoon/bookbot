def count_book_words(book_text): 
    return len(book_text.split())

def count_book_chars(book_text):
    book_text = book_text.lower()
    book_chars_count = {}

    for char in book_text:
        if char not in book_chars_count:
            book_chars_count[char] = 1
        
        elif char in book_chars_count:
            book_chars_count[char] += 1 
            
    return book_chars_count

def sort_dict(dict):
        return dict["num"]
    
def format_chars(stats_dict):
    stats = [] 
    for key in stats_dict: 
        stats.append({"char": key, "num": stats_dict[key]})
        
    stats.sort(reverse=True, key=sort_dict)
    
    return stats 
    

'''
Add a new function to your stats.py file that takes the dictionary of characters and their counts and returns a sorted list of dictionaries.

Each dictionary should have two key-value pairs: one for the character itself and one for that character's count (e.g. {"char": "b", "num": 4868}).
'''
    
# we have a dictionary that contains count = {"a": 40287, "b": 287} etc.

# we want to split into a list to be 
# count = [{"char": "a", "num:" 40287}] , [{"char": "b", "num:" 287}] etc.

'''
here is the algorithm basically:
    1- iterate through book_count_dict dictionary 
    2- create a temp_dictionary 
    3- take its key and put it as the value of char: of temp_dictionary 
    4- take its value and put it as the second element of temp_dictionary 
    5- add the newly generated dictionary into the list[i]
    6- go back to step 1
'''





