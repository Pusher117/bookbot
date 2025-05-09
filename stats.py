
def get_book_text(file_path):
    with open (file_path) as f: 
        return f.read()

def count_words(text):
    words=text.split()
    return len(words)

def char_count(text):
    char_count = {}
    for char in text.lower():
            if char in char_count: 
                char_count[char] +=1
            else: 
                char_count[char] = 1 
    return char_count   

def sort(char_dict):
    filtered = {char: count for char, count in char_dict.items() if char.isalpha()}
    sorted_list = [{"char": char, "num": count} for char, count in filtered.items()]
    sorted_list.sort(key=lambda item: item["num"], reverse=True)
    return sorted_list
     
    