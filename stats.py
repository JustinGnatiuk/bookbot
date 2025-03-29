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
