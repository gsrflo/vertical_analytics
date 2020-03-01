import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np
import pandas as pandas
import yfinance as yf
from tkinter import *

import plot
import main

def drawgui(name_stock1, name_stock2, name_stock3,):
    window = Tk()
    window.title("Vertical Analytics")
    window.geometry('1000x800')
    # label
    lbl_stocks_headline = Label(window, text="Total Stock Return:", font=("Arial", 20))
    lbl_stocks_headline.grid(column=0, row=3)

    # div_stock1 = get_div(name_stock1)
    tsr_stock1 = plot.total_return(name_stock1)
    tsr_stock2 = plot.total_return(name_stock2)
    tsr_stock3 = plot.total_return(name_stock3)

    # creating total stock return labels
    text_tsr_stock1 = name_stock1 + ": " + str(tsr_stock1) + "%"
    text_tsr_stock2 = name_stock2 + ": " + str(tsr_stock2) + "%"
    text_tsr_stock3 = name_stock3 + ": " + str(tsr_stock3) + "%"

    lbl_stocks1 = Label(window, text=text_tsr_stock1, font=("Arial", 15))
    lbl_stocks1.grid(column=1, row=3)
    lbl_stock2 = Label(window, text=text_tsr_stock2, font=("Arial", 15))
    lbl_stock2.grid(column=1, row=4)
    lbl_stock3 = Label(window, text=text_tsr_stock3, font=("Arial", 15))
    lbl_stock3.grid(column=1, row=5)

    # entry box
    txt = Entry(window, width=10)
    txt.grid(column=1, row=10)

    # button
    btn = Button(window, text="Click Me")
    btn.grid(column=1, row=11)

    # diagram plot
    fig = plt.figure(1)
    plt.ion()
    plot.plot_diagram(main.name_stock1)
    plot.plot_diagram(main.name_stock2)
    plot.plot_diagram(main.name_stock3)
    canvas = FigureCanvasTkAgg(fig, master=window)
    plot_widget = canvas.get_tk_widget()
    plot_widget.grid(row=2, column=1)

    # updating figure - working?
    fig.canvas.draw()
    # updating window
    window.mainloop()

def import_plot():
    trollolo = 1
    #tk.Button(root, text="Update", command=update).grid(row=1, column=0)