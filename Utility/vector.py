import numpy as np
import math

class Vector2:
    def __init__(self, sx, sy, ex, ey):
        self.sx = sx
        self.sy = sy
        self.ex = ex
        self.ey = ey

        self.start = (sx, sy)
        self.end = (ex, ey)

        self.xlen = ex - sx
        self.ylen = ey - sy
        self.length = np.sqrt(self.xlen**2 + self.ylen**2)

    def dot(self, other) -> float:
        dotprod = self.xlen * other.xlen + self.ylen * other.ylen
        return dotprod
    
    def normalize(self):
        """
        Normalizes current Vector,\n
        WILL CHANGE CURRENT VECTOR
        """
        if(self.length <= 0): return
        self.xlen /= self.length
        self.ylen /= self.length
        self.length /= self.length

    def get_norm(self):
        """
        Returns a normalized version of the Vector\n
        without changing the Vector itself.
        """
        if(self.length <= 0): return
        norm = Vector2(self.sx, self.sy, self.ex, self.ey)
        norm.normalize()
        return norm

