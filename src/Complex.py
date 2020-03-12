import math

class Complex:

    def __init__(self,re,im,freq):
        self.re = re
        self.im = im
        self.freq = freq

    def amp(self):
        return math.sqrt(self.re * self.re + self.im*self.im)

    def phase(self):
        return math.atan2(self.im,self.re)

    def frequency(self):
        return self.freq
