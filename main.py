import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(book):
    return book.read()

from stats import get_word_count

from stats import get_char_count

from stats import sorted_dict

def main():
    with open(sys.argv[1]) as book:
        words = get_book_text(book)
        num_words = get_word_count(words)
        char_count = get_char_count(words)
        report = sorted_dict(char_count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for char_dict in report:
            for char, count in char_dict.items():
                if char.isalpha():
                    print(f"{char}: {count}")
        print("============= END ===============")

main()