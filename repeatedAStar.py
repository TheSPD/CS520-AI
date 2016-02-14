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
    
    while not (agentPos.row == goal.row and agentPos.column == goal.column):
           
            #Update map           
            for neighbor in origMap.neighbors(agentPos):
                if(neighbor.isBlocked()):
                    agentMap.getCell(neighbor.row, neighbor.column).setBlocked(True)

            #Calculate best path as per available input
            bestPath = aStarPath.aStar(agentMap, agentPos, goal)
            
            #If no path is available
            if(not bestPath):
                return None
            
            #Traverse 1 step in the direction
            l = len(bestPath)-2
            (pathStepX,pathStepY) = bestPath[l]
            agentPos = origMap.getCell(pathStepX,pathStepY)
            
            #recordPath
            path.append(bestPath[l])
            
    return path 