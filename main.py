def get_book_text(path):
    with open(path) as f:
        return f.read()

def main() :
    path_to_file = "books/frankenstein.txt"
    file_contents = get_book_text(path_to_file)
    print(file_contents)

main()
