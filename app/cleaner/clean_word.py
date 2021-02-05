import re
from .remove_space import remove_space


def clean_word(word):
    word = re.sub(r'[^\w]', ' ', word)
    word = word.lower()
    word = remove_space(word)
    return word

