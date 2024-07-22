def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text, count_all_chars=False)
    converted_list = dict_to_list(chars_dict)
    converted_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for item in converted_list:
        print(f"The '{item['letter']}' character was found {item['num']} times")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text, count_all_chars=True):
    chars = {}
    for c in text:
        lowered = c.lower()
        if count_all_chars or lowered.isalpha():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars


def dict_to_list(chars_dict):
    list_of_dicts = []
    for c in chars_dict:
        char_dict = {"letter": c, "num": chars_dict[c]}
        list_of_dicts.append(char_dict)
    return list_of_dicts


def sort_on(char_dict):
    return char_dict["num"]


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()