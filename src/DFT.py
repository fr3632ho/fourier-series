import Complex
import math
import numpy as np,scipy

class DFT:

    def __init__(self):
        print("DFT Initiated")

    def transform(self,y):
        N = len(y)
        X = [0]*N
        for k in range(0,N):
            re = 0
            im = 0
            for n in range(0,N):
                phi = (2*np.pi * k * n)/N
                re += y[n]*np.cos(phi)
                im -= y[n]*np.sin(phi)
            re = re / N
            im = im / N
            freq = k
            phase = np.arctan2(im,re)
            amplitude = np.sqrt(re * re + im * im)
            X[k] = Complex.Complex(re,im,freq,phase,amplitude)
        return X
