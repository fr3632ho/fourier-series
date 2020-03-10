import numpy as np,scipy
import time
import matplotlib.pyplot as plt
import matplotlib.patches as patch

x_pos = -1
y_pos = 0
radius = 20;

def init_figure():
    plt.figure(figsize=(8,6), dpi=80)
    plt.ion()
    plt.axis([-50,100,-50,50])
    plt.show()

def draw_circle(x_pos,y_pos,radius):
    t = np.linspace(0,2*np.pi,100)
    circle_x = x_pos + radius*np.cos(t)
    circle_y = y_pos + radius*np.sin(t)
    plt.plot(circle_x,circle_y,color='k')
    plt.draw()

def draw_dot(x,y):
    plt.plot(x,y,marker='o',color='k')
    plt.draw()

def draw_wave(x,y):
    plt.plot(x,y,marker='.',color='k')
    plt.draw()

def clear_axis():
    plt.pause(0.01)
    plt.cla()
    plt.axis([-50,100,-50,50])

def draw():
    #initiate figure
    init_figure()
    step = (2*np.pi)/40;
    theta=0
    wave = []
    while theta < 8*np.pi:
        #Add the point to the points list and draw the canvas
        draw_circle(x_pos,y_pos,radius)
        x_dot = x_pos + radius*np.cos(theta)
        y_dot = y_pos + radius*np.sin(theta)
        wave.insert(0,y_dot)
        draw_dot(x_dot,y_dot)
        draw_dot([x_pos,x_dot],[y_pos,y_dot])
        for i in range(0,len(wave)):
            index = (4*i*step)+50
            if i == 0:
                draw_dot([x_dot,index],[y_dot,wave[i]])
            draw_dot(index,wave[i])

        if len(wave) >= 75:
            wave.pop()

        theta+=step
        clear_axis()

draw()
