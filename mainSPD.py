'''
Created on 07-Feb-2016

@author: Shreepad Patil
@Ruid: 169005770
'''

import pickle
import cell
import grid
import aStarPath
from mhlib import PATH
import priorityQueue
import repeatedAStar
import repeatedBackwardAStar
import repeatedAdaptiveAStar
import heapq

import time

"""        
NewCell = cell(5,5)

NewCell.setBlocked(True)

if(NewCell.isBlocked()):
    print('Blocked')
else: 
    print('Unblocked')
"""    
#grid1 = grid.grid(5,20,20,5)


"""
grid1.getCell(3, 3).setBlocked(True)
grid1.getCell(4, 3).setBlocked(True)
grid1.getCell(3, 2).setBlocked(True)
"""
"""
grid1.down(grid1.getCell(8, 9)).setBlocked(True)

print grid1.getCell(2, 2).isBlocked()
"""

#grid1.generate()

"""
nodes_stack = [grid1.getCell(2,2)]

if not nodes_stack:
    print 'Empty'
elif nodes_stack:
    print 'Not Empty'

#nodes_stack.append(grid1.getCell(3,3))
#print nodes_stack.pop().row

print(random.randint(0,9))
"""
#grid1.printGrid()

s = 'Map1'


#Remove comment to run for 5x5
#s = '5x5Map'

#s = '10x10Map'

f = open(s, 'rb+')
g = pickle.load(f)
f.close()

start = cell.cell(0,0)
goal = cell.cell(0,0)

#print g.getCell(2,7).isBlocked() #75,90 

# For 101x101
start = cell.cell(10,4)
goal = cell.cell(75,90)

#For 5x5 
#start = cell.cell(0,1)
#goal = cell.cell(0,4)

#For 10x10
#start = cell.cell(6,4)
#goal = cell.cell(2,7)


t0 = time.time()
path=[]
#path,expCells = aStarPath.aStar(g, start, goal)

#Forward A Star
path,expCells = repeatedAStar.repeatedAStar(g, start, goal)

#Backward A Star
#path,expCells = repeatedBackwardAStar.repeatedAStar(g, start, goal)

#Adaptive A Star
#path,expCells = repeatedAdaptiveAStar.repeatedAStar(g, start, goal)

t1 = time.time()

if(path):
    path = [(start.row,start.column)] + path
print 'Time taken : %f' %(t1-t0),' Expanded Cells : %f' %(expCells) 
if(not path):
    print  'No path',' Time taken : %f' %(t1-t0),' Expanded Cells : %f' %(expCells) 

g.printGrid((start.row,start.column),(goal.row,goal.column),path)

#start = cell.cell(75,90)

#goal = cell.cell(15,20)
""""
openSet = priorityQueue.PriorityQueue()

openSet.put((5,5),4)

openSet.put((1,1),3)
openSet.put((3,2),5)
print openSet.elements.index((4,(5,5)))
openSet.elements[1] = openSet.elements[-1]
openSet.get()
heapq.heapify(openSet.elements) 
openSet.put((5,5),0)
print openSet.elements
"""
#t = openSet.get()

#print t





#path = aStarPath.aStar(grid1, start, goal)

#print path

#path = repeatedAStar.repeatedAStar(grid1, start, goal)

#print path

#print path
#print came_from.pop()

#print cost_so_far
'''
f = open('workfile', 'wb+')
pickle.dump(grid1,f)
f.close()

f = open('workfile', 'rb+')
grid2 = pickle.load(f)
f.close()

grid2.printGrid()
'''