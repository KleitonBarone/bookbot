def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def count_letter_occurrences(text):
    text = text.lower()
    letters = {}
    for word in text.split():
        for letter in word:
            if not letter.isalpha():
                continue
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters

def dictionary_to_list_of_dictionaries(dictionary):
    return [{"key": key, "value": value} for key, value in dictionary.items()]

def sort_on_value(dictionary):
    return dictionary["value"]

def print_report(path_to_file, word_count, letter_count_list):
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document")
    print("")
    for letter in letter_count_list:
        print(f"The {letter['key']} character was found {letter['value']} times")
    print("--- End report ---")

def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_book_text(path_to_file)
    word_count = get_word_count(file_contents)
    letter_count = count_letter_occurrences(file_contents)
    letter_count_list = dictionary_to_list_of_dictionaries(letter_count)
    letter_count_list.sort(key=sort_on_value, reverse=True)
    print_report(path_to_file, word_count, letter_count_list)


main()
