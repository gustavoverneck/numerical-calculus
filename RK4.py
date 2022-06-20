# ------ RK4 ------

from math import *
import matplotlib.pyplot as plt

# RK4 Method

class RK4:
    def __init__(self):
        self.function = str(input("Insira a expressão da equação: "))
        self.x0 = float(input("Insira x inicial: "))
        self.t0 = float(input("Insira t inicial: "))
        self.t = float(input("Insira o t final: "))
        self.tf = self.t
        self.h = 0.0001
        self.resT = []
        self.resX = []
        self.runRK4()
     
    def f(self, t, x):
        return eval(self.function)
    
    def k1(self, t0, x0):
        return self.h*(self.f(self.t0, self.x0))
    
    def k2(self, t, x):
        return self.h*(self.f(t + 0.5 * self.h, x + 0.5 * self.k1(t, x)))
    
    def k3(self, t, x):
        return self.h * self.f(self.t0 + 0.5 * self.h, x + 0.5* self.k2(t, x))

    def k4(self, t, x):
        return self.h * self.f(self.x0 + self.h, t + self.k3(x, t))
    
    def calculate_k(self):
        self.storageResults(self.t0, self.x0)
        self.c1 = self.k1(self.t0, self.x0)
        self.c2 = self.k2(self.t0, self.x0)
        self.c3 = self.k3(self.t0, self.x0)
        self.c4 = self.k4(self.t0, self.x0)
        self.k = (self.c1+2*self.c2+2*self.c3+self.c4)/6
        self.x0 += self.k
        self.t0 += self.h
    
    def storageResults(self, t, x):
        self.resT.append(t)
        self.resX.append(x)

    def runRK4(self):
        while self.t0 <= self.tf:
            self.calculate_k()
        self.plotGraph()

    def plotGraph(self):
        plt.xlabel("Time [s]")
        plt.ylabel("Position [m]")
        plt.title("Position over time")
        plt.plot(self.resT, self.resX)
        plt.show()

def main():
    RK4()

if __name__ == '__main__':
    main()