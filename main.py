import sys
from stats import (
    count_words,
    chars_dict_to_sorted_list,
    get_chars_dict,
)

# get books
def main():
    #book_path = "books/frankenstein.txt"
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    #text = get_book_text(book_path)
    text = get_book_text(book_path)
    #words =  text.split()
    #from stats import count_words
    number_of_words = count_words(text)
    #from stats import get_chars_dict
    chars_dict = get_chars_dict(text)
    #from stats import sort_on
    #from stats import chars_dict_to_sorted_list
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, number_of_words, chars_sorted_list)

def print_report(book_path, number_of_words, chars_sorted_list):
    print("============ BOOKBOT =============")
    print(f"Analyzing book found at: {book_path}...")
    print("----------- Word Count -----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count --------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============ END =================")






    #for word in words:
        #number_of_words = len(words)

    #print(text)
    #print(f"{number_of_words} words found in the document")
    #print(chars_dict)




    
def get_book_text(path):
    with open(path) as f:
        return f.read()

main()

