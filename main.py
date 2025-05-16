from stats import get_book_word_count
from stats import count_characters
from stats import sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1] 
        book_text = get_book_text(book_path)
        word_count = get_book_word_count(book_text)
        list = sort_dict(count_characters(book_text))
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for i in list:
            print(f"{i["char"]}: {i["num"]}")
        print("============= END ===============")
