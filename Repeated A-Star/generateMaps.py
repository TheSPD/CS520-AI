'''
Created on 07-Feb-2016

@author: Shreepad Patil
@Ruid: 169005770
'''

"""
Program to generate 50 101x101 Maps. 
"""

import grid
import pickle

for i in range(1,51):
    g = grid.grid(101,5,5,1)
    g.generate()
    f = open('Map' + str(i), 'wb+')
    pickle.dump(g,f)
    f.close()
