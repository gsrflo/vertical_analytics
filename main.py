# ******************
# * main file      *
# ******************

#TODO:
# GUI:
#   - user input: stock & time span
#   - solving closing issue
#   - graph updating
#   - graph manipulating
# dynamic data handling
# adquat total retun graph


import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

import plot
import gui

# init stocks
name_stock1 = "AAPL"
name_stock2 = "SKT"
name_stock3 = "GOOG"
name_stock4 = "URTH"

def main():

    # gui
    gui.drawgui(name_stock1, name_stock2, name_stock3)


if __name__== "__main__":
  main()