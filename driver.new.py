# breath-first search is a simple strategy in which the root nood is expanded first
# then, all of the successors of the root node are expanded next, then their successors, and soo on.
# all the nodes are expanded at the given depth in the seach tree before any notes at the next level
# are expanded


input = [[0,3,4],[8,1,2],[5,6,7]]

goalState = [[0,1,2],[3,4,5],[6,7,8]]

for i in input:
    for j in i:
        print "value: " + str(j) + ' floor ' + str(input.index(i))  + ' door ' + str(i.index(j))

floor = -1
door  = -1


def findNonce(board):
    
    if (type(board) == list):

        x, y = 0,0

        for y in range(0, len(board)):

            for x in range(0, len(board[y])):

                if(board[y][x] == '0'):

                    current_nonce_location = [y, x]

                    return current_nonce_location
                
def expandNode(input_array):  
    
    return_value = [0,0]
    #input_array = [[8,3,4],[0,1,2],[5,6,7]]
    
    for i in input_array:
        
        for j in i:

            if(j == 0):

                floor = input_array.index(i)
                door  = i.index(j) 
                
                #print "value: " + str(j) + ' floor ' + str(input_array.index(i))  + ' door ' + str(i.index(j))

                return floor,door

    #UDLR

def vertical(input_array,int_direction):

    vertical_input_array = input_array[:][:]

    floor =  (expandNode(vertical_input_array)[0])
    door  =  (expandNode(vertical_input_array)[1])
    
# initialize variables

    node_one = vertical_input_array[:][:] # the first dimension is the
    temp = node_one[floor + int_direction][door]
    node_one[floor][door] = temp
    node_one[floor + int_direction][door] = 0

    print "verticle done" + str(vertical_input_array)

    return node_one

def horizontal(input_array,int_direction):

    horizontal_input_array = input_array[:][:]

    floor =  (expandNode(horizontal_input_array)[0])
    door  =  (expandNode(horizontal_input_array)[1])


    node_one   = horizontal_input_array[floor][:]
    temp = node_one[door+int_direction]
    node_one[door] = temp
    node_one[door+int_direction] = 0
    horizontal_input_array[floor][:] = node_one
  
    print "horizontal done" + str(horizontal_input_array)
    return horizontal_input_array


def createBranches(n_input_array):

    a = [[0,0,0],[0,0,0],[0,0,0]]
    b = [[0,0,0],[0,0,0],[0,0,0]]
    
    exploredBranch = []
    exploredCount  = 0
    attempts = 2
    
    print "........................................"

    branch_01 = []
    branch_01_count = 0
    branch_01_input = []


    print "........................................"

    branch_02 = []
    branch_02_count = 0
    branch_02_input = [] 


    
    



    #################################
    a = n_input_array[:][:] # horizontal 
    b = n_input_array[:][:]

    #IC = INPUT_ARRAY[:][:]



   
    
    branch_01_input = horizontal(a,1)[:][:]
    print " branch number 1 " + str(branch_01_input)

    branch_02_input = vertical(b,1)[:][:]
    print " branch number 2 " + str(branch_02_input)



    
    #while( !(branch_01_input==goalState) and (exploredBranch.count(branch_01_input) < 1) ):
    for i in range(0,attempts):

        print "inside loop" + repr(branch_01_input)
        print "inside loop" + repr(branch_02_input)

        if((branch_01_input!=goalState)):

            if(exploredBranch.count(branch_01_input) < 1):

                print "starting position branch 1 ***** " + str(branch_01_input)

                exploredBranch.insert(exploredCount, branch_01_input)
                exploredCount = exploredCount + 1
                branch_01.insert(branch_01_count,branch_01_input)
                branch_01_count = branch_01_count + 1
                branch_01_input = horizontal(branch_01_input,1)


        if((branch_02_input!=goalState)):

            if(exploredBranch.count(branch_02_input) < 1):


                exploredBranch.insert(exploredCount,branch_02_input)
                exploredCount = exploredCount + 1
                branch_02.insert(branch_02_count,branch_02_input)
                branch_02_count = branch_02_count + 1
                branch_02_input = vertical(branch_02_input,1)

    #################################
    
    #
    #horizontal(a,1)
    #################################
    
    
    
    #print vertical(a)

    
#   
#
#
#
#
def test():
    
    a = [[0,3,4],[8,1,2],[5,6,7]]
    print "starting intput " + str(a)
    createBranches(a)
    
test()       

        

    
