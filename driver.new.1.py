import sys, copy
# breath-first search is a simple strategy in which the root nood is expanded first
# then, all of the successors of the root node are expanded next, then their successors, and soo on.
# all the nodes are expanded at the given depth in the seach tree before any notes at the next level
# are expanded




goalState = [[0,1,2],[3,4,5],[6,7,8]]
explored   = []

#for i in input:
#
#    for j in i:
#
#        print "value: " + str(j) + ' floor ' + str(input.index(i))  + ' door ' + str(i.index(j))
                
def expandNode(input_array):  
    
    expand_array = copy.deepcopy(input_array)
    return_value = [0,0]
    #input_array = [[8,3,4],[0,1,2],[5,6,7]]
    
    for i in expand_array:
        
        for j in i:

            if(j == 0):

                floor = expand_array.index(i)
                door  = i.index(j) 
                
                #print "value: " + str(j) + ' floor ' + str(input_array.index(i))  + ' door ' + str(i.index(j))

                return floor,door

    #UDLR

def vertical(input_array,int_direction):


    vertical_input_array = copy.deepcopy(input_array)    
    

    floor,door = expandNode(vertical_input_array)
    print "horizontal floor ->" + str(floor)
    print "horizontal door ->" + str(door)

    node_one = vertical_input_array # the first dimension is the
    temp = node_one[floor + int_direction][door]
    node_one[floor][door] = temp
    node_one[floor + int_direction][door] = 0
    #print "vertical floor value" + str(floor) 
    #print "verticle done..." + str(node_one)
    print str(node_one)
    return node_one

def horizontal(input_array,int_direction):

      
    h_input_array = copy.deepcopy(input_array)

    #print "horizontal input" + str(h_input_array)
    horizontal_input_array = copy.deepcopy(h_input_array)

    floor,door = expandNode(horizontal_input_array)

    print "vertical floor ->" + str(floor)
    print "vertical door ->" + str(door)

    #print "horizontal value " + str(door)
   

    print str(int_direction)

    node_one   = horizontal_input_array[floor][:]
    temp = node_one[door+int_direction]
    node_one[door] = temp
    node_one[door+int_direction] = 0
    horizontal_input_array[floor][:] = node_one
  
    #print "horizontal done" + str(horizontal_input_array)
    return horizontal_input_array

def createYBranches(n_input_array):
    y = copy.deepcopy(n_input_array)
    v_return = vertical(y,1)
    return v_return

def createXBranches(n_input_array):
    x = copy.deepcopy(n_input_array)
    v_return = horizontal(x,1)
    return v_return

    
    #while( !(branch_01_input==goalState) and (exploredBranch.count(branch_01_input) < 1) ):
def branchOut(input_board):

    list_of_test = list()

    floor,door = expandNode(input_board)

    def Up(input_board):
        
        print "Up" + " " + str(floor) + " " +  str(door)

    if(explored.count(input_board) < 1 and floor==0):
        
        input_listy = copy.deepcopy(input_board)
        ybranch_output = vertical(input_listy,1)  
        list_of_test.append(ybranch_output)

def Down(input_board):

    print "Down"+ " " + str(floor) + " " +  str(door)

    if(explored.count(input_board) < 1 or floor==2):
        
        input_listy = copy.deepcopy(input_board)
        ybranch_output = vertical(input_listy,-1)  
        list_of_test.append(ybranch_output)

def Left(input_board):

    print "Left"+ " " + str(floor) + " " +  str(door)

    if( explored.count(input_board) < 1 or  door==0):
        
        input_listx = copy.deepcopy(input_board)
        xbranch_output = horizontal(input_listx,-1)
        list_of_test.append(xbranch_output)
    

def Right(input_board):

    print "Right" + " " + str(floor) + " " +  str(door)

    if( explored.count(input_board) < 1 or door ==2):
        
        input_listx = copy.deepcopy(input_board)
        xbranch_output = horizontal(input_listx,1)
        list_of_test.append(xbranch_output)

    
    for i in range (0,4):
        
        if(i == 0):
           
           Up(input_board,floor,door)
           
        elif(i ==1):

            Down(input_board,floor,door)

        elif(i == 2):

            Left(input_board,floor,door)
    
        elif(i == 3):

            Right(input_board,floor,door)

            

def test(board):

    
   
    
    x = copy.deepcopy(branchOut(board))

    print str(x)



input_board_one = [[0,3,4],[8,1,2],[5,6,7]]

test(input_board_one)       
 
        

    
