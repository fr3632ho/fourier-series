import numpy as np,scipy
import time
import matplotlib.pyplot as plt
import matplotlib.patches as patch
import DFT

class FourierIllustrator:
    PI = np.pi
    step = (2*PI)/60;

    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.radius = 20

    def init_figure(self):
        plt.figure(figsize=(8,6), dpi=80)
        plt.ion()
        plt.axis([-50,100,-50,50])
        plt.show()

    def draw_circle(self,x_pos,y_pos,radius):
        t = np.linspace(0,2*FourierIllustrator.PI,100)
        circle_x = x_pos + radius*np.cos(t)
        circle_y = y_pos + radius*np.sin(t)
        plt.plot(circle_x,circle_y,color='k')

    def draw_dot(self,x,y):
        plt.plot(x,y,marker='o',color='k')

    def clear_axis(self):
        plt.pause(0.001)
        plt.cla()
        plt.axis([-50,100,-50,50])

    def cycles(self,x_start,y_start,n,theta):
        prev_x = x_start
        prev_y = y_start
        for i in range(1,n+1):
            j = 2*i-1
            rad = self.radius *(4 / (j * FourierIllustrator.PI))
            self.draw_circle(prev_x,prev_y,rad)
            x_prime = prev_x + rad * np.cos(j*theta)
            y_prime = prev_y + rad * np.sin(j*theta)
            self.draw_dot([prev_x,x_prime],[prev_y,y_prime])
            prev_x = x_prime
            prev_y = y_prime
        return [prev_x,prev_y];

    def update_wave(self,wave):
        for i in range(1,len(wave)):
            wave[i][0] += 5*FourierIllustrator.step
        return wave

    def draw(self,n):
        wave = []
        self.init_figure()
        theta=0
        while theta < 16*FourierIllustrator.PI:
            xy = self.cycles(0,0,n,theta)
            wave.insert(0,[50,xy[1]])
            wave = self.update_wave(wave)
            self.draw_dot([xy[0],wave[0][0]],[xy[1],wave[0][1]])
            plt.plot(*zip(*wave))
            if len(wave) >= 500:
                wave.pop()
            theta+=FourierIllustrator.step;
            plt.draw()
            self.clear_axis()


n = input("Choose your n: ")
fourierTest = FourierIllustrator().draw(n)