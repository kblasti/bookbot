def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_count = {}
    for char in text:
        all_char = char.lower()
        if all_char not in char_count:
            char_count[all_char] = 1
        else:
            char_count[all_char] += 1
    return char_count

def sort_on(char_count):
    return list(char_count.values())[0]

def sorted_dict(char_count):
    input_list = [{char: count} for char, count in char_count.items()]
    input_list.sort(reverse=True, key=sort_on)
    return input_list

