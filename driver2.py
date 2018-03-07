import sys, copy 
from collections import deque


class Actions:

    action_board = []
    frontier = []
    explored = []

    def __init__(self,input_board):
        
        self.action_board = copy.deepcopy(input_board)

        self.floor,self.door = findNonce(self.action_board)

        
    def Up(self):
        
        self.action_board
    
    def Down():

        self.action_board
        
        print down
    
    def Left():
        
        self.action_board
        
        print left
    
    def Right():

        self.action_board
        
    def findNextAction():

        if upavailable try it 
        if downavailble try it 
        if left available try it 
        if right avaiable try it

     
        print str(self.floor)
        print str(self.door)



board     = []
goalState = []
path_cost = 0

input_from_user = sys.argv[2].split(',')


sorted_input_string = sorted(input_from_user)

board.append(input_from_user[0:3])
board.append(input_from_user[3:6])
board.append(input_from_user[6:9])

print str(board)

goalState.append(sorted_input_string[0:3])
goalState.append(sorted_input_string[3:6])
goalState.append(sorted_input_string[6:9])


#print str(goalState)

def findNonce(input_array):
    
    floor, door  = 0,0
    
    expand_array = copy.deepcopy(input_array)
            
    for i in expand_array:
        
       for j in i:

         if(j==str(0)):

             floor = expand_array.index(i)

             door  = i.index(j)

             return floor,door



def bfs(board):

    explored = []
    this_board = copy.deepcopy(board)

    actions = Actions(this_board)
    
    print str(actions.door) + " door "
    

    print str(actions.floor) +  " floor "
    print str(actions.door)  + " door "

    if( not(this_board==goalState) ):
        explored.append(this_board)
    


        






    return this_board

def findNonce(input_array):  
    floor, door  = 0,0
    expand_array = copy.deepcopy(input_array)
            
    for i in expand_array:
        
       for j in i:

         if(j==str(0)):

             floor = expand_array.index(i)
             door  = i.index(j)
             return floor,door


bfs(board)











