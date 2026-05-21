import sys
from stats import (
    word_count,
    char_count,
    sort_chars,
)

def get_booktext(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    text = get_booktext(sys.argv[1])
    print("---------- Word Count ----------")
    word_count(text)
    print("---------- Character Count -------")
    dictionary = char_count(text)
    sorted_list = sort_chars(dictionary)
    for char in sorted_list:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
        else:
            continue
    print("============== END ==============")
    
main()

