'''
Created on 10-Feb-2016

@author: Shreepad Patil
'''

"""
Program to generate 5x5 Maps. 
"""

import grid
import pickle

g = grid.grid(5,20,20,5)
g.generate()
f = open('10x10Map', 'wb+')
pickle.dump(g,f)
f.close()

g.printGrid()


