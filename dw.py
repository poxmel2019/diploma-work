import numpy as np

def f():

    global mas
    someMas = [i for i in range(1,10)]
    emptyArray = []
    mas = []
    
  
    while True:
        path = input('Point path:\n')
        try:
            with open (path) as file:
                for x in file:
                    mas += [int(x)]
                file.close()
        except FileNotFoundError:
            if path == 'q': break
            elif path == '': print('You haven\'t entered')
            else: print('Error')
        except OSError:
            print('There is no the path')
        except ValueError:
            print("File has unreaded data")

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

        mas = []
    
