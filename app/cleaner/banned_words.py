import re


from .clean_word import clean_word
from .remove_space import remove_space


banstuff = ['fuck', 'hold', 'vote', 'hodl', 'long', 'term',
            'into', 'open', 'wsb', 'new',
            'add', 'cnbc', 'real', 'pays', 'let', 'imo', 'mean',
            'it s', 'best', 'make', 'know',
            'look', 'mars', 'moon', 'fly', 'wsb', 'pull', 'i ll',
            'call', 'yolo', 'apes', 'sale', 'wtf',
            'for', 'made', 'lmao', 'back',
            'all', 'day', 'down', 'zero', 'stop',
            'shit', 'run', 'huge', 'gone',
            'musk', 'hold', 'wsb', 'sec', 'dip',
            'fool', 'moon', 'line', 'pain',
            'the', 'have', 'aint', 'were', 'sell',
            'put', 'wtf', 'our', 'who',
            'not', 'bull', 'psa', 'rip', 'you', 'can',
            'fire', 'with', 'one', 'hand',
            'your', 'some', 'next', 'buy', 'they','more',
            'low', 'yes', 'yall', 'why', 'bell',
            'out', 'fyi', 'hear', 'feel', 'like', 'are',
            'ship', 'how', 'that', 'lose',
            'just', 'dont', 'guys', 'lose', 'get', 'from',
            'more', 'what', 'is', 'how', 'avg',
            'but', 'is', 'cry', 'just', 'dont', 'then',
            'over', 'lost', 'was', 'when', 'fyi',
            'and', 'here', 'this', 'calm', 'way', 'puts',
            'calm', 'nyse', 'IT S', 'boys', 'go', 'very', 'halt',
            'time', 'dead', 'wont', 'give', 'ape', 'army',
            'now', 'big', 'mac', 'mega', 'porn', 'loss', 'bear',
            'TILL', 'take', 'off', 'keep', 'out', 'nakd',
            'lets', 'now', 'left', 'baby', 'dips',
            'help', 'gtfo', 'wsj', 'each', 'too',
            'its', 'wide', 'play', 'diy', 'no',
            'yes', 'elon', 'musk', 'ez','fall', 'yet',
            'want', 'ffs', 'love', 'game', 'stay',
            'will', 'i m', 'ipo', 'rice','need', 'full',
            'usa', 'read', 'oc', 'dfv', 'per', 'coal',
            'holy', 'rh', 'pay', 'pst', 'est', 'gang',
            'ryan', 'die', 'papa', 'than', "i'm", 'idk', 'pure'
            'ceo', 'red', 'till', 'red', 'op', 'said', 'dd',
            'won', 'fda', 'us', 'only', 'irs', 'got', 'see', 'did'
            ]


def banned_words(word):
    word = clean_word(word)
    if word in banstuff:
        return True
    else:
        return False
