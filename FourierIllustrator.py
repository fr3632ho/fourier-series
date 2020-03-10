import numpy as np,scipy
import time
import matplotlib.pyplot as plt
import matplotlib.patches as patch

class FourierIllustrator:
    PI = np.pi

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
        plt.draw()

    def draw_dot(self,x,y):
        plt.plot(x,y,marker='o',color='k')
        plt.draw()

    def draw_wave(self,x,y):
        plt.plot(x,y,marker='.',color='k')
        plt.draw()

    def clear_axis(self):
        plt.pause(0.01)
        plt.cla()
        plt.axis([-50,100,-50,50])

    def draw(self,n):
        self.init_figure()
        step = (2*FourierIllustrator.PI)/60;
        theta=0
        wave = []
        while theta < 8*FourierIllustrator.PI:
            prev_x = self.x_pos
            prev_y = self.y_pos
            for i in range(1,n+1):
                j = 2*i-1
                rad = self.radius *(4 / (j * FourierIllustrator.PI))
                self.draw_circle(prev_x,prev_y,rad)
                x_prime = prev_x + rad * np.cos(j*theta)
                y_prime = prev_y + rad * np.sin(j*theta)
                self.draw_dot([prev_x,x_prime],[prev_y,y_prime])
                plt.draw()
                prev_x = x_prime
                prev_y = y_prime

            wave.insert(0,prev_y)
            for i in range(0,len(wave)):
                index = (4*i*step)+50
                if i == 0:
                    self.draw_dot([prev_x,index],[prev_y,wave[i]])
                self.draw_dot(index,wave[i])
            if len(wave) >= 75:
                wave.pop()
            theta+=step
            self.clear_axis()

fourierTest = FourierIllustrator()
fourierTest.draw(4)
