#import bolgrant
from tkinter import *
from tkinter import messagebox
import scipy.stats as scst
import statistics as st
import numpy as np
from pylab import *

def f():
    
    root = Tk()
    enteredText = StringVar()
    mas = []
    
    def readFile():
        mas = []
        address=enteredText.get()
        try:
            with open (address) as file:
                for x in file:
                    mas += [x]
                    print(x,end=" ")
                file.close()
        except FileNotFoundError:
            if address == "":# or address_of_file == None:
                messagebox.showinfo("Warning","Empty address")
            else:
                messagebox.showinfo("Warning","No file")
        
        except OSError:
            messagebox.showinfo("Warning","Invalid argument")

        except UnicodeDecodeError:
            messagebox.showinfo("Warning","This format is not able writtens")

        #print(enteredText.get())
        #print(address)
        print(mas)
   
        

    def cleanFile():
        entry.delete(0,END)


        
        

    
    
            
            
    entry = Entry(textvariable=enteredText)
    read_file = Button(text="read file",command=readFile)
    #process = Button(text="process")
    clean = Button(text="clean",command=cleanFile)
    

 

    
        
    entry.grid(row=0,column=0,padx="3",pady="3")
    read_file = Button(text="read file",command=readFile)
    read_file.grid(row=0,column=1,padx="3",pady="3")
    #process.grid(row=0,column=1,padx="3",pady="3")
    clean.grid(row=1,column=1,padx="3",pady="3")
    
    root.mainloop()

def f0():

    mas = [i for i in range(0,10)]
    ""
    print("Sample:",mas)
    print("Maximum:",max(mas))
    print("Minimum:",min(mas))
    print("Scope:",max(mas)-min(mas))
    print("Mean:",st.mean(mas))
    print("Median:",st.median(mas))
    print("Standard deviation:",np.std(mas))
    print("Variance:",np.var(mas))

    figure()
    hist(mas,bins=10)
    show()
    
    
    #for
def words():
    pass
    "Sample:"
    "Maximum:"
    "Minimum:"
    "Scope:"
    "Mean:"
    "Median:"
    "Standard deviation:"
    "Variance:"
    "Sample:"
    
    
    
