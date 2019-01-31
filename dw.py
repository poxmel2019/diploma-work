from tkinter import *
from tkinter import messagebox
import numpy as np
import math

    
def f():
    # interface
    root = Tk()

    address = Entry()
    formats = Entry()
    
    button = Button()
    address.pack()
    
    root.mainloop()
def read_txt():
    pass
def read_xml():
    pass
def read_json():
    pass
def read_csv():
    pass
def read_xl():
    pass
def read_xls():
    pass

def ff():

    global mas
    someMas = [i for i in range(1,10)]
    emptyArray = []
    mas = []
    print('This is an array')
    print(mas)

    while True:
        path = input('Point path:\n')
        try:
            with open (path) as file:
                for x in file:
                    mas += [int(x)]
                file.close()
        except FileNotFoundError:
            if path == 'q': break
            else: print('Error')
        except OSError:
            print('There is no the path')

        print("This is an array: {0}".format(mas))

        try:    
            print("This is a maximum: {0}".format(max(mas))) # handy
            print("This is a minimum: {0}".format(min(mas))) # handy
            print("This is a mean: {0}".format(np.mean(mas))) # handy
            print("This is a median: {0}".format(np.mean(mas))) # handy
            print("This is a standard deviation: {0}".format(np.std(mas))) # handy
            print("This is a dispersion: {0}".format(np.var(mas))) # handy
        except ValueError:
            print('Empty array')
    
