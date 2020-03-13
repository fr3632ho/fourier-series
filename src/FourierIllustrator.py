import numpy as np,scipy
import time
import matplotlib.pyplot as plt
import matplotlib.patches as patch
import DFT
from random import seed
from random import randint

y_test = [10,10,10,10,10,10,10,-10,-10,-10,-10,-10,-10,-10,10,10,10,10,10,10,10,-10,-10,-10,-10,-10,-10,-10,10,10,10,10,10,10,10,-10,-10,-10,-10,-10,-10,-10,10,10,10,10,10,10,10,-10,-10,-10,-10,-10,-10,-10,10,10,10,10,10,10,10,-10,-10,-10,-10,-10,-10,-10,10,10,10,10,10,10,10,-10,-10,-10,-10,-10,-10,-10,10,10,10,10,10,10,10,-10,-10,-10,-10,-10,-10,-10,10,10,10,10,10,10,10,-10,-10,-10,-10,-10,-10,-10]

class FourierIllustrator:
    PI = np.pi
    step = (2*PI)/60;

    def __init__(self):
        self.DFT = DFT.DFT()
        self.x_pos = 0
        self.y_pos = 0
        self.radius = 20

    def init_figure(self):
        plt.figure(figsize=(8,6), dpi=80)
        plt.ion()
        plt.axis([-50,100,-50,50])
        plt.show()

    def draw_circle(self,x_pos,y_pos,radius):
        t = np.linspace(0,2*FourierIllustrator.PI,35)
        circle_x = x_pos + radius*np.cos(t)
        circle_y = y_pos + radius*np.sin(t)
        plt.plot(circle_x,circle_y,color='k')

    def draw_dot(self,x,y):
        plt.plot(x,y,marker='o',color='k')

    def clear_axis(self):
        plt.pause(0.001)
        plt.cla()
        plt.axis([-50,100,-50,50])

    def update_wave(self,wave):
        for i in range(1,len(wave)):
            wave[i][0] += 5*FourierIllustrator.step
        return wave

    def draw(self,n,laps):
        wave = []
        self.init_figure()
        theta=0
        while theta < 2*laps*FourierIllustrator.PI:
            prev_x = self.x_pos
            prev_y = self.y_pos
            for i in range(1,n+1):
                j = 2*i-1
                rad = self.radius *(4 / (j * FourierIllustrator.PI))
                self.draw_circle(prev_x,prev_y,rad)
                x_prime = prev_x + rad * np.cos(j*theta)
                y_prime = prev_y + rad * np.sin(j*theta)
                self.draw_dot([prev_x,x_prime],[prev_y,y_prime])
                prev_x = x_prime
                prev_y = y_prime

            wave.insert(0,[50,prev_y])
            wave = self.update_wave(wave)
            self.draw_dot([prev_x,wave[0][0]],[prev_y,wave[0][1]])
            plt.plot(*zip(*wave))
            if len(wave) >= 500:
                wave.pop()
            theta+=FourierIllustrator.step;
            plt.draw()
            self.clear_axis()

n = int(input("Choose your n: "))
laps = int(input("choose laps: "))
fourierTest = FourierIllustrator().draw(n,laps)

def create_random_list(n,size):
    y=[]
    seed(1)
    for _ in range(0,n):
        y.append(randint(-size,size))
    return y

print("nagger")
