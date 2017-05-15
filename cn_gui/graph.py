import matplotlib.pyplot as plt
import numpy as np


class Grapher():

    def __init__(self):
        x = 25

    def gen(self, arr, time):
        t = np.array(arr)
        s = np.array(time)
        plt.plot(s, t)
        plt.title('About as simple as it gets, folks')
        plt.grid(True)
        plt.savefig("test.png")
        plt.show()

