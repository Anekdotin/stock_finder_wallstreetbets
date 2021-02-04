import re
import praw
import config
import datetime
import time

subs = ['wallstreetbets', 'wallstreetbetsnew']

listofstocks = []
banstuff = ['fuck', 'hold', 'vote', 'hodl', 'long', 'term',
            'into', 'open', 'wsb', 'new',
            'add', 'cnbc', 'real', 'pays', 'let', 'imo', 'mean',
            'it s', 'best', 'make', 'know',
            'look', 'mars', 'moon', 'fly', 'wsb', 'pull', 'i ll',
            'call', 'yolo', 'apes', 'sale', 'wtf', 'for', 'made', 'lmao',
            'all', 'day', 'down', 'zero', 'stop', 'shit', 'run', 'huge',
            'musk', 'hold', 'wsb', 'sec', 'dip', 'fool', 'moon', 'line',
            'the', 'have', 'aint', 'were', 'sell', 'put', 'wtf',
            'not', 'bull', 'psa', 'rip', 'you', 'can', 'fire', 'with',
            'your', 'some', 'next', 'buy', 'they', 'more',
            'low', 'yes', 'yall', 'why', 'bell',
            'out', 'fyi', 'hear', 'feel', 'like', 'are',
            'ship', 'how', 'that', 'lose',
            'just', 'dont', 'guys', 'lose', 'get', 'from',
            'more', 'what', 'is', 'how',
            'but', 'is', 'cry', 'just', 'dont', 'then',
            'over', 'lost', 'was', 'when', 'fyi',
            'and', 'here', 'this', 'calm', 'way', 'puts',
            'calm', 'nyse', 'IT S', 'boys',
            'time', 'dead', 'wont', 'give', 'ape', 'army',
            'now', 'big', 'mac', 'mega', 'porn', 'loss', 'bear',
            'TILL', 'take', 'off', 'keep', 'out', 'nakd',
            'lets', 'now', 'left', 'baby', 'dips',
            'help', 'gtfo', 'wsj', 'each', 'too',
            'its', 'wide', 'play', 'diy', 'no', 'yes', 'elon', 'musk', 'ez',
            'want', 'ffs', 'love', 'game', 'stay', 'fall',
            'will', 'i m', 'ipo', 'rice',
            'usa', 'read', 'oc', 'dfv', 'per'
            ]


def remove_space(word):
    return word.replace(" ", "")


def clean_word(word):
    word = re.sub(r'[^\w]', ' ', word)
    word = word.lower()
    word = remove_space(word)
    return word


def banned_words(word):
    word = clean_word(word)
    if word in banstuff:
        return True
    else:
        return False


def hasnumbers(word):
    return any(char.isdigit() for char in word)


def determine_time(submission):
    now = int(datetime.datetime.timestamp(datetime.datetime.today()))
    then = int(submission.created)

    return datetime.datetime.fromtimestamp(then).strftime('%Y-%m-%d %H:%M:%S')


def appendword(word):
    word = clean_word(word)
    word = word.upper()
    listofstocks.append(word)


def valid_symbol(word):
    if word.startswith('$'):
        appendword(word)
        return True

    elif (len(word) == 3 or len(word) == 4) and word.isupper():
        appendword(word)
        return True

    else:
        return False


def print_results(word, submission):

    cleaned_upper = clean_word(word)
    upper_word = cleaned_upper.upper()
    the_time_posted = determine_time(submission)
    print("*" * 10)
    print(submission.id)
    print(submission.title)
    print(the_time_posted)
    print("stock found: $" + upper_word)
    print("")


def main():
    reddit = praw.Reddit(client_id=config.client_id,
                         client_secret=config.client_secret,
                         password=config.password,
                         user_agent=config.user_agent,
                         username=config.username)
    for sub in subs:
        subreddit = reddit.subreddit(sub)
        submissions = subreddit.new(limit=50)
        for submission in submissions:

            time.sleep(1)
            string_split = submission.title.split()

            for f in string_split:

                if (len(f) == 3 or len(f) == 4) and f.isupper():
                    hasnumber = hasnumbers(f)
                    bannedword = banned_words(f)

                    if hasnumber is False and bannedword is False:
                        f = remove_space(f)
                        if valid_symbol(f) is True:
                            print_results(f, submission)



