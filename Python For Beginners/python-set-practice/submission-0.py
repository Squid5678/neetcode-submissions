from typing import List

def contains_duplicate(words: List[str]) -> bool:
    set_of_words = set()

    for word in words:
        if word in set_of_words:
            return True
        set_of_words.add(word)
    
    return False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
