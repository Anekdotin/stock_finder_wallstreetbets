import re

from reddit_api import reddit_api
import datetime
import time
from .cleaner.banned_words import banned_words
from .cleaner.clean_word import clean_word
from .cleaner.remove_space import remove_space


subs = ['wallstreetbets', 'wallstreetbetsnew', 'stocks', 'investing']


class TerminalColors:

    HEADER = '\033[95m'
    BLACK = '\033[40m'
    WHITE = '\033[47m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_results(word, submission):

    cleaned_upper = clean_word(word)
    upper_word = cleaned_upper.upper()
    the_time_posted = determine_time(submission)

    print("")
    print(f"{TerminalColors.ENDC}{TerminalColors.WARNING}r/{submission.subreddit}{TerminalColors.ENDC}")
    print(submission.id)
    print(f"{TerminalColors.ENDC}{TerminalColors.OKCYAN}{submission.title}{TerminalColors.ENDC}")
    print(the_time_posted)
    print(f"{TerminalColors.ENDC}Stock Found: {TerminalColors.OKGREEN}${upper_word}{TerminalColors.ENDC} ")
    print("")




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
        return True

    elif (len(word) == 3 or len(word) == 4) and word.isupper():
        return True

    else:
        return False


def main():
    reddit = reddit_api

    for sub in subs:
        subreddit = reddit.subreddit(sub)
        submissions = subreddit.new(limit=20)
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



