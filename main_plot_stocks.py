
import matplotlib.pyplot as plt
import os

from os import path
from app import session
from app.models import Stocks, StocksCount
import matplotlib.animation as anim


while True:
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
    plt.clf()

    the_data = session.query(StocksCount).order_by(StocksCount.count.desc()).limit(20)

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
    plt.title("Live Updating Graph Mentions past 24 hours..")

    plt.pause(5)
    plt.clf()