# functions for plotting graphs

#import libs
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

import yfinance as yf
import numpy as np
import pandas as pandas
import main

time_span = '1y'

def plot_diagram(name):
    data = get_hist(name)
    plt.plot(data, label = name)
    plt.ylabel('%')
    plt.xlabel('Time')
    plt.grid(True)
    plt.legend()
    plt.title('Stock Chart')
    return

def get_hist(name):
    stock = yf.Ticker(name)
    hist = stock.history(period = time_span)
    close = hist['Close']

    #include dividends to chart
    dividends = hist['Dividends']

    acc_dividends = np.sum(dividends)
    mean_dividends = np.mean(dividends)

    #Plots in Prozente umrechnen
    start_value = close[0] #ersten Werte der Matrix
    close_per = ((close) * 100 / start_value) - 100
    #print("Close Prozent")
    #print(close_per[-1])
    return close_per

def get_div(name):
    stock = yf.Ticker(name)
    div = stock.dividends
    return div

def total_return(name):
    stock = yf.Ticker(name)
    hist = stock.history(period = time_span)
    close = hist['Close']
    dividends = hist['Dividends']

    # total stock return = ((P1-P0)+sum(D) /P0)
    price_start = close[0]
    price_end = close[-1]
    acc_dividends = np.sum(dividends)
    tsr = ((price_end-price_start+acc_dividends))/price_start*100
    tsr = round(tsr,2)
    return tsr

def drawplot(name_stock1, name_stock2, name_stock3):

    tsr_stock1 = total_return(name_stock1)
    tsr_stock2 = total_return(name_stock2)
    tsr_stock3 = total_return(name_stock3)


    #download from yf
    hist_stock1 = get_hist(name_stock1)
    hist_stock2 = get_hist(name_stock2)
    hist_stock3 = get_hist(name_stock3)


    # create plots
    plot_diagram(name_stock1)
    plot_diagram(name_stock2)
    plot_diagram(name_stock3)


    # plot
    plt.legend(loc="upper left")
    plt.show()


