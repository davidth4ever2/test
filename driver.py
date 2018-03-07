import sys, copy
# breath-first search is a simple strategy in which the root node is expanded first
# then, all of the successors of the root node are expanded next, then their successors, and soo on.
# all the nodes are expanded at the given depth in the seach tree before any notes at the next level
# are expanded

action_sequence = 'up','down','left','right'

function_name = sys.argv[1]
goalState = [[0,1,2],[3,4,5],[6,7,8]]
exploredFrontier   = []
input_from_user = list()
input_from_user = sys.argv[2].split(',')


def vertical(input_array,int_direction):


    vertical_input_array = copy.deepcopy(input_array)    
    

    floor,door = findNonce(vertical_input_array)



    node_one = vertical_input_array # the first dimension is the
    temp = node_one[floor + int_direction][door]
    node_one[floor][door] = (temp)
    node_one[floor + int_direction][door] = 0
    #print "vertical floor value" + str(floor) 
    print "verticle done..." + str(node_one)
  
    return node_one

def horizontal(input_array,int_direction):

      
    h_input_array = copy.deepcopy(input_array)

    #print "horizontal input" + str(h_input_array)
    horizontal_input_array = copy.deepcopy(h_input_array)

    floor,door = findNonce(horizontal_input_array)



    #print "horizontal value " + str(door)
   

 

    node_one   = horizontal_input_array[floor][:]
    temp = node_one[door+int_direction]
    node_one[door] = temp
    node_one[door+int_direction] = 0
    horizontal_input_array[floor][:] = node_one
  
    print "horizontal done" + str(horizontal_input_array)
    return horizontal_input_array



def findNonce(input_array):  
    floor, door  = 0,0
    expand_array = copy.deepcopy(input_array)
            
    for i in expand_array:
        
       for j in i:

         if(j==str(0)):

             floor = expand_array.index(i)
             door  = i.index(j)
             return floor,door

    
    

def bfs():

    global input_from_user
    
  
    board = []
    

    print " length " + str(len(input_from_user))

    board.append(input_from_user[0:3])
    board.append(input_from_user[3:6])
    board.append(input_from_user[6:9])


    floor, door = findNonce(board)

    
    def findAvailableMoves(floor,door):

        moveList = ["U","D","L","R"]

        if(floor == 0):
           moveList.remove("U")
        if(floor == 2):
            moveList.remove("D")
        if(door == 0):
            moveList.remove("L")
        if(door == 2):
            moveList.remove("R")

        return (moveList)

   
    def getBranches(input_board):

        parent =  copy.deepcopy(input_board)
        child  =  []
        ml = findAvailableMoves(floor,door)

        branchList = []

        print str(ml)

        i = ml[0]
            
        if(i=="U" and exploredFrontier.count(input_board)< 1):
               
            input_listy = copy.deepcopy(input_board)
            child = vertical(input_listy,-1)  
           
            
        elif(i=="D" and exploredFrontier.count(input_board)< 1):

            print i
            
            input_listy = copy.deepcopy(input_board)
            child = vertical(input_listy,1)  
            
            
        
        elif(i=="L" and exploredFrontier.count(input_board)< 1):
            
            input_listx = copy.deepcopy(input_board)
            child = horizontal(input_listx,-1)
           
            

        elif(i=="R" and exploredFrontier.count(input_board)< 1):
            
            input_listx = copy.deepcopy(input_board)
            child = horizontal(input_listx,1)
            
               
            exploredFrontier.append(parent)
            exploredFrontier.append(child)

        print "appending parent > " + str(parent)
        print "appending child > " + str(child)

        branchList.append(parent)
        branchList.append(child)


        return branchList

    print "board=" + str(board)
    x = getBranches(board)
    print "X len->" + str(len(x))

    while(len(x) > 0):
        
        for i in x:

           print i
           
           x = getBranches(i)

           print "new x > " + str(x)
  

   
   

        
    

        
        
        

    

if(function_name == 'bfs'):
   
    bfs()



