
import matplotlib.pyplot as plt
import os

from os import path
from app import session
from app.models import Stocks, StocksCount
import matplotlib.animation as anim

from datetime import datetime, timedelta


while True:

    last_24_hours_stocks = []

    plt.rcParams.update({
        "lines.color": "white",
        "patch.edgecolor": "white",
        "text.color": "black",
        "axes.facecolor": "white",
        "axes.edgecolor": "lightgray",
        "axes.labelcolor": "white",
        "xtick.color": "white",
        "ytick.color": "white",
        "grid.color": "lightgray",
        "figure.facecolor": "black",
        "figure.edgecolor": "black",
        "savefig.facecolor": "black",
        "savefig.edgecolor": "black"})

    plt.style.use('dark_background')
    print("here")
    plt.show()
    plt.clf()

    filter_after = datetime.today() - timedelta(days=1)

    getlateststocks = session.query(Stocks)\
        .filter(Stocks.subreddit == 'pennystocks', Stocks.last_seen >=filter_after )\
        .limit(10)

    for f in getlateststocks:
        last_24_hours_stocks.append(f.stockname)

    the_data = session.query(StocksCount)\
        .filter(StocksCount.subreddit == 'pennystocks', StocksCount.stockname.in_(last_24_hours_stocks)) \
        .order_by(StocksCount.count.desc())\
        .limit(10)

    x_data = []
    y_data = []

    for f in the_data:
        x_data.append(f.stockname)

    for g in the_data:
        y_data.append(g.count)

    x_pos = [i for i, _ in enumerate(x_data)]

    plt.bar(x_data, y_data, color='green')
    plt.xlabel("Symbols")
    plt.ylabel("Mentions")
    plt.title("r/Pennystocks Live Updating Graph Mentions past 24 hours..")
    print("here2")
    plt.pause(5)
    plt.show()
    plt.clf()

