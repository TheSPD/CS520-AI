'''
Created on 07-Feb-2016

@author: Shreepad Patil
@Ruid: 169005770
'''

import grid
import pickle

str = '10x10Map'

f = open(str, 'rb+')
g = pickle.load(f)
f.close()

g.printGrid()
