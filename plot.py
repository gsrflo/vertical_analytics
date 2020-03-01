#dividenden zahlungen summieren

#splits sind bereits eingeprisen

import matplotlib.pyplot as plt
import numpy as np
import pandas as pandas
import yfinance as yf

time_span = '1y'

def my_function():
  print("Hello from a function")

def plot_diagram(name, data, tsr):
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
    #1. check where div vector =! 0
    #dividends_nonzero = dividends > 0
    #dividends_nonzero = np.nonzero(dividends)
    #dividends_nonzero = np.where(np.any(dividends > 0))
    #2. get div

    #3. accumulate div to every following close value

    acc_dividends = np.sum(dividends)
    mean_dividends = np.mean(dividends)
    print("Acc. Div.")
    print(acc_dividends)

    #Plots in Prozente umrechnen
    start_value = close[0] #ersten Werte der Matrix
    close_per = ((close) * 100 / start_value) - 100
    #close_per = ((close+acc_dividends) * 100 / start_value) - 100 --> für einkalkulierte dividenden
    print("Close Prozent")
    print(close_per[-1])
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
    print("Total stock return of " + name)
    print(tsr)
    return tsr

def main():
    #init stocks
    name_stock1 = "AAPL"
    name_stock2 = "SKT"
    name_stock3 = "GOOG"
    name_stock4 = "URTH"
    #portfolio_name = "Portfolio"

    #download form yf
    hist_stock1 = get_hist(name_stock1)
    hist_stock2 = get_hist(name_stock2)
    hist_stock3 = get_hist(name_stock3)
    hist_stock4 = get_hist(name_stock4)

    #div_stock1 = get_div(name_stock1)
    tsr_stock1 = total_return(name_stock1)
    tsr_stock2 = total_return(name_stock2)
    tsr_stock3 = total_return(name_stock3)
    tsr_stock4 = total_return(name_stock4)

    #create plots
    plot_diagram(name_stock1, hist_stock1, tsr_stock1)
    plot_diagram(name_stock2, hist_stock2, tsr_stock2)
    plot_diagram(name_stock3, hist_stock3, tsr_stock3)
    plot_diagram(name_stock4, hist_stock4, tsr_stock4)

    #plot
    plt.legend(loc="upper left")
    plt.show()

    #debug
    #print(div_stock1)


    my_function()


if __name__== "__main__":
  main()