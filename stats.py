def get_book_word_count(book):
    return len(book.split())

def count_characters(book):
    new_dict = {}
    for i in book:
        if i.lower() in new_dict:
            new_dict[i.lower()] += 1
        else:
            new_dict[i.lower()] = 1
    return new_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    list = []
    for i in dict:
        if i.isalpha():
            list.append({"char": i, "num": dict[i]})
    list.sort(reverse=True, key=sort_on)
    return list
