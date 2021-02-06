import re
import arrow
from reddit_api import reddit_api
import datetime
from datetime import timedelta
import time
from .cleaner.banned_words import banned_words
from .cleaner.clean_word import clean_word
from .cleaner.remove_space import remove_space


subs = ['bitcoin',
        'monero',
        'Bitcoincash',
        'ethereum',
        'Stellar',
        'cardano',
        'dogecoin',
        'Chainlink'
        ]


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


def print_results(submission):

    the_time_posted = determine_time(submission)

    print("")
    print(f"{TerminalColors.ENDC}{TerminalColors.WARNING}r/{submission.subreddit}{TerminalColors.ENDC}")
    print(the_time_posted)
    print(submission.id)

    print(f"{TerminalColors.ENDC}{TerminalColors.OKCYAN}{submission.title}{TerminalColors.ENDC}")

    print("")


def determine_time(submission):
    now = int(datetime.datetime.timestamp(datetime.datetime.today()))
    # account for time zone distance in california
    then_now = datetime.datetime.fromtimestamp(submission.created) - (timedelta(hours=3))

    utc = arrow.get(then_now)
    local = utc.to('local')
    readable_time = local.humanize()
    return readable_time


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
        time.sleep(3)
        subreddit = reddit.subreddit(sub)

        if sub == 'wallsteetbetsnew':
            limit_amount = 10
        elif sub == 'wallstreetbets':
            limit_amount = 20
        else:
            limit_amount = 5

        submissions = subreddit.new(limit=limit_amount)
        for submission in submissions:

            time.sleep(3)

            print_results(submission)
