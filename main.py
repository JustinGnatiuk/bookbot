import sys
from stats import *
def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)

    char_dict = get_character_dict(text)

    char_dict_list = get_sorted_list_from_dict(char_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count(text)} words found in the document")
    
    for dict in char_dict_list:
        if dict["character"].isalpha():
            char = dict["character"]
            count = dict["count"]
            print(f"{char}: {count}")

    print("--- End report ---")

main()
