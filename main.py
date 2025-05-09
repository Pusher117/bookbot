from stats import get_book_text,count_words,char_count,sort
import sys


def main(): 
    if len(sys.argv) !=2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text=get_book_text(file_path)
    word_count=count_words(book_text)
    char_counts=char_count(book_text)
    sorted_chars=sort(char_counts)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {file_path}')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()