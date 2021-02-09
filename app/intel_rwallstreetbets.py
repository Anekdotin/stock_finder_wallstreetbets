import re
import arrow
from reddit_api import reddit_api
import datetime
from datetime import timedelta
import time
from .cleaner.banned_words import banned_words
from .cleaner.clean_word import clean_word
from .cleaner.remove_space import remove_space

from app import session
from app.models import Stocks, StocksCount


subs = ['wallstreetbets', 'wallstreetbetsnew', 'stocks', 'investing', 'pennystocks']


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


def add_symbol_todb(symbol, subreddit, reddit_post_id):

    now = datetime.datetime.utcnow()

    get_db_stock = session.query(Stocks) \
        .filter(Stocks.stockname == symbol,
                Stocks.reddit_post_id == reddit_post_id
                ) \
        .first()
    if get_db_stock is None:
        get_count_stock = session.query(StocksCount) \
            .filter(StocksCount.stockname == symbol) \
            .first()

        if get_count_stock is None:
            addnewentry = StocksCount(
                stockname=symbol,
                count=1,
                subreddit=subreddit
            )
            session.add(addnewentry)

        else:
            current_number = get_count_stock.count
            newnumber = current_number + 1
            get_count_stock.count = newnumber
            session.add(get_count_stock)

        addnewstockentry = Stocks(
            stockname=symbol,
            subreddit=subreddit,
            count=1,
            first_seen=now,
            last_seen=now,
            reddit_post_id=reddit_post_id
        )
        session.add(addnewstockentry)

    session.commit()



def print_results(word,  status, submission):
    if word is not None:
        cleaned_upper = clean_word(word)
        upper_word = cleaned_upper.upper()
    else:
        upper_word = None

    the_time_posted = determine_time(submission)

    print("")
    print(f"{TerminalColors.ENDC}{TerminalColors.WARNING}r/{submission.subreddit}{TerminalColors.ENDC}")
    print(the_time_posted)
    print(submission.id)
    print(f"{TerminalColors.ENDC}{TerminalColors.OKCYAN}{submission.title}{TerminalColors.ENDC}")

    if status is True:
        print(f"{TerminalColors.ENDC}Possible Stock Found: {TerminalColors.OKGREEN}${upper_word}{TerminalColors.ENDC} ")
        add_symbol_todb(symbol=upper_word, subreddit=submission.subreddit.display_name, reddit_post_id=submission.id)
    print("")


def hasnumbers(word):
    return any(char.isdigit() for char in word)


def determine_time(submission):
    # account for time zone distance in california
    then_now = datetime.datetime.fromtimestamp(submission.created) - (timedelta(hours=8))

    utc = arrow.get(then_now)
    local = utc.to('local')
    readable_time = local.humanize()
    return readable_time


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


def find_stock(thestring):
    has_stock = False
    f = None
    string_split = thestring.split()

    for f in string_split:
        if (len(f) == 3 or len(f) == 4 or len(f) == 5) and f.isupper():
            hasnumber = hasnumbers(f)
            bannedword = banned_words(f)
            if hasnumber is False and bannedword is False:
                f = remove_space(f)
                if valid_symbol(f) is True:
                    has_stock = True
                    f = f
                    break
                else:
                    has_stock = False
                    f = None
            else:
                has_stock = False
                f = None
        else:
            has_stock = False
            f = None
    return has_stock,  f


def main():
    reddit = reddit_api

    for sub in subs:

        time.sleep(3)
        subreddit = reddit.subreddit(sub)
        submissions = subreddit.new(limit=10)

        for submission in submissions:

            time.sleep(3)
            find_stock_ticker, f = find_stock(submission.title)
            print_results(f, find_stock_ticker, submission)
