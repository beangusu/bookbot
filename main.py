from stats import (
    word_count,
    char_count,
    sort_chars,
)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    dictionary = char_count(text)
    sorted_chars = sort_chars(dictionary)
    print_report(book_path, num_words, sorted_chars)

def print_report(book_path, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
