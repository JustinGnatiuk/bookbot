import sys

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
            print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

        

def get_sorted_list_from_dict(dict):

    char_dict_list = [{'character': k, 'count': v} for k, v in dict.items()]
    char_dict_list.sort(reverse=False, key=sort_on)

    return char_dict_list

def sort_on(dict):
    return dict["character"]

def get_book_text(path):

    with open(path) as f:
        return f.read()

    
def word_count(book):

    words = book.split()

    return len(words)

def get_character_dict(book):

    character_count = {}

    for letter in book:

        letter = letter.lower()

        if letter in character_count:
            character_count[letter] += 1
        else:
            character_count[letter] = 1

    return character_count


main()
