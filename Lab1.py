import numpy as np
import math

if __name__ == '__main__':
    print("-"*19)
    print("|{0:8}|{1:8}|".format('x', 'y'))
    print("-"*19)
    for x in np.arange(-0.4, 0.8, 3*math.pi/13):
        print("|%8.3f|%8.3f|" % (x, - math.sin(6*x) - 1/math.tan(x)))
    print("-"*19)
    input()