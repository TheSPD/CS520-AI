'''
Created on 12-Feb-2016

@author: Shreepad Patil
@NetID: sp1467 
'''

import aStarPath
import grid

def repeatedAStar(origMap,start,goal):
    agentMap = grid.grid(origMap.size,origMap.width,origMap.height,origMap.margin)
    agentPos = start
    path = []
    expandedCells = 0
    
    while not (agentPos.row == goal.row and agentPos.column == goal.column):
           
            #Update map           
            for neighbor in origMap.neighbors(agentPos):
                if(neighbor.isBlocked()):
                    agentMap.getCell(neighbor.row, neighbor.column).setBlocked(True)

            #Calculate best path as per available input
            bestPath,aStarExpandedCells = aStarPath.aStar(agentMap, goal, agentPos)
            expandedCells = expandedCells + aStarExpandedCells
            
            #If no path is available
            if(not bestPath):
                return None,expandedCells
            
            #Traverse 1 step in the direction
            #l = len(bestPath)-2
            (pathStepX,pathStepY) = bestPath[1]
            agentPos = origMap.getCell(pathStepX,pathStepY)
            
            #recordPath
            path.append(bestPath[1])
            
    return path,expandedCells 