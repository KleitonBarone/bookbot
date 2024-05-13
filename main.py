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
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters

def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_book_text(path_to_file)
    word_count = get_word_count(file_contents)
    letter_count = count_letter_occurrences(file_contents)
    print(word_count)
    print(letter_count)

main()
