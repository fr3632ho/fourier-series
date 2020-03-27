import numpy as np,scipy
import sys
import time
import matplotlib.pyplot as plt
import matplotlib.patches as patch
import DFT
from random import seed
from random import randint

y_hardcode = [50,50,50,50,50,50,50,50,50,50,-50,-50,-50,-50,-50,-50,-50,-50,-50,-50]
y_square = [[0,0],[0,10],[0,20],[0,30],[10,30],[20,30],[30,30],[30,20],[30,10],[30,0],[20,0],[10,0],[0,0]]
fourierX = []
fourierY = []
width = 100
height = 100

def setup(image):
    x = []
    y = []
    for i in image:
        x.insert(0,i[0])
        y.insert(0,i[1])
    x = DFT.DFT().transform(x)
    y = DFT.DFT().transform(y)
    return x,y
def create_random_list(n,size):
    y=[]
    seed(1)
    for _ in range(0,n):
        y.append(randint(-size,size))
    return y

class FourierIllustrator:
    PI = np.pi
    step = (2*PI)/60;

    def __init__(self):
        self.DFT = DFT.DFT()
        self.x_pos = 0
        self.y_pos = 0
        self.radius = 20

    def setup(self):
        print("hehe")

    def init_figure(self):
        plt.figure(figsize=(8,6), dpi=80)
        plt.ion()
        plt.axis([-width,width,-height,height])
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
        plt.axis([-width,width,-height,height])

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

    def cycles(self,x,y,time,rotation,fourier):
        x_prime,y_prime = x,y
        for complex in fourier:

            freq = complex.freq
            phase = complex.phase
            amp = complex.amp
            prev_x,prev_y,x,y = (x,
                y,
                x + amp * np.cos(freq*time + phase + rotation),
                y + amp * np.sin(freq*time + phase + rotation))
            self.draw_circle(prev_x,prev_y,amp)
            self.draw_dot([x,prev_x],[y,prev_y])
        return [x,y]


    def draw_transform(self,x,y):
        wave =[]
        self.init_figure()
        time=0
        while time < 10*FourierIllustrator.PI:
            vx,vy = self.cycles(-width/4,50,time,0,x), self.cycles(50,-width/4,time,np.pi/2,y)
            vect = [vx[0],vy[1]]
            wave.insert(0,vect)
            self.draw_dot([vx[0],vx[1]],[vect[0],vect[1]])
            self.draw_dot([vy[0],vy[1]],[vect[0],vect[1]])
            plt.plot(*zip(*wave))

            dt = (2*np.pi) / len(x)
            time+= dt;
            plt.draw()
            self.clear_axis()

            if time > 2*np.pi:
                wave = []
                time = 0

def parse_data(image):
    inp_file = sys.stdin

def start():
    if int(input("Series or Transform (1/0)")) == 0:
        fourierX, fourierY = setup(y_square)
        fourierX.sort(key=lambda x: x.amp, reverse=True)
        fourierY.sort(key=lambda y: y.amp, reverse=True)
        FourierIllustrator().draw_transform(fourierX,fourierY)
    else:
        n = int(input("Choose your n: "))
        laps = int(input("choose laps: "))
        fourierTest = FourierIllustrator().draw(n,laps)

start()
