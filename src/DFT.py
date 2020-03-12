import Complex
import math
import numpy as np,scipy

class DFT:

    def transform(y):
        N = len(y)
        X = []*N
        for k in range(0,N):
            discrete_freq=k/N
            re = 0
            im = 0
            for n in range(0,N):
                rad = ((2*np.pi)/N)*k*n
                re += y(n)*np.cos(rad)
                im -= y(n)*np.sin(rad)
        X[k] = Complex(re,im,discrete_freq)
        return X
